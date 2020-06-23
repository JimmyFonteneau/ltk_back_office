from django.contrib import admin

from .models import Artwork, Artwork_Style, Artwork_Category, Artwork_Storage_Place

admin.site.register(Artwork)
admin.site.register(Artwork_Style)
admin.site.register(Artwork_Category)
admin.site.register(Artwork_Storage_Place)