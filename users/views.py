from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import User
from django.contrib.auth.decorators import login_required

# Create your views here.

def login_excluded(redirect_to):
    """ This decorator kicks authenticated users out of a view """ 
    def _method_wrapper(view_method):
        def _arguments_wrapper(request, *args, **kwargs):
            if request.user.is_authenticated:
                return redirect(redirect_to) 
            return view_method(request, *args, **kwargs)
        return _arguments_wrapper
    return _method_wrapper

@login_excluded('home-page')
def loginPage(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		try:
			user = User.objects.get(username=username)
		except:
			messages.error(request,'Username does not exist')
		
		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('login-page')
		else:
			messages.error(request,'Username Or Password are Incorrect')
		
	context = {}
	return render(request, 'login.html',context)


@login_excluded('home-page')
def register(request):
	form = User()

	if request.method == 'POST':
		form = User(request.POST)
		if form.is_valid():
			form.save()
			return redirect('account')
	context = {'form': form}
	return render(request, 'register.html',context)
@login_required(login_url = "login")

def logOut(request):
	logout(request)
	messages.error(request,'Successfully Logged Out!')
	return redirect('login-page')

def account(request):
	

	

	context = {}
	return render(request, 'account.html', context)