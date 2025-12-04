from django.http import HttpResponse
import stripe

from munch_crunch_pantry import settings

from .models import Order, OrderLineItem
from products.models import ProductQuantity

import json
import time

stripe.api_key = settings.STRIPE_SECRET_KEY


class StripeWH_Handler:
    """
    Handle Stripe webhooks
    """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle an unexpected webhook event.
        """
        return HttpResponse(
            content=f"Unhandled webhook received: {event['type']}",
            status=200,
        )

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe.
        - Try to find an order already created by the checkout view.
        - If it doesn't exist, create it using the PaymentIntent data and metadata.
        """
        intent = event["data"]["object"]
        pid = intent["id"]
        metadata = intent.get("metadata", {})
        basket_str = metadata.get("basket")
        save_info = metadata.get("save_info")
        username = metadata.get("username")
        stripe_charge = stripe.Charge.retrieve(intent["latest_charge"])
        billing_details = stripe_charge["billing_details"]
        grand_total = round(stripe_charge["amount"] / 100, 2)
        shipping_details = intent.get("shipping", {}) or {}
        shipping_address = shipping_details.get("address", {}) or {}

        for field, value in shipping_address.items():
            if value == "":
                shipping_address[field] = None

        order = None
        order_exists = False
        attempt = 1
        max_attempts = 5

        while attempt <= max_attempts and not order_exists:
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
                )
                order_exists = True
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)

        if order_exists:
            print(
                f"✅ Webhook: Order already exists for PI {pid} "
                f"(order_number={order.order_number})"
            )
            return HttpResponse(
                content="Webhook: order already exists",
                status=200,
            )

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
            )

            if hasattr(order, "original_basket"):
                order.original_basket = basket_str
            if hasattr(order, "stripe_pid"):
                order.stripe_pid = pid
            order.save()

            basket = json.loads(basket_str) if basket_str else {}

            for item_id, quantity in basket.items():
                try:
                    product_quantity = ProductQuantity.objects.get(pk=item_id)
                except ProductQuantity.DoesNotExist:
                    continue

                OrderLineItem.objects.create(
                    order=order,
                    product_quantity=product_quantity,
                    quantity=quantity,
                )

            order.update_total()

            print(
                f"✅ Webhook: Created order via webhook for PI {pid} "
                f"(order_number={order.order_number})"
            )

            return HttpResponse(
                content="Webhook: order created",
                status=200,
            )

        except Exception as e:
            print(f"❌ Webhook error while creating order for PI {pid}: {e}")
            if order:
                order.delete()
            return HttpResponse(
                content="Webhook: error creating order",
                status=500,
            )

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe.
        """
        intent = event["data"]["object"]
        pid = intent["id"]
        return HttpResponse(
            content=f"Webhook received: {event['type']} for PaymentIntent {pid}",
            status=200,
        )
