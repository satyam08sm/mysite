from django.db import models
from django.conf import settings
from product.models import ProductList


class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False, blank=False)
    products = models.ManyToManyField(ProductList)

    def __str__(self):
        return str(self.products.count()) + " products in cart"

    def cart_total(self):
        total = 0
        for product in self.products.all():
            total += product.product_price() * product.get_quanity()
        return total
