from django.contrib.auth.models import User
from django.db import models

class Suplier (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=70)
    position = models.CharField(max_length=20)
    mail = models.EmailField()

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=70)
    address = models.CharField(max_length=50)
    phone = models.IntegerField()
    mail = models.EmailField()