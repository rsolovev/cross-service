from django import forms
from django.contrib.auth.forms import UserChangeForm

from crossservice.models import UserProfileInfo, ServicePostInfo
from django.contrib.auth.models import User


# form for storing basic info (pass, login, email)
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password', 'email')


# form for storing additional info
class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        fields = ('organization', 'location', 'bio')


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        fields = ('organization', 'location', 'bio')


class PostServiceForm(forms.ModelForm):
    class Meta:
        model = ServicePostInfo
        fields = (
            'service_name', 'service_description', 'city_of_provision', 'time_of_availability',
            'rate_of_payment_per_hour')


class EditPostForm(forms.ModelForm):
    class Meta:
        model = ServicePostInfo
        fields = (
            'service_name', 'service_description', 'city_of_provision', 'time_of_availability',
            'rate_of_payment_per_hour')
