from django.urls import path
from . import views

app_name = 'rates'

urlpatterns = [
    path('update-rate-<int:rate_id>/', views.update, name='rates_update'),
    path('add/', views.add, name='rates_add'),
    path('list/', views.rates_list, name='rates_list'),
]

