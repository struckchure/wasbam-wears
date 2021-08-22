from django.db import models

from wasbam_wears.utils import generate_slug
from accounts.models import User
from products.models import Product


class Transaction(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    status = models.BooleanField(default=False)
    slug = models.SlugField(max_length=60, blank=True, unique=True)
    date = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Transaction'
        verbose_name_plural = 'Transactions'

    def __str__(self):
        pass

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = generate_slug(60)
            slug_exits = Transaction.objects.filter(slug=slug).exists()

            if not slug_exits:
                self.slug = slug

        super(Transaction, self).save(*args, **kwargs)

    def pay_now(self):
        pass
