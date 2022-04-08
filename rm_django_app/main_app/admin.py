from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Client

# Register your models here.

admin.site.register(Client, UserAdmin)