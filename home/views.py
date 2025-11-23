from django.shortcuts import render


# Create your views here.
def index(request):
    # Render the home page template
    return render(request, 'home/index.html')