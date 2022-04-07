from django.db import models

# Create your models here.

class Videos(models.Model):
    link = models.CharField(max_length=100)
    title = models.CharField(max_length=50)