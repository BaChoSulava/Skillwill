from django.db import models

class Animal(models.Model):
    name = models.CharField(max_length=50)
    species = models.CharField(max_length=50)
    habitat = models.CharField(max_length=50)
    lifespan = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.species})"

