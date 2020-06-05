from django.urls import path

from . import views

app_name = 'site_content'

urlpatterns = [
    path('edit/', views.update_content, name='update_content'),
]