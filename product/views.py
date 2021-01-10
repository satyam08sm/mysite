from django.shortcuts import render
from django.views.generic import ListView
from .models import ProductList


class ProductListView(ListView):
    model = ProductList
    template_name = 'product/product_list.html'
