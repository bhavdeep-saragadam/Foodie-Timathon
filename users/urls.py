from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('login/', views.loginPage, name='login-page'),
    path('register', views.register, name='register-page'),
    path('profile/', views.account, name='account'),
    path('logOut/', views.logOut, name='logOut'),


]
