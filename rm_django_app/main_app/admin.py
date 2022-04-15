from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Client, Provider, Video, Invoice

# Register your models here.

admin.site.register(Client, UserAdmin)
admin.site.register(Provider)
admin.site.register(Video)
admin.site.register(Invoice)