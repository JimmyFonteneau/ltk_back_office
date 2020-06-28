from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path(r'order-confirm/', views.order_confirm, name='order_confirm'),
    path(r'order-confirm-noaccount/', views.order_confirm_noaccount, name='order_confirm_noaccount'),
    path(r'create-user-orders-<str:user_email>-<int:artwork_id>/', views.create_user_orders, name='create_user_orders'),
]