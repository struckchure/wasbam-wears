from rest_framework.generics import GenericAPIView as View
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.shortcuts import get_object_or_404, redirect

from accounts.models import User
from cart.serializers import CartItemUpdateSerializer, CartItemSerializer
from cart.models import CartItem


class CartAPI(View):

    permission_classes = [
        IsAuthenticated
    ]
    serializer_class = CartItemSerializer

    def get(self, request):
        user = User.objects.get(
            username=request.user.username
        )
        cart_items = CartItem.objects.filter(user=user).order_by('-updated')
        cart_items_serializer = self.get_serializer(cart_items, many=True)

        response = Response(
            cart_items_serializer.data
        )

        return response


class CartItemAddAPI(View):

    permission_classes = [
        IsAuthenticated
    ]
    serializer_class = CartItemUpdateSerializer

    def post(self, request):
        user = User.objects.get(
            username=request.user.username
        )
        cart_item_data = request.data

        cart_item_serializer = self.get_serializer(data=cart_item_data)
        cart_item_serializer.is_valid(raise_exception=True)
        cart_item_serializer.save(user=user)

        response = Response(
            cart_item_serializer.data
        )

        return response


class CartItemUpdateAPI(View):

    permission_classes = [
        IsAuthenticated
    ]
    serializer_class = CartItemUpdateSerializer

    def post(self, request, slug):
        user = request.user
        cart_item_data = request.data
        cart_item = get_object_or_404(CartItem, slug=slug)

        if cart_item.user != user:
            return Response(
                {
                    'error': [
                        'You do not have permission to perform this operation'
                    ]
                },
                status=status.HTTP_401_UNAUTHORIZED
            )

        cart_item_serializer = self.get_serializer(
            cart_item,
            data=cart_item_data,
            partial=True
        )
        cart_item_serializer.is_valid(raise_exception=True)
        cart_item_serializer.save()

        response = Response(
            cart_item_serializer.data
        )

        return response


class CartItemDeleteAPI(View):

    permission_classes = [
        IsAuthenticated
    ]

    def get(self, request, slug):
        user = request.user
        cart_item = get_object_or_404(CartItem, slug=slug)

        if cart_item.user != user:
            return Response(
                {
                    'error': [
                        'You do not have permission to perform this operation'
                    ]
                },
                status=status.HTTP_401_UNAUTHORIZED
            )

        cart_item.delete()

        return redirect('cart:details')
