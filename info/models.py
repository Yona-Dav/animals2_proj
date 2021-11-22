from django.db import models

# Create your models here.

class Family(models.Model):
    name = models.CharField(max_length=100)

class Animal(models.Model):
    name = models.CharField(max_length=100)
    legs = models.PositiveIntegerField(null=True)
    weight = models.CharField(max_length=100)
    height = models.CharField(max_length=100)
    speed = models.PositiveIntegerField(null=True)
    family = models.ForeignKey(Family, on_delete=models.CASCADE)
