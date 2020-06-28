from django.urls import path
from . import views

app_name = 'carts'

urlpatterns = [
    path(r'mycart/', views.cart_detail, name='cart_detail'),
    path(r'add-<int:artwork_id>/', views.cart_add, name='cart_add'),
    path(r'remove-<int:artwork_id>/', views.cart_remove, name='cart_remove'),
]