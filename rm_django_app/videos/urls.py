from django.urls import path

from . import views


app_name = 'videos'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('<int:video_id>/', views.viewvid, name='viewvid'),
]