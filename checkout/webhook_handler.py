from django.http import HttpResponse


class StripeWH_Handler:
    """
    Handle Stripe webhooks.
    """
    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handles unexpected webhook events
        """
        return HttpResponse(
            content=f"Unhandled webhook received: {event['type']}",
            status=200,
        )

    def handle_payment_intent_succeeded(self, event):
        """
        Handles payment intent succeeded webhooks from Stripe
        """
        return HttpResponse(
            content="Webhook received: payment_intent.succeeded",
            status=200,
        )

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe.
        """
        return HttpResponse(
            content="Webhook received: payment_intent.payment_failed",
            status=200,
        )
