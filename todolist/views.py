from django.shortcuts import render, redirect
from .models import Todo, TodoPage
from .forms import TodoForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url = "login")

def todo(request):
    

    todo = Todo.objects.all()

    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)

    if form.is_valid():
        todo = form.save(commit=False)
        todo.owner = request.user
        todo.save()
        return redirect('todo')

    context = {'todo': todo, 'form': form}
    return render(request, 'todo.html', context)
