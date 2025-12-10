from django.shortcuts import render

from products.models import Product

import random


def index(request):
    products = list(Product.objects.all())
    random.shuffle(products)
    random_products = products[:6]
    new_arrivals = Product.objects.order_by('-created_at')[:6]

    context = {
        'products': random_products,
        'new_arrivals': new_arrivals,
    }

    return render(request, 'home/index.html', context)
