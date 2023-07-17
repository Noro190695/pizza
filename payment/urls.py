from django.urls import path
from .views import *

urlpatterns = [
    path('', pay, name='pay'),
    path('checkout/', Checkout.as_view(), name='checkout')
]
