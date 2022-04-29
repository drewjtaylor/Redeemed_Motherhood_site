from django.urls import path, re_path
from django.conf.urls import url

from . import views


app_name = "main_app"

urlpatterns = [
    path('', views.home, name='home'),
    url('signup/', views.signup, name='signup'),
    url('login/', views.login, name='login'), #Currenctly conflicts with default "login" added to urls
    url('authtestpage/', views.authtestpage, name="authtest"),
]


