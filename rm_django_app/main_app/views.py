from django.shortcuts import render
from django.http import HttpResponse
from .models import Client, Provider, Video, Invoice


# Create your views here.

def home(request):
    return render(request, 'home.html', {})

def index(request):
    return HttpResponse("This is the index page.")

def clients(request):
    return HttpResponse("This is the clients page.")

def videos(request):
    video_list = Video.objects.all()
    return HttpResponse("This is the video page")

def invoices(request):
    return HttpResponse("This is the invoices page.")

def try_template(request):
    return HttpResponse(f"")