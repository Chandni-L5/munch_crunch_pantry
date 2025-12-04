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
import time

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
            print("Order form invalid", order_form.errors)  # DEBUG: watch runserver output
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
    """
    Listen for Stripe events.

    On payment_intent.succeeded:
    - find an order that was already created by the checkout view.
    - if it doesn't exist, create it using the PaymentIntent data and metadata.
    """
    if request.method != "POST":
        return HttpResponse(status=200)

    payload = request.body
    sig_header = request.META.get("HTTP_STRIPE_SIGNATURE")
    endpoint_secret = settings.STRIPE_WEBHOOK_SECRET

    try:
        event = stripe.Webhook.construct_event(payload, sig_header, endpoint_secret)
    except ValueError:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError:
        # Invalid signature
        return HttpResponse(status=400)
    if event["type"] == "payment_intent.succeeded":
        intent = event["data"]["object"]
        pid = intent["id"]

        # Metadata you added in cache_checkout_data
        metadata = intent.get("metadata", {})
        basket_str = metadata.get("basket")          # e.g. '{"5": 1}'
        save_info = metadata.get("save_info")        # "true" / "false"
        username = metadata.get("username")          # e.g. "admin"

        try:
            stripe_charge = stripe.Charge.retrieve(intent["latest_charge"])
            billing_details = stripe_charge["billing_details"]
        except (KeyError, IndexError, TypeError):
            billing_details = {
                "email": None,
                "name": None,
                "phone": None,
                "address": {
                    "line1": None,
                    "line2": None,
                    "city": None,
                    "postal_code": None,
                    "country": None,
                    "state": None,
                },
            }

        shipping_details = intent.get("shipping", {}) or {}
        shipping_address = shipping_details.get("address", {}) or {}
        grand_total = round(stripe_charge["amount"] / 100, 2)

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


@require_POST
@csrf_exempt
def cache_checkout_data(request):
    """
    Add metadata to the PaymentIntent so the webhook handler
    can reconstruct the order (basket, save_info, username).
    """
    try:
        data = json.loads(request.body.decode("utf-8"))
        client_secret = data.get("client_secret")

        if not client_secret:
            return JsonResponse({"error": "Missing client_secret"}, status=400)

        pid = client_secret.split("_secret")[0]
        save_info = data.get("save_info", False)
        basket = request.session.get("basket", {})

        stripe.PaymentIntent.modify(
            pid,
            metadata={
                "basket": json.dumps(basket),
                "save_info": json.dumps(save_info),
                "username": (
                    request.user.username if request.user.is_authenticated else "anonymous"
                ),
            },
        )

        return JsonResponse({"success": True})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)
