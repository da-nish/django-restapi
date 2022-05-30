from django.db import models

# Create your models here.


class users(models.Model):
    username = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100, default='none')
    email = models.CharField(max_length=100, default='none')
    age = models.CharField(max_length=100, default='none')
    mobile = models.CharField(max_length=100, default='none')