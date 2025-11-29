from django.shortcuts import render


# Create your views here.
def view_basket(request):
    # Render the basket template
    return render(request, 'basket/basket.html')
