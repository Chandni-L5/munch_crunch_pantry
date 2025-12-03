from django.urls import path
from . import views

urlpatterns = [
    path('create-payment-intent/', views.create_payment_intent, name='create_payment_intent'),
    path('', views.checkout, name='checkout'),
    path('success/', views.checkout_success, name='checkout_success'),
]
