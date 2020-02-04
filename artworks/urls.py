from django.urls import path

from . import views

app_name = 'artworks'

urlpatterns = [
    path('list/', views.artworks_list, name='artworks_list'),
]