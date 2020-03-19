from django.urls import path
from . import views

urlpatterns = [
    path('artists/new/', views.artist_new, name='artist_new'),,    
]

