from django.shortcuts import render, redirect
from posts.forms import PostForm
from django.contrib.auth.models import User
from posts.models import Post
# Create your views here.



def home(request):
	posts = Post.objects.all()
	context = {'posts': posts}
	return render(request, 'home.html', context)
def findFood(request):
	return render(request, 'search.html')