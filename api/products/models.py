from django.db import models
import secrets

from products.handlers import product_image_handler


class Product(models.Model):

    name = models.CharField(max_length=255, blank=False)
    image = models.ImageField(upload_to=product_image_handler)
    description = models.TextField(blank=True)
    amount = models.PositiveIntegerField(default=0)
    slug = models.SlugField(max_length=60, blank=True, unique=True)
    date = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = secrets.token_urlsafe(60)
            while slug not in Product.objects.values_list('slug', flat=True):
                self.slug = slug

        super(Product, self).save(*args, **kwargs)
