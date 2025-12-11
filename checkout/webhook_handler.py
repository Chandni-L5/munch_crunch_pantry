from django.urls import reverse
import stripe
import json
import time
import logging

from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.core.mail import send_mail

from .models import Order, OrderLineItem
from products.models import ProductQuantity
from profiles.models import UserProfile

logger = logging.getLogger(__name__)

stripe.api_key = settings.STRIPE_SECRET_KEY


class StripeWH_Handler:
    """
    Handle Stripe webhooks
    """

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """Send the user an order confirmation email."""
        cust_email = order.email
        request = self.request

        if order.user_profile:
            base_url = reverse("order_history", args=[order.order_number])
        else:
            base_url = reverse("checkout_success", args=[order.order_number])

        order_url = request.build_absolute_uri(f"{base_url}?from_email=1")

        subject = render_to_string(
            "checkout/confirmation_emails/confirmation_email_subject.txt",
            {"order": order},
        ).strip()

        body = render_to_string(
            "checkout/confirmation_emails/confirmation_email_body.txt",
            {
                "order": order,
                "contact_email": settings.DEFAULT_FROM_EMAIL,
                "order_url": order_url,
            },
        )
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email],
        )

    def handle_event(self, event):
        """Handle unexpected webhook events."""
        logger.warning("Unhandled webhook received: %s", event["type"])
        return HttpResponse(
            content=f"Unhandled webhook received: {event['type']}",
            status=200,
        )

    def handle_payment_intent_succeeded(self, event):
        """Handle the payment_intent.succeeded webhook."""
        intent = event["data"]["object"]
        pid = intent["id"]
        metadata = intent.get("metadata", {}) or {}
        basket_str = metadata.get("basket")
        username = metadata.get("username", "AnonymousUser")
        save_info = metadata.get("save_info", "false")

        if not basket_str:
            logger.error("No basket metadata for PI %s", pid)
            return HttpResponse("Webhook: missing basket metadata", status=400)

        stripe_charge = stripe.Charge.retrieve(intent["latest_charge"])
        billing_details = stripe_charge["billing_details"]
        grand_total = round(stripe_charge["amount"] / 100, 2)

        shipping_details = intent.get("shipping", {}) or {}
        shipping_address = shipping_details.get("address", {}) or {}

        for field, value in shipping_address.items():
            if value == "":
                shipping_address[field] = None

        profile = None
        if username != "AnonymousUser":
            try:
                user = User.objects.get(username=username)
                profile, created = UserProfile.objects.get_or_create(user=user)

                if save_info == "true":
                    profile.default_phone_number = shipping_details.get(
                        "phone"
                    )
                    profile.default_street_address1 = shipping_address.get(
                        "line1"
                    )
                    profile.default_street_address2 = shipping_address.get(
                        "line2"
                    )
                    profile.default_town_or_city = shipping_address.get("city")
                    profile.default_postcode = shipping_address.get(
                        "postal_code"
                    )
                    profile.default_country = shipping_address.get("country")
                    profile.save()
            except User.DoesNotExist:
                logger.warning(
                    "Username %s from metadata not found when handling PI %s",
                    username,
                    pid,
                )

        order_exists = False
        order = None
        attempt = 1

        while attempt <= 5 and not order_exists:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.get("name"),
                    email__iexact=billing_details.get("email"),
                    phone_number__iexact=shipping_details.get("phone"),
                    country__iexact=shipping_address.get("country"),
                    postcode__iexact=shipping_address.get("postal_code"),
                    town_or_city__iexact=shipping_address.get("city"),
                    street_address1__iexact=shipping_address.get("line1"),
                    street_address2__iexact=shipping_address.get("line2"),
                    grand_total=grand_total,
                    original_basket=basket_str,
                    stripe_pid=pid,
                )
                order_exists = True
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)

        if order_exists:
            logger.info(
                "Order already exists for PI %s (%s)",
                pid,
                order.order_number,
            )
            self._send_confirmation_email(order)
            logger.info(
                "Confirmation email sent for order %s to %s",
                order.order_number,
                order.email,
            )
            return HttpResponse("Webhook: order already exists", status=200)

        try:
            order = Order.objects.create(
                full_name=shipping_details.get("name"),
                email=billing_details.get("email"),
                phone_number=shipping_details.get("phone"),
                country=shipping_address.get("country"),
                postcode=shipping_address.get("postal_code"),
                town_or_city=shipping_address.get("city"),
                street_address1=shipping_address.get("line1"),
                street_address2=shipping_address.get("line2"),
                original_basket=basket_str or "",
                stripe_pid=pid,
                user_profile=profile,
            )

            basket = json.loads(basket_str)

            for item_id, quantity in basket.items():
                try:
                    product_quantity = ProductQuantity.objects.get(pk=item_id)
                except ProductQuantity.DoesNotExist:
                    logger.warning(
                        "ProductQuantity %s missing – skipping",
                        item_id,
                    )
                    continue

                OrderLineItem.objects.create(
                    order=order,
                    product_quantity=product_quantity,
                    quantity=quantity,
                )

            order.update_total()
            self._send_confirmation_email(order)
            logger.info(
                "Order created by webhook for PI %s (%s)",
                pid,
                order.order_number,
            )
            return HttpResponse("Webhook: order created", status=200)

        except Exception as e:
            logger.error("Error creating order for PI %s: %s", pid, e)
            if order:
                order.delete()
            return HttpResponse("Webhook: error creating order", status=500)

    def handle_payment_intent_payment_failed(self, event):
        """Handle the payment_intent.payment_failed webhook."""
        pid = event["data"]["object"]["id"]
        logger.warning("Payment failed for PI %s", pid)
        return HttpResponse(
            content=f"Webhook: payment failed for {pid}",
            status=200,
        )
