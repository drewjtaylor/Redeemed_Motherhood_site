from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('clients/', views.clients, name='clients'),
    path('videos/', views.videos, name='videos'),
    path('invoices/', views.invoices, name='invoices'),
]