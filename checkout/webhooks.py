import stripe

from django.conf import settings
from django.http import HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .webhook_handler import StripeWH_Handler


@require_POST
@csrf_exempt
def webhook(request):
    """
    Listen for webhooks from Stripe.
    Verify the signature, then route the event
    to the appropriate handler method.
    """
    stripe.api_key = settings.STRIPE_SECRET_KEY
    wh_secret = settings.STRIPE_WEBHOOK_SECRET

    payload = request.body
    sig_header = request.META.get("HTTP_STRIPE_SIGNATURE")
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload=payload,
            sig_header=sig_header,
            secret=wh_secret,
        )
    except ValueError:
        return HttpResponseBadRequest("Invalid payload")
    except stripe.error.SignatureVerificationError:
        return HttpResponseBadRequest("Invalid signature")
    except Exception as e:
        return HttpResponseBadRequest(f"Webhook error: {e}")

    handler = StripeWH_Handler(request)
    event_map = {
        "payment_intent.succeeded": (
            handler.handle_payment_intent_succeeded
        ),
        "payment_intent.payment_failed": (
            handler.handle_payment_intent_payment_failed
        ),
    }
    event_type = event["type"]
    event_handler = event_map.get(event_type, handler.handle_event)
    response = event_handler(event)
    return response
