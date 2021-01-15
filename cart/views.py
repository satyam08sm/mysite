from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.shortcuts import get_object_or_404, redirect
from .models import Cart
from product.models import ProductList


class CartDetails(LoginRequiredMixin, generic.DetailView):
    model = Cart
    template_name = 'cart/cart_details.html'
