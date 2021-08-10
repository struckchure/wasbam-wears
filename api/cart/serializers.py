from rest_framework import serializers
from django.forms.models import model_to_dict

from cart.models import CartItem
from products.models import Product
from products.serializers import ProductSerializer


class CartItemSerializer(serializers.ModelSerializer):

    product = ProductSerializer()
    quantity = serializers.SerializerMethodField()
    price = serializers.SerializerMethodField()
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = [
            'product',
            'quantity',
            'price',
            'total_price',
            'slug'
        ]

    def get_product(self, obj):
        return model_to_dict(Product(pk=obj.pk))

    def get_quantity(self, obj):
        if not obj.product:
            return None
        return obj.quantity

    def get_price(self, obj):
        return obj.get_unit_price()

    def get_total_price(self, obj):
        return obj.get_total_price()


class CartItemUpdateSerializer(serializers.ModelSerializer):

    product = serializers.SlugField()

    class Meta:
        model = CartItem
        fields = [
            'product',
            'quantity',
            'slug'
        ]
        read_only_fields = ['slug']

    def validate_product(self, value):
        product = Product.objects.get(slug=value)
        item_exists = CartItem.objects.filter(product=product).exists()

        if item_exists:
            raise serializers.ValidationError(
                "Product already exist in your cart"
            )

        return product
