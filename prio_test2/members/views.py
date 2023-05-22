from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.contrib.auth.models import Group

# Create your views here.

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('viewSched')
        else:
            return redirect('login')
    else:
        return render(request, 'registration/login.html', {})
    
def logout_user(request):
    logout(request)
    messages.success(request, ("You were logged-out successfully"))
    return redirect('login')

def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            hello = form.save()
            group = Group.objects.get(name='Default_user')
            hello.groups.add(group)

            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(email=email, username=username, password=password)
            login(request, user)
            messages.success(request, ("You were logged out successfully, " + str(username)))

            return redirect('viewSched')
    else:
        form = RegisterUserForm()

    return render(request, 'registration/register.html', {'form':form,})