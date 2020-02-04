from django.contrib import admin
from django.urls import path, include

import artworks

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'artworks/', include('artworks.urls', namespace='artworks')),
]
