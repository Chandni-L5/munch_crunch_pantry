from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages
from products.models import ProductQuantity, Product


def view_basket(request):
    # Render the basket template
    return render(request, 'basket/basket.html')


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
