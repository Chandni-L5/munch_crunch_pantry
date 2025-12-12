from decimal import Decimal

from django.conf import settings
from django.shortcuts import get_object_or_404

from products.models import ProductQuantity


def basket_contents(request):
    """
    A context processor to add the shopping basket contents to the context.
    """
    basket_items = []
    total = Decimal('0.00')
    product_count = 0
    basket = request.session.get('basket', {})

    for item_id, quantity in basket.items():
        product = get_object_or_404(ProductQuantity, pk=item_id)
        price = product.price
        line_total = price * quantity
        total += line_total
        product_count += quantity
        basket_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
            'total_price': line_total
        })

    free_delivery_threshold = Decimal(str(settings.FREE_DELIVERY_THRESHOLD))
    standard_delivery = Decimal(str(settings.STANDARD_DELIVERY))

    if product_count == 0:
        delivery = Decimal('0.00')
        free_delivery_delta = Decimal('0.00')
    elif total < free_delivery_threshold:
        delivery = standard_delivery
        free_delivery_delta = free_delivery_threshold - total
    else:
        delivery = Decimal('0.00')
        free_delivery_delta = Decimal('0.00')

    grand_total = total + delivery

    return {
        "basket_items": basket_items,
        "total": total,
        "product_count": product_count,
        "delivery": delivery,
        "free_delivery_delta": free_delivery_delta,
        "free_delivery_threshold": free_delivery_threshold,
        "grand_total": grand_total,
    }
