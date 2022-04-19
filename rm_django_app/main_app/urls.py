from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('clients/', views.clients, name='clients'),
    path('invoices/', views.invoices, name='invoices'),
    url('signup/', views.signup, name='signup'),
]