from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField


# Create your models here.
# user model - same for customer and provider
class UserProfileInfo(models.Model):
    type_choices = (('item_key1', 'Customer'),
                    ('item_key2', 'Provider'))
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization = models.TextField(max_length=100)
    location = models.TextField(max_length=50)
    bio = models.TextField(max_length=100)
    type = MultiSelectField(choices=type_choices, max_choices=1)


def __str__(self):
    return self.user.username
