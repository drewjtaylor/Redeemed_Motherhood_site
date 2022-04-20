from django.urls import path
from django.conf.urls import url

from . import views


app_name = "main_app"

urlpatterns = [
    path('', views.home, name='home'),
    url('signup/', views.signup, name='signup'),
]