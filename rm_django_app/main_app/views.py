from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm


from .models import Client, Provider, Video, Invoice


# Create your views here.

def home(request):
    return render(request, 'home.html')


# Signup form for creating new users
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login(request):
    form = AuthenticationForm
    return render(request, 'login.html', {'form': form})

def authtestpage(request):
    user = authenticate(username="testuser", password="testpassword")
    if user is not None:
        return HttpResponse("The user WAS authenticated")
    else:
        return HttpResponse("The user was not authenticated")