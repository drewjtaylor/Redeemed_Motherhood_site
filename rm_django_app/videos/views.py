from django.shortcuts import render
from django.http import HttpResponse
from main_app.models import Client, Video

# Create your views here.

def index(request):
    video_list = Video.objects.all()
    context = {'video_list': video_list}
    return render(request, 'videos/index.html', context)

def viewvid(request, video_id):
    video = Video.objects.get(pk=video_id)
    context = {'video_id': video_id, 'video': video}
    return render(request, 'videos/viewvid.html', context)