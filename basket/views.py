from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import HttpResponse
from django.contrib import messages
from products.models import ProductQuantity, Product


def remove_from_basket(request, item_id):
    """Remove a ProductQuantity from the basket completely."""
    product_quantity = get_object_or_404(ProductQuantity, pk=item_id)
    basket = request.session.get('basket', {})
    item_key = str(item_id)

    if item_key in basket:
        basket.pop(item_key)
        messages.success(
            request,
            f"Removed {product_quantity.product.name} ({product_quantity.quantity.name}) from your basket."
        )

    request.session['basket'] = basket
    return HttpResponse(status=200)


def view_basket(request):
    # Render the basket template
    return render(request, 'basket/basket.html')


def adjust_basket(request, item_id):
    """Adjust the quantity of a specific item in the basket"""
    product_quantity = get_object_or_404(ProductQuantity, pk=item_id)

    try:
        quantity = int(request.POST.get('quantity'))
    except (TypeError, ValueError):
        messages.error(request, "Invalid quantity.")
        return redirect(reverse('view_basket'))

    basket = request.session.get('basket', {})
    item_key = str(item_id)

    if quantity > 0:
        basket[item_key] = quantity
        messages.success(
            request,
            f"Updated {product_quantity.product.name} ({product_quantity.quantity.name}) to {quantity}."
        )
    else:
        basket.pop(item_key, None)
        messages.success(
            request,
            f"Removed {product_quantity.product.name} ({product_quantity.quantity.name}) from your basket."
        )

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))


def add_to_basket(request, item_id):
    # Add a quantity of a product to the basket
    product = get_object_or_404(Product, pk=item_id)

    pq_id = request.POST.get('product_quantity_id')
    if not pq_id:
        messages.error(request, "Please select a size before adding this product to your basket.")
        return redirect(reverse('product_detail', args=[item_id]))

    product_quantity = get_object_or_404(ProductQuantity, pk=pq_id, product=product)
    quantity = int(request.POST.get('quantity', 1))
    redirect_url = request.POST.get('redirect_url', reverse('product_detail', args=[item_id]))
    basket = request.session.get('basket', {})
    if pq_id in basket:
        basket[pq_id] += quantity
        messages.success(
            request,
            f"Updated {product_quantity.product.name} ({product_quantity.quantity.name}) quantity to {basket[pq_id]}."
        )
    else:
        basket[pq_id] = quantity
        messages.success(
            request,
            f"Added {product_quantity.product.name} ({product_quantity.quantity.name}) to your basket."
        )

    request.session['basket'] = basket
    return redirect(redirect_url)
