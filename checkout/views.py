from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import OrderForm


def checkout(request):
    """ A view to return the checkout page """
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "Your basket is empty")
        return redirect('products')

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {'order_form': order_form, }
    return render(request, template, context)
