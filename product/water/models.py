from django.db import models

# Create your models here.

class Water(models.Model):
    title=models.CharField(max_length=100),
    litres=models.IntegerField(default=0),
    raiting=models.IntegerField(max_length=100),