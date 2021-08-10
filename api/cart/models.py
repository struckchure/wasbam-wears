from django.db import models
import secrets

from accounts.models import User
from products.models import Product


class CartItem(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.OneToOneField(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField(default=1)
    slug = models.SlugField(max_length=60, blank=True, unique=True)
    date = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Cart item'
        verbose_name_plural = 'Cart items'

    def __str__(self):
        return self.product.name

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = secrets.token_urlsafe(60)
            slug_exits = CartItem.objects.filter(slug=slug).exists()

            if not slug_exits:
                self.slug = slug

        super(CartItem, self).save(*args, **kwargs)

    def get_unit_price(self):
        if not self.product:
            return None

        return self.product.price

    def get_total_price(self):
        if not self.product:
            return None

        return self.product.price * self.quantity
