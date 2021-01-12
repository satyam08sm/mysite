from django.urls import path
from .views import CartDetails

app_name = 'cart'
urlpatterns = [
    path('<int:pk>', CartDetails.as_view(), name='cart-details'),
]
