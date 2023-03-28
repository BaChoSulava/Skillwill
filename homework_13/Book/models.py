from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    author = models.CharField(max_length=100, null=True, blank=True)