from django.urls import path

from users import views

app_name = 'users'

urlpatterns = [
    path('logout/', views.logout_view, name="logout"),
    path('login/', views.login_view, name="login"),
]