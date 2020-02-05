from django.urls import path

from users import views

app_name = 'users'

urlpatterns = [
    path('logout/', views.logout_view, name="logout"),
    path('login/', views.login_view, name="login"),
    path('register/', views.register_view, name="register"),
    path('myaccount/', views.myaccount, name="myaccount"),
    path('account_settings/', views.account_settings, name="account_settings"),
]