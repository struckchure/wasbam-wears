from rest_framework.generics import GenericAPIView as View
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404, redirect
from django.forms.models import model_to_dict

from accounts.permissions import IsAdmin
from products.models import Product
from products.serializers import ProductSerializer


class ProductCreateAPI(View):

    serializer_class = ProductSerializer
    permission_classes = [
        IsAuthenticated,
        IsAdmin
    ]

    def post(self, request):
        product_data = request.data
        product_serializer = self.get_serializer(data=product_data)
        product_serializer.is_valid(raise_exception=True)
        product_serializer.save()

        response = Response(
            product_serializer.data
        )

        return response


class ProductListAPI(View):

    serializer_class = ProductSerializer

    def get(self, request):
        products = Product.objects.order_by('-updated')
        products_serializer = self.get_serializer(products, many=True)

        response = Response(
            products_serializer.data
        )

        return response


class ProductDetailsAPI(View):

    serializer_class = ProductSerializer

    def get(self, request, slug):
        product = get_object_or_404(Product, slug=slug)
        product_serializer = self.get_serializer(product)

        response = Response(
            product_serializer.data
        )

        return response


class ProductUpdateAPI(View):

    serializer_class = ProductSerializer
    permission_classes = [
        IsAuthenticated,
        IsAdmin
    ]

    def post(self, request, slug):
        product_data = request.data
        product = get_object_or_404(Product, slug=slug)
        product_serializer = self.get_serializer(
            product,
            data=product_data,
            partial=True
        )
        product_serializer.is_valid(raise_exception=True)
        product_serializer.save()

        response = Response(
            product_serializer.data
        )

        return response


class ProductDeleteAPI(View):

    permission_classes = [
        IsAuthenticated,
        IsAdmin
    ]

    def get(self, request, slug):
        product = get_object_or_404(Product, slug=slug)
        product.delete()

        return redirect('products:list')
