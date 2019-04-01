from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# user model - same for customer and provider
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization = models.TextField(max_length=100)
    location = models.TextField(max_length=50)
    bio = models.TextField(max_length=100)


class ServicePostInfo(models.Model):
    service_name = models.TextField(max_length=100)
    service_description = models.TextField(max_length=280)  # like in Twitter:D
    city_of_provision = models.TextField(max_length=150)
    time_of_availability = models.TextField(max_length=35)
    rate_of_payment_per_hour = models.IntegerField()


def __str__(self):
    return self.user.username
