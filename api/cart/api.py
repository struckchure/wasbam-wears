from rest_framework.generics import GenericAPIView as View
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from accounts.models import User
from cart.serializers import CartSerializer
from cart.models import Cart


class CartAPI(View):

    permission_classes = [
        IsAuthenticated
    ]
    serializer_class = CartSerializer

    def get(self, request):
        user = User.objects.get(
            username=request.user.username
        )
        cart, created = Cart.objects.get_or_create(
            user=user
        )

        if not created:
            cart.save()

        cart_serializer = self.get_serializer(cart)

        response = Response(
            cart_serializer.data
        )

        return response


class CartUpdateAPI(View):

    permission_classes = [
        IsAuthenticated
    ]
    serializer_class = CartSerializer

    def post(self, request):
        cart_data = request.data
        user = User.objects.get(
            username=request.user.username
        )
        cart, created = Cart.objects.get_or_create(
            user=user
        )

        if not created:
            cart.save()

        cart_serializer = self.get_serializer(
            cart,
            data=cart_data,
            partial=True
        )
        cart_serializer.is_valid(raise_exception=True)
        cart_serializer.save()

        response = Response(
            cart_serializer.data
        )

        return response
