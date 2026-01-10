from decimal import Decimal

from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from django.conf import settings
from django.http import JsonResponse, HttpResponseBadRequest
from django.urls import reverse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError, transaction
from django.views.decorators.cache import never_cache

from profiles.forms import UserProfileForm
from profiles.models import UserProfile
from products.models import ProductQuantity
from basket.context_processor import basket_contents
from basket.utils import get_discount_amount

from .forms import OrderForm
from .models import Order, OrderLineItem, DiscountSingleUse
from .utils import send_confirmation_email

import json
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


@never_cache
def checkout_success_pid(request):
    """
    Redirect to checkout_success with order_number from session
    Used when order_number is not known at the time of redirect
    """
    pid = request.GET.get("pid")
    if not pid:
        messages.error(request, "Missing payment intent ID.")
        return redirect("contact")

    order = Order.objects.filter(stripe_pid=pid).first()
    if order:
        request.session.pop("pending_pid", None)
        request.session.pop("save_info", None)
        request.session.pop("basket", None)
        request.session.pop("discount_amount", None)
        return redirect(
            "checkout_success", order_number=order.order_number
        )
    try:
        intent = stripe.PaymentIntent.retrieve(pid)
    except Exception:
        messages.error(
            request,
            "We couldn't verify your payment. Please try again."
        )
        return redirect("checkout")

    if intent.status in ('processing', 'requires_capture'):
        return render(
            request,
            "checkout/payment_processing.html",
            {"pid": pid}
        )

    if intent.status == 'succeeded':
        return render(
            request,
            "checkout/payment_processing.html",
            {"pid": pid, "succeeded_no_order": True}
        )
    messages.error(
        request,
        "Your payment was not successful. Please try again."
    )
    return redirect("checkout")


@never_cache
def checkout(request):
    """
    Handle the checkout process
    - Display order form
    - Process order on POST
    - Create Order and OrderLineItems
    - Redirect to success page
    """
    pending_pid = request.session.get("pending_pid")
    if pending_pid and request.method == "GET":
        return redirect(f"{reverse('checkout_success_pid')}?pid={pending_pid}")

    basket = request.session.get("basket", {})
    if not basket:
        messages.error(request, "Your basket is empty.")
        return redirect("products")

    if request.method == "POST":
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
            basket_data = basket_contents(request)

            client_secret = request.POST.get("client_secret")
            pid = None
            if client_secret:
                pid = client_secret.split("_secret")[0]

            order = order_form.save(commit=False)
            order.stripe_pid = pid
            order.original_basket = json.dumps(basket)
            order.discount_code = None
            order.discount_amount = Decimal("0.00")
            discount_details = get_discount_amount(request)

            order.save()

            if discount_details["valid"]:
                code = discount_details["code"]
                email = order.email.strip().lower()

                try:
                    with transaction.atomic():
                        DiscountSingleUse.objects.create(
                            code=code,
                            email=email,
                            order_number=order.order_number,
                        )

                        order.discount_code = code
                        order.discount_amount = basket_data.get(
                            "discount_amount", Decimal("0.00")
                        )
                        order.save()

                except IntegrityError:
                    request.session.pop("discount_amount", None)
                    messages.error(
                        request,
                        "This discount code has already been used with "
                        "this email address."
                    )
                    order.delete()
                    return redirect("view_basket")

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
                    return redirect("view_basket")

            order.update_total()

            request.session["save_info"] = "save_info" in request.POST
            if not pid:
                messages.error(
                    request,
                    "Payment reference missing. Please try again."
                )
                order.delete()
                return redirect("checkout")

            try:
                intent = stripe.PaymentIntent.retrieve(pid)
            except Exception:
                messages.error(
                    request,
                    "We couldn't verify your payment. Please try again."
                )
                order.delete()
                return redirect("checkout")

            if intent.status != "succeeded":
                messages.error(
                    request,
                    "Payment not completed. Please try again."
                )
                order.delete()
                return redirect("checkout")

            return redirect(
                "checkout_success", order_number=order.order_number
            )

        messages.error(
            request,
            "There was an error with your form. "
            "Please double-check your information."
        )

    else:
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(
                    initial={
                        "full_name": profile.user.get_full_name()
                        or profile.user.username,
                        "email": profile.user.email,
                        "phone_number": profile.default_phone_number,
                        "street_address1": profile.default_street_address1,
                        "street_address2": profile.default_street_address2,
                        "town_or_city": profile.default_town_or_city,
                        "postcode": profile.default_postcode,
                        "country": profile.default_country,
                    }
                )
            except UserProfile.DoesNotExist:
                order_form = OrderForm(
                    initial={
                        "full_name": request.user.get_full_name()
                        or request.user.username,
                        "email": request.user.email,
                    }
                )
        else:
            order_form = OrderForm()

    context = {
        "order_form": order_form,
        "basket": basket,
        "stripe_public_key": settings.STRIPE_PUBLIC_KEY,
        "geoapify_api_key": settings.GEOAPIFY_API_KEY,
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


@never_cache
def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    order = get_object_or_404(Order, order_number=order_number)
    request.session.pop("pending_pid", None)
    from_email = request.GET.get("from_email") == "1"
    save_info = request.session.get("save_info", False)

    if (
        not from_email
        and order.stripe_pid
        and not order.confirmation_email_sent
    ):
        payment_intent = stripe.PaymentIntent.retrieve(order.stripe_pid)
        if payment_intent["status"] == "succeeded":
            send_confirmation_email(order, request)
            order.confirmation_email_sent = True
            order.is_paid = True
            order.save(update_fields=["confirmation_email_sent", "is_paid"])

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        order.user_profile = profile
        order.save()

        if save_info:
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
            else:
                messages.error(
                    request,
                    "There was an error updating your profile. "
                    "Please check the form."
                )

    request.session.pop("save_info", None)
    request.session.pop("basket", None)
    request.session.pop("discount_amount", None)

    if not from_email:
        messages.success(
            request,
            f"Order successfully processed! "
            f"Your order number is {order.order_number}. "
            "A confirmation email will be sent to "
            f"{order.email}.",
        )

    template = "checkout/checkout_success.html"
    context = {
        "order": order,
        "from_profile": False,
        "from_email": from_email,
    }
    return render(request, template, context)


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
        request.session["pending_pid"] = pid
        request.session.modified = True
        save_info = data.get("save_info", False)
        basket = request.session.get("basket", {})

        stripe.PaymentIntent.modify(
            pid,
            metadata={
                "basket": json.dumps(basket),
                "save_info": str(save_info).lower(),
                "username": (
                    request.user.username
                    if request.user.is_authenticated
                    else "AnonymousUser"
                ),
            },
        )

        return JsonResponse({"success": True})

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)
