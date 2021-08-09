from django.urls import path

from cart.api import (
	CartAPI
)

app_name = 'cart'

urlpatterns = [
	path('cart/', CartAPI.as_view(), name='details')
]
