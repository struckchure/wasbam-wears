from django.urls import path

from cart.api import (
    CartAPI,
    CartItemAddAPI,
    CartItemDetailAPI,
    CartItemUpdateAPI,
    CartItemDeleteAPI,
    CartItemFilterByProductAPI,
    CartCheckoutAPI
)

app_name = 'cart'

urlpatterns = [
    path('cart/', CartAPI.as_view(), name='details'),
    path('cart/add-item/', CartItemAddAPI.as_view(), name='add'),
    path('cart/<slug:cart_item_slug>/details/', CartItemDetailAPI.as_view(), name='details'),
    path('cart/<slug:slug>/update/', CartItemUpdateAPI.as_view(), name='update'),
    path('cart/<slug:slug>/delete/', CartItemDeleteAPI.as_view(), name='delete'),
    path('cart/<slug:product_slug>/filter/', CartItemFilterByProductAPI.as_view(), name='filter'),
    path('cart/check-out/', CartCheckoutAPI.as_view(), name='check-out')
]
