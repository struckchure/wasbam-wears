from rest_framework import serializers

from accounts.serializers import UserSerializer
from products.serializers import ProductSerializer
from cart.models import Cart, CartItem


class CartItemSerializer(serializers.ModelSerializer):

    product = ProductSerializer()

    class Meta:
        model = CartItem
        fields = [
            'product',
            'quantity'
        ]


class CartSerializer(serializers.ModelSerializer):

    user = UserSerializer()
    items = CartItemSerializer(many=True)

    class Meta:
        model = Cart
        fields = [
            'user',
            'items'
        ]
