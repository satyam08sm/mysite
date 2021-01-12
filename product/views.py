from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView
from .models import ProductList
from cart.models import Cart


class ProductListView(ListView):
    model = ProductList
    template_name = 'product/product_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'] = Cart.objects.filter(user=self.request.user).first()
        print(context['cart'].products.all())
        return context


def add_to_cart(request, product_id):
    product = get_object_or_404(ProductList, id=product_id)
    cart = Cart.objects.filter(user=request.user)
    if cart:
        cart[0].products.add(product)
    else:
        cart = Cart.objects.create(user=request.user)
        cart.products.add(product)
    return redirect("product:product_list")


def remove_from_cart(request, product_id):
    product = get_object_or_404(ProductList, id=product_id)
    cart = Cart.objects.filter(user=request.user).first()
    cart.products.remove(product)
    return redirect("product:product_list")
