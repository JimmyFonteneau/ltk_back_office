from django.urls import path
from . import views

app_name = 'carts'

urlpatterns = [
    path('add/', views.cart_add, name='cart_add'),
    path('length/', views.cart_length, name='cart_length'),
    path('delete/', views.cart_delete, name='cart_delete'),
    path('mycart/', views.cart, name='cart_list'),
]