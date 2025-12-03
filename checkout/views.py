from django.contrib import messages
from django.shortcuts import redirect, render
from django.conf import settings
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

from .forms import OrderForm
from basket.context_processor import basket_contents

import json
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


def checkout(request):
    """ A view to return the checkout page """
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "Your basket is empty")
        return redirect('products')

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
    }
    return render(request, template, context)


@require_POST
@csrf_exempt
def create_payment_intent(request):
    """
    AJAX call to create the PaymentIntent
    - Calculate order amount on server
    - Create PaymentIntent
    - Return clientSecret as JSON
    """
    try:
        basket = basket_contents(request)
        grand_total = basket["grand_total"]
        amount = int(round(grand_total * 100))
        if amount <= 0:
            return HttpResponseBadRequest("Invalid amount.")
        intent = stripe.PaymentIntent.create(
            amount=amount,
            currency="gbp",
            payment_method_types=["card"],
        )

        return JsonResponse({"clientSecret": intent.client_secret})

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)


@csrf_exempt
def stripe_webhook(request):
    """Listen for Stripe events."""
    if request.method != "POST":
        return HttpResponse(status=200)

    payload = request.body
    sig_header = request.META.get("HTTP_STRIPE_SIGNATURE")
    endpoint_secret = settings.STRIPE_WEBHOOK_SECRET

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError:
        # Invalid signature
        return HttpResponse(status=400)

    if event["type"] == "payment_intent.succeeded":
        payment_intent = event["data"]["object"]
        print("💳 Payment succeeded:", payment_intent["id"])
        # TODO: create Order here

    return HttpResponse(status=200)


def checkout_success(request):
    """ A view to handle successful checkouts """
    return render(request, "checkout/checkout_success.html")
