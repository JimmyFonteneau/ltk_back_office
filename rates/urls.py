from django.urls import path
from . import views

app_name = 'rates'

urlpatterns = [
    path('update/', views.update, name='rates_update'),
     path('add/', views.add, name='rates_add'),
]

