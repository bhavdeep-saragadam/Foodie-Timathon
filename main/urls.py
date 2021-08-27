from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.home, name='home-page' ),
    path('healthy-food/', views.findFood, name='healthy-food-page' ),

]
