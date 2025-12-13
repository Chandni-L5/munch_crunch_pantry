from decimal import Decimal, ROUND_HALF_UP

from django.conf import settings
from django.shortcuts import get_object_or_404

from products.models import ProductQuantity
from .utils import get_discount_amount


def basket_contents(request):
    basket_items = []
    total = Decimal("0.00")
    discount_amount = Decimal("0.00")
    discount_details = get_discount_amount(request)
    product_count = 0
    basket = request.session.get("basket", {})

    for item_id, quantity in basket.items():
        product = get_object_or_404(ProductQuantity, pk=item_id)
        price = product.price
        line_total = price * quantity
        total += line_total
        product_count += quantity
        basket_items.append({
            "item_id": item_id,
            "quantity": quantity,
            "product": product,
            "total_price": line_total,
        })

    if product_count == 0:
        delivery = Decimal("0.00")
        free_delivery_delta = Decimal(str(settings.FREE_DELIVERY_THRESHOLD))
    else:
        free_threshold = Decimal(str(settings.FREE_DELIVERY_THRESHOLD))
        standard_delivery = Decimal(str(settings.STANDARD_DELIVERY))

        subtotal_after_discount = total

        if discount_details['valid']:
            discount_amount = (
                total * (discount_details['percentage'] / Decimal("100"))
            ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
            subtotal_after_discount -= discount_amount

        if subtotal_after_discount < 0:
            subtotal_after_discount = Decimal("0.00")

        if subtotal_after_discount < free_threshold:
            delivery = standard_delivery
            free_delivery_delta = free_threshold - subtotal_after_discount
        else:
            delivery = Decimal("0.00")
            free_delivery_delta = Decimal("0.00")

    grand_total = total + delivery
    discounted_total = total - discount_amount
    if discounted_total < 0:
        discounted_total = Decimal("0.00")
    grand_total = discounted_total + delivery

    return {
        "basket_items": basket_items,
        "total": total,
        "discount_amount": discount_amount,
        "discount_details": discount_details,
        "discount_code": (
            discount_details["code"]
            if discount_details["valid"]
            else None
        ),
        "discount_percentage": (
            discount_details["percentage"]
            if discount_details["valid"]
            else Decimal("0.00")
        ),
        "discounted_total": discounted_total,
        "product_count": product_count,
        "delivery": delivery,
        "free_delivery_delta": free_delivery_delta,
        "free_delivery_threshold": Decimal(
            str(settings.FREE_DELIVERY_THRESHOLD)
        ),
        "grand_total": grand_total,
    }
