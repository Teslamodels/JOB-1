from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.CharField(max_length=500)
    address = models.CharField(max_length=1000)
    last_name = models.CharField(max_length=300)
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=300)



