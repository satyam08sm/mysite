from django.db import models
import django.utils
from django.shortcuts import reverse
from django.core.validators import MaxValueValidator

CATEGORIES = (
    ('clothes', 'CLOTHES'),
    ('mobile', 'MOBILE'),
    ('laptop', 'LAPTOP'),
    ('home appliances', 'HOME_APPLIANCES'),
    ('miscellaneous', 'MISCELLANEOUS'),
)


class ProductList(models.Model):
    name = models.CharField(max_length=50, blank=False)
    img = models.ImageField(upload_to='images')
    desc = models.TextField(max_length=500)
    price = models.IntegerField(default=0)
    category = models.CharField(null=True, choices=CATEGORIES, max_length=20)
    created_at = models.DateTimeField(editable=False, auto_now_add=True)
    updated_at = models.DateTimeField(editable=False, auto_now=True)
    discount = models.IntegerField(validators=[MaxValueValidator(100)], default=0)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.name

    def product_price(self):
        return (1 - (self.discount / 100)) * self.price

    def get_quanity(self):
        return self.quantity

    def get_final_price(self):
        return self.product_price() * self.get_quanity()

    def get_add_to_cart_url(self):
        return reverse("product:add-to-cart", args=(self.id,))

    def get_remove_from_cart_url(self):
        return reverse("product:remove-from-cart", args=(self.id,))
