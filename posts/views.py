from django.shortcuts import render, redirect
from .forms import PostForm
from django.contrib.auth.models import User
from .models import Post

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
def UserPosts(request):
	profile = request.user
	projects = profile.Post_set.all()
	context = {'profile':profile, 'projects':projects}
	return render(request, 'user-posts.html')