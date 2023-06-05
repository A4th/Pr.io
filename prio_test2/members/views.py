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

        log = "User -- " + str(username) + " -- has been logged-in successfully"
        if user is not None:
            login(request, user)
            messages.success(request, (log))
            return redirect('viewSched')
        else:
            messages.error(request, ("Invalid username/password"))
            return redirect('login')
    else:
        return render(request, 'registration/login.html', {})
    
def logout_user(request):
    username = request.user
    logout(request)

    log = "User -- " + str(username) + " -- has been logged-out successfully"
    messages.success(request, (log))
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
            is_active = form.cleaned_data['is_active']

            is_superuser = form.cleaned_data['is_superuser']
            is_staff = form.cleaned_data['is_staff']

            user = authenticate(email=email, username=username, password=password, 
                                is_active=is_active, is_superuser=is_superuser, is_staff=is_staff)
            login(request, user)

            return redirect('viewSched')
    else:
        form = RegisterUserForm()

    return render(request, 'registration/register.html', {'form':form,})