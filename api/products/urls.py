from django.urls import path

from products.api import (
    ProductCreateAPI,
    ProductListAPI,
    ProductDetailsAPI,
    ProductUpdateAPI,
    ProductDeleteAPI
)

app_name = 'products'

urlpatterns = [
    path('products/create/', ProductCreateAPI.as_view(), name='create'),
    path('products/list/', ProductListAPI.as_view(), name='list'),
    path('products/<slug:slug>/details/', ProductDetailsAPI.as_view(), name='details'),
    path('products/<slug:slug>/update/', ProductUpdateAPI.as_view(), name='update'),
    path('products/<slug:slug>/delete/', ProductDeleteAPI.as_view(), name='delete')
]
