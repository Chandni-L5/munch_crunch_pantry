from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('shipping/', views.shipping, name='shipping'),
    path('faq/', views.faq, name='faq'),
    path('returns/', views.returns, name='returns'),
    path('contact/', views.contact, name='contact'),
]
