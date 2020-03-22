from django.urls import path
from . import views

app_name = 'artists'

urlpatterns = [
    path('new/', views.artist_new, name='artist_new'),
    path('all/', views.all_artists, name='artists'),
]

