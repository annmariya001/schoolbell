from django.urls import path
from app import views


urlpatterns = [
    path('',views.home, name="home"),
    path('login', views.login_view,  name="login"),
    path('register', views.register, name="register")
]