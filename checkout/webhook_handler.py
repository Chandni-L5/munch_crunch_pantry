from django.urls import reverse
import stripe
import logging

from django.http import HttpResponse
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import send_mail

from .models import Order

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
        intent = event["data"]["object"]
        pid = intent["id"]

        order = Order.objects.filter(stripe_pid=pid).first()

        if not order:
            logger.warning("Webhook: no order found for PI %s", pid)
            return HttpResponse("Webhook: no order found", status=200)

        if not order.is_paid:
            order.is_paid = True
            order.save(update_fields=["is_paid"])

        return HttpResponse("Webhook: order updated", status=200)

    def handle_payment_intent_payment_failed(self, event):
        """Handle the payment_intent.payment_failed webhook."""
        pid = event["data"]["object"]["id"]
        logger.warning("Payment failed for PI %s", pid)
        return HttpResponse(
            content=f"Webhook: payment failed for {pid}",
            status=200,
        )
