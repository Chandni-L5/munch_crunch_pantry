from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from django.conf import settings
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

from .forms import OrderForm
from products.models import ProductQuantity
from .models import Order, OrderLineItem
from basket.context_processor import basket_contents

import json
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


def checkout(request):
    """
    Handle the checkout process
    - Display order form
    - Process order on POST
    - Create Order and OrderLineItems
    - Redirect to success page
    """
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "Your basket is empty.")
        return redirect('products')

    if request.method == 'POST':
        form_data = {
            "full_name": request.POST.get("full_name"),
            "email": request.POST.get("email"),
            "phone_number": request.POST.get("phone_number"),
            "street_address1": request.POST.get("street_address1"),
            "street_address2": request.POST.get("street_address2"),
            "town_or_city": request.POST.get("town_or_city"),
            "postcode": request.POST.get("postcode"),
            "country": request.POST.get("country"),
        }

        order_form = OrderForm(form_data)

        if order_form.is_valid():
            order = order_form.save()
            print("ORDER CREATED:", order.order_number)  # DEBUG: watch runserver output
            for item_id, quantity in basket.items():
                try:
                    product_quantity = ProductQuantity.objects.get(pk=item_id)
                    OrderLineItem.objects.create(
                        order=order,
                        product_quantity=product_quantity,
                        quantity=quantity,
                    )
                except ProductQuantity.DoesNotExist:
                    messages.error(
                        request,
                        "One of the products in your basket was not found. "
                        "Please contact us for assistance."
                    )
                    order.delete()
                    return redirect('view_basket')
            order.update_total()
            request.session['save_info'] = 'save-info' in request.POST
            return redirect('checkout_success', order_number=order.order_number)
        else:
            messages.error(
                request,
                "There was an error with your form. Please double-check your information."
            )
    else:
        order_form = OrderForm()

    context = {
        'order_form': order_form,
        'basket': basket,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
    }
    return render(request, "checkout/checkout.html", context)


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


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get("save_info")
    order = get_object_or_404(Order, order_number=order_number)

    messages.success(
        request,
        f"Order successfully processed! "
        f"Your order number is {order.order_number}. "
        "A confirmation email will be sent to "
        f"{order.email}.",
    )

    if "basket" in request.session:
        del request.session["basket"]

    context = {
        "order": order,
    }

    return render(request, "checkout/checkout_success.html", context)
