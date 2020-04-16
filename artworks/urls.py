from django.urls import path

from . import views

app_name = 'artworks'

urlpatterns = [
    path('new/', views.artwork_new, name='artwork_new'),
    path('list/', views.artworks_list, name='artworks_list'),
    path('artwork-<int:artwork_id>/', views.artwork, name="artwork_show"),
    path('update-artwork-<int:artwork_id>/', views.update_artwork, name="artwork_update"),
]