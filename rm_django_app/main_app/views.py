from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm


from .models import Client, Provider, Video, Invoice


# Create your views here.

def home(request):
    return render(request, 'home.html')

def index(request):
    return HttpResponse("This is the index page.")

def clients(request):
    return HttpResponse("This is the clients page.")

def invoices(request):
    return HttpResponse("This is the invoices page.")

# def try_template(request):
#     return HttpResponse(f"")


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