from pyexpat import model
from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField(max_length=264,unique=True)
    field_name = models.TextField(max_length=500)
