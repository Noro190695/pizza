from django.urls import path
from .views import *

urlpatterns = [
    path('', get),
    path('add/<int:product_id>/', add),
    path('remove/<int:product_id>/<int:product_size>/', remove),
    path('clean/', clean)
]
