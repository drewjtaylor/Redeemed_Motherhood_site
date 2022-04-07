from django.db import models

# Create your models here.


class Providers(models.Model):
    name = models.CharField("Business name", max_length=50)
    contact = models.CharField("Contact person", max_length=30)
    email = models.CharField(max_length=50)
    phone = models.CharField("Phone number", max_length=10, )

class Videos(models.Model):
    title = models.CharField(max_length=35)
    link = models.CharField(max_length=100)

class Invoices(models.Model):
    amount = models.DecimalField(max_digits=5, decimal_places=2)
#    owing_client = models.ForeignKey(Client, on_delete=models.CASCADE)