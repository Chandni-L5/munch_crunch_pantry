from django.urls import path
from . import views, webhooks

urlpatterns = [
    path('create-payment-intent/', views.create_payment_intent, name='create_payment_intent'),
    path('', views.checkout, name='checkout'),
    path('success/<order_number>/', views.checkout_success, name='checkout_success'),
    path('cache_checkout_data/', views.cache_checkout_data, name='cache_checkout_data'),
    path('wh/', webhooks.webhook, name='webhook'),
]
