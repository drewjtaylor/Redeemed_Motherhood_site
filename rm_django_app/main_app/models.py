from django.db import models

# Create your models here.

class Videos(models.Model):
    title = models.CharField(max_length=35)
    link = models.CharField(max_length=100)