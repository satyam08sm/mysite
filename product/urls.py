from django.urls import path
from .views import ProductListView, add_to_cart, remove_from_cart

app_name = 'product'
urlpatterns = [
    path('list/', ProductListView.as_view(), name='product_list'),
    path('add-to-cart/<int:product_id>', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<int:product_id>', remove_from_cart, name='remove-from-cart'),
]
