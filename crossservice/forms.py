from django import forms
from crossservice.models import UserProfileInfo
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
        fields = ('organization', 'location', 'type', 'bio')
