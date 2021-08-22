from django.db import models

from wasbam_wears.utils import generate_slug
from products.handlers import product_image_handler


class Product(models.Model):

    name = models.CharField(max_length=255, blank=False)
    image = models.ImageField(upload_to=product_image_handler)
    description = models.TextField(blank=True)
    price = models.PositiveIntegerField(default=0)
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
            slug = generate_slug(60)
            slug_exits = Product.objects.filter(slug=slug).exists()

            if not slug_exits:
                self.slug = slug

        super(Product, self).save(*args, **kwargs)

    def delete(self):
        self.image.delete()
        super(Product, self).delete()
