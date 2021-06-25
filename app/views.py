from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth import authenticate,login as loginUser,logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import ToDoForm
from .models import Todo
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def index(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            user = request.user
            form = ToDoForm()
            todos = Todo.get_all_todos(user)
            data = {
                'form' : form ,
                'todos' : todos
            }
            return render(request, 'index.html',data)
    else:
        if request.user.is_authenticated:
            user = request.user
            form = ToDoForm(request.POST)
            if form.is_valid():
                todo = form.save(commit=False)
                todo.user = user
                form.save()
                return redirect('homepage')
            else:
                return render(request, 'index.html', {'form': form})

def signup(request):
    if request.method == 'GET':
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})

    else:
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            if user is not None:
                return redirect('homepage')
        else:
            return render(request, 'signup.html', {'form': form})


def login(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

    else:
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password= password)
            if user is not None:
                loginUser(request,user)
                return redirect('homepage')
            else:
                return render(request, 'login.html', {'form': form})
        else:
            return render(request, 'login.html', {'form': form})


def signout(request):
    logout(request)
    return redirect('login')

def deletetodo(request, id):
    todo = Todo.delete_todo(id)
    if todo:
        return redirect('homepage')
    else:
        error_message = "There is a problem while deleting"
        return redirect('homepage',{'error':error_message})

def changestatus(request,id, status):
    todo = Todo.change_todo_status(id,status)
    if todo:
        return redirect('homepage')
    else:
        error_message = "There is a problem while deleting"
        return redirect('homepage',{'error':error_message})