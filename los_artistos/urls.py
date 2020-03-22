from django.contrib import admin
from django.urls import path, include

import artworks, users, homepage, artists

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'artworks/', include('artworks.urls', namespace='artworks')),
    path(r'users/', include('users.urls', namespace='users')),
    path(r'artists/', include('artists.urls', namespace='artists')),
    path('', include ('homepage.urls')),
    path('', include('pwa.urls')),
]
