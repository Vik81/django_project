from django.urls import path

from .views import (
    product_detail, product_list
)

urlpatterns = [
    path('detail/', product_detail),
    path('', product_list),
]