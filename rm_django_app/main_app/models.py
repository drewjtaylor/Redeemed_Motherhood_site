from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Client(AbstractUser):
    phone = models.CharField(max_length=10, null=True)
    partner_name = models.CharField(max_length=50, null=True)
    partner_phone = models.CharField(max_length=10, null=True)
    partner_email = models.CharField(max_length=50, null=True)
    address = models.CharField("street address", max_length=50, null=True)
    city = models.CharField(max_length=20, null=True)
    zip = models.CharField("zip code", max_length=9, null=True)
    state = models.CharField(max_length=2, null=True)
    due_date = models.DateField(null=True)

class Provider(models.Model):
    name = models.CharField("Business name", max_length=50)
    contact = models.CharField("Contact person", max_length=30)
    email = models.CharField(max_length=50)
    phone = models.CharField("Phone number", max_length=10, )

class Video(models.Model):
    title = models.CharField(max_length=35)
    link = models.CharField(max_length=100)

class Invoice(models.Model):
    amount = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    owing_client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)

