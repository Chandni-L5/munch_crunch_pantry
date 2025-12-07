from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from django.conf import settings
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

from profiles.forms import UserProfileForm
from profiles.models import UserProfile
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
            client_secret = request.POST.get("client_secret")
            pid = None
            if client_secret:
                pid = client_secret.split("_secret")[0]
            order = order_form.save(commit=False)
            order.stripe_pid = pid
            order.original_basket = json.dumps(basket)
            order.save()
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
            request.session['save_info'] = 'save_info' in request.POST
            return redirect('checkout_success', order_number=order.order_number)
        else:
            print("Order form invalid", order_form.errors)  # DEBUG: watch runserver output
            messages.error(
                request,
                "There was an error with your form. Please double-check your information."
            )
    else:
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': profile.user.get_full_name() or profile.user.username,
                    'email': profile.user.email,
                    'phone_number': profile.default_phone_number,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                    'town_or_city': profile.default_town_or_city,
                    'postcode': profile.default_postcode,
                    'country': profile.default_country,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

    context = {
        'order_form': order_form,
        'basket': basket,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
        'geoapify_api_key': settings.GEOAPIFY_API_KEY,
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


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get("save_info")
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        order.user_profile = profile
        order.save()

        if save_info:
            print("ORDER DATA:", {
                "phone_number": order.phone_number,
                "street_address1": order.street_address1,
                "street_address2": order.street_address2,
                "town_or_city": order.town_or_city,
                "postcode": order.postcode,
                "country": order.country,
            })

            profile_data = {
                "default_phone_number": order.phone_number,
                "default_street_address1": order.street_address1,
                "default_street_address2": order.street_address2,
                "default_town_or_city": order.town_or_city,
                "default_postcode": order.postcode,
                "default_country": order.country,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()
                print("Profile updated successfully")  # DEBUG
            else:
                print("UserProfileForm invalid:", user_profile_form.errors)  # DEBUG

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
