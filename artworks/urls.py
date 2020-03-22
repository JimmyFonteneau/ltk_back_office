from django.urls import path

from . import views

app_name = 'artworks'

urlpatterns = [
    path('new/', views.artwork_new, name='artwork_new'),
    path('list/', views.artworks_list, name='artworks_list'),
]