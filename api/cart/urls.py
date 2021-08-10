from django.urls import path

from cart.api import (
    CartAPI,
    CartItemAddAPI,
    CartItemUpdateAPI,
    CartItemDeleteAPI
)

app_name = 'cart'

urlpatterns = [
    path('cart/', CartAPI.as_view(), name='details'),
    path('cart/add-item/', CartItemAddAPI.as_view(), name='add'),
    path('cart/<slug:slug>/update/', CartItemUpdateAPI.as_view(), name='update'),
    path('cart/<slug:slug>/delete/', CartItemDeleteAPI.as_view(), name='delete'),
]
