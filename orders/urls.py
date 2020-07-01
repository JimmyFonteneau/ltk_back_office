from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path(r'order-confirm/', views.order_confirm, name='order_confirm'),
    path(r'order-confirm-noaccount/', views.order_confirm_noaccount, name='order_confirm_noaccount'),
    path(r'accept-order-<int:order_id>/', views.accept_order, name='accept_order'),
    path(r'deny-order-<int:order_id>/', views.deny_order, name='deny_order'),
]