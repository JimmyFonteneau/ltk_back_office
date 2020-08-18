from django.urls import path
from . import views

app_name = 'configuration'

urlpatterns = [
    path('update-configuration/', views.update, name='configuration_update'),
]

