from django.urls import path
from . import views
from .views import SearchResultsView

urlpatterns = [
    path(r'', views.homepage, name='homepage'),
    path('search/', views.search_result_view, name='search_results'),
     path('dashboard/', views.dashboard, name='dashboard'),   
]