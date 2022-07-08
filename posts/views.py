from django.shortcuts import render, redirect
from .forms import PostForm
from django.contrib.auth.models import User
from .models import Post
from main.views import home
# Create your views here.

def CreatePost(request):
        profile = request.user
        form = PostForm()
        if request.method == 'POST':
                

                form = PostForm(request.POST, request.FILES)
                if form.is_valid():
                            post = form.save(commit=False)
                            post.owner = profile
                            post.save()
                            return redirect('home-page')
        context = {'form':form}
        return render(request, 'create-post.html',context)
