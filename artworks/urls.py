from django.urls import path

from . import views

app_name = 'artworks'

urlpatterns = [
    path('new/', views.artwork_new, name='artwork_new'),
    path('list/', views.artworks_list, name='artworks_list'),
    path('artwork-<int:artwork_id>/', views.artwork, name="artwork_show"),
    path('update-artwork-<int:artwork_id>/', views.update_artwork, name="artwork_update"),
    path('new-style/', views.add_style, name="add_style"),
    path('new-categorie/', views.add_category, name="add_category"),
    path('new-storage-place/', views.add_storage_place, name="add_storage_place"),
    path('all-style/', views.all_style, name="all_style"),
    path('update-style-<int:style_id>/', views.update_style, name="update_style"),
    path('all-category/', views.all_category, name="all_category"),
    path('update-category-<int:category_id>/', views.update_category, name="update_category"),
    path('all-storage-place/', views.all_storage_place, name="all_storage_place"),
    path('update-storage-place-<int:storage_place_id>/', views.update_storage_place, name="update_storage_place"),
]