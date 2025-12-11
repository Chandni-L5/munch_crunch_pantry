from django.shortcuts import render

from munch_crunch_pantry import settings
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


def shipping(request):
    context = {
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'standard_delivery': settings.STANDARD_DELIVERY,
    }
    return render(request, 'home/shipping.html', context)


def faq(request):
    return render(request, 'home/faq.html')


def returns(request):
    return render(request, 'home/returns.html')


def contact(request):
    return render(request, 'home/contact.html')
