from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotAllowed
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.urls import reverse

from checkout.models import DiscountSingleUse
from products.models import ProductQuantity, Product
from .utils import get_discount_amount


def remove_from_basket(request, item_id):
    """Remove a ProductQuantity from the basket completely."""
    try:
        if request.method != "POST":
            return HttpResponseNotAllowed(["POST"])

        product_quantity = get_object_or_404(ProductQuantity, pk=item_id)
        basket = request.session.get("basket", {})
        item_key = str(item_id)

        if item_key in basket:
            basket.pop(item_key)
            messages.success(
                request,
                f"Removed {product_quantity.product.name} "
                f"({product_quantity.quantity.name}) from your basket. ✅",
            )

        request.session["basket"] = basket
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f"Error removing item: {e}")
        return HttpResponse(status=500)


def view_basket(request):
    return render(request, "basket/basket.html")


def adjust_basket(request, item_id):
    """Adjust the quantity of a specific item in the basket"""
    product_quantity = get_object_or_404(ProductQuantity, pk=item_id)

    try:
        quantity = int(request.POST.get("quantity"))
    except (TypeError, ValueError):
        messages.error(request, "Invalid quantity.")
        return redirect(reverse("view_basket"))

    basket = request.session.get("basket", {})
    item_key = str(item_id)

    if quantity > 0:
        basket[item_key] = quantity
        messages.success(
            request,
            f"Updated {product_quantity.product.name} "
            f"({product_quantity.quantity.name}) to {quantity}. ✅",
        )
    else:
        basket.pop(item_key, None)
        messages.success(
            request,
            f"Removed {product_quantity.product.name} "
            f"({product_quantity.quantity.name}) from your basket. ✅",
        )

    request.session["basket"] = basket
    return redirect(reverse("view_basket"))


def add_to_basket(request, item_id):
    """Add a quantity of a ProductQuantity to the basket."""
    product = get_object_or_404(Product, pk=item_id)

    pq_id = request.POST.get("product_quantity_id")
    if not pq_id:
        messages.error(
            request,
            "Please select a size before adding this product to your basket."
        )
        return redirect(reverse("product_detail", args=[item_id]))

    product_quantity = get_object_or_404(
        ProductQuantity, pk=pq_id, product=product
    )
    quantity = int(request.POST.get("quantity", 1))
    redirect_url = request.POST.get(
        "redirect_url", reverse("product_detail", args=[item_id])
    )

    basket = request.session.get("basket", {})

    if pq_id in basket:
        basket[pq_id] += quantity
        messages.success(
            request,
            f"Updated: {product_quantity.product.name} "
            f"({product_quantity.quantity.name}) "
            f"is now set to {basket[pq_id]} in your basket. ✅",
        )
    else:
        basket[pq_id] = quantity
        messages.success(
            request,
            f"Added: {product_quantity.product.name} "
            f"({product_quantity.quantity.name}) added to your basket. ✅",
        )

    request.session["basket"] = basket
    return redirect(redirect_url)


@require_POST
def apply_discount(request):
    """
    Validate and apply a discount code to the basket.
    Empty or invalid code clears any existing discount.
    Check if code has been used previously by the user in checkout logic
    """
    code = (request.POST.get("discount_code") or "").strip().upper()

    if not code:
        request.session.pop("discount_amount", None)
        messages.info(request, "Please enter a discount code.")
        return redirect(reverse("view_basket"))

    request.session["discount_amount"] = {"code": code}
    discount = get_discount_amount(request)

    if not discount["valid"]:
        request.session.pop("discount_amount", None)
        messages.error(request, "Sorry, that discount code is not valid.")
        return redirect(reverse("view_basket"))

    if request.user.is_authenticated and request.user.email:
        email = request.user.email.strip().lower()

        if DiscountSingleUse.objects.filter(code=code, email=email).exists():
            request.session.pop("discount_amount", None)
            messages.error(
                request,
                "You have already used this discount code."
            )
            return redirect(reverse("view_basket"))
        else:
            messages.info(
                request,
                "Discount applied. We'll confirm eligibility at checkout."
            )

    messages.success(
        request,
        f"Discount applied: {discount['percentage']}% off."
    )
    return redirect(reverse("view_basket"))
