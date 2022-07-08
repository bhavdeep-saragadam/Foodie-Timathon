from django.urls import reverse
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import views
from django.urls import reverse



urlpatterns = [
	
	path('todolist/',views.todo, name="todo"),
    
]
