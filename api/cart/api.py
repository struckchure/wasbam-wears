from rest_framework.generics import GenericAPIView as View
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.shortcuts import get_object_or_404, redirect
from django.db.models import Sum

from accounts.models import User
from cart.serializers import CartItemUpdateSerializer, CartItemSerializer
from cart.models import CartItem
from records.models import Transaction


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
        total_price = cart_items.aggregate(total_price=Sum('product__price'))
        cart_items_serializer = self.get_serializer(cart_items, many=True)

        response = Response(
            {
                'items': cart_items_serializer.data,
                'total_price': total_price['total_price']
            }
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
        product_slug = request.data.get('product')
        cart_item = CartItem.objects.filter(
            user=user,
            product__slug=product_slug
        )

        if cart_item.exists():
            cart_item.delete()
            response = Response(
                {
                    "message": [
                        'Cart item removed'
                    ],
                    "removed": True
                }
            )
        else:
            cart_item_serializer = self.get_serializer(data=cart_item_data)
            cart_item_serializer.is_valid(raise_exception=True)
            cart_item_serializer.save(user=user)

            response = Response(
                cart_item_serializer.data
            )

        return response


class CartItemDetailAPI(View):

    permission_classes = [
        IsAuthenticated
    ]
    serializer_class = CartItemSerializer

    def get(self, request, cart_item_slug):
        user = request.user
        cart_item = get_object_or_404(
            CartItem,
            user=user,
            slug=cart_item_slug
        )
        cart_item_serializer = self.get_serializer(cart_item)

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


class CartItemFilterByProductAPI(View):

    permission_classes = [
        IsAuthenticated
    ]
    serializer_class = CartItemSerializer

    def get(self, request, product_slug):
        user = request.user
        cart_item = CartItem.objects.filter(
            user=user,
            product__slug=product_slug
        )
        if not cart_item.exists():
            return Response(
                {
                    'cart_item_exists': False
                }
            )

        cart_item_serializer = self.get_serializer(cart_item[0])

        response = Response(
            cart_item_serializer.data
        )

        return response


class CartCheckoutAPI(View):

    permission_classes = [
        IsAuthenticated
    ]

    def get(self, request):
        user = request.user
        cart_items = CartItem.objects.filter(
            user=user
        )
        self.check_out(user, cart_items)

        response = Response(
            {
                'success': [
                    'Checkout successful'
                ]
            }
        )
        return response

    def check_out(self, user, items):
        for item in items:
            self.check_out_item(user, item)
            item.delete()

    def check_out_item(self, user, item):
        item_record = Transaction.objects.create(
            user=user,
            product=item.product,
            quantity=item.quantity
        )
        item_record.save()
