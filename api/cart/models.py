from django.db import models

from accounts.models import User
from products.models import Product


class Cart(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    items = models.ManyToManyField('CartItem')
    date = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super(Cart, self).save(*args, **kwargs)


class CartItem(models.Model):

    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    quantity = models.PositiveIntegerField(default=1)
    date = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Cart item'
        verbose_name_plural = 'Cart items'

    def __str__(self):
        return self.product.name

    def save(self, *args, **kwargs):
        super(CartItem, self).save(*args, **kwargs)
