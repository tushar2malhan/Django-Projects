from django.db import models
from django.db.models.base import Model
from django.utils import timezone
from django.db.models.fields import AutoField
# Create 3 models in animals app -> 
# Mammal, Bird and Fish with features mentioned above

CHOICES = [
    ('Male','female')
]
class Mammal(models.Model):
    name = models.CharField(max_length=100,primary_key=True)
    species = models.CharField(max_length=100 , null=True, blank=True) 
    food = models.CharField(max_length=100, null=True, blank=True)
    last_feed = models.DateField(null=True, blank=True)
    gender = models.CharField(choices=CHOICES,max_length=100)

    def __str__(self):
        return f'{self.name} , {self.gender}'

class Bird(models.Model):
    name = models.CharField(max_length=100,primary_key=True)
    species = models.CharField(max_length=100,null=True, blank=True)
    food =models.CharField(max_length=100,null=True)
    last_feed=models.DateField(null=True,blank=True)
    
    def __str__(self):
        return f'{self.name , self.species}'

class Fish(models.Model):
    color = models.CharField(max_length=100,null=True, blank=True)
    species = models.CharField(max_length=100,null=True)
    food = models.CharField(max_length=100,null=True)
    count = models.IntegerField(null=True,blank=True)
    last_feed = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.color , self.species}'