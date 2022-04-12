from django.shortcuts import render
from django.http import HttpResponse
from main_app.models import Client, Video

# Create your views here.

def index(request):
    video_list = Video.objects.all()
    return HttpResponse("This is the video index page")

def viewvid(request, video_id):
    context = {'video_id': video_id}
    return render(request, 'videos/viewvid.html', context)