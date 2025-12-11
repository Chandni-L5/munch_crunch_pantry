from django.conf import settings
from products.models import ProductQuantity
from django.shortcuts import get_object_or_404


def basket_contents(request):
    """
    A context processor to add the shopping basket contents to the context.
    """
    basket_items = []
    total = 0.00
    product_count = 0
    basket = request.session.get('basket', {})

    for item_id, quantity in basket.items():
        product = get_object_or_404(ProductQuantity, pk=item_id)
        price = float(product.price)
        line_total = price * quantity
        total += line_total
        product_count += quantity
        basket_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
            'total_price': line_total
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = float(settings.STANDARD_DELIVERY)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0.00
        free_delivery_delta = 0.00
    grand_total = total + delivery

    context = {
        'basket_items': basket_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
