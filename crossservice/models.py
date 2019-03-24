from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization = models.TextField(max_length=100)
    location = models.TextField(max_length=50)
    bio = models.TextField(max_length=100)
    type = models.TextField(default='customer')


def __str__(self):
    return self.user.username
