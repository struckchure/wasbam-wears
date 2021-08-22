from rest_framework import serializers

from products.models import Product
from products.serializers import ProductSerializer
from records.models import Transaction


class TransactionSerializer(serializers.ModelSerializer):

    product = ProductSerializer()

    class Meta:
        model = Transaction
        fields = [
            'product',
            'quantity',
            'status',
            'slug'
        ]


class TransactionCreateSerializer(serializers.ModelSerializer):

    product = serializers.SlugField()

    class Meta:
        model = Transaction
        fields = [
            'product',
            'status',
            'quantity',
            'slug'
        ]
        read_only_fields = [
            'slug'
        ]

    def validate_product(self, value):
        product = Product.objects.filter(slug=value)
        product_exists = product.exists()

        if not product_exists:
            raise serializers.ValidationError("PRODUCT_DOES_NOT_EXISTS")

        return product[0]
