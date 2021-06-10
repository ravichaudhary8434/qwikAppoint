from django import forms
from django.forms import fields, models
from .models import UserProfile
from django.contrib.auth.models import User


class UserForm(models.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class ProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('contact', 'dob')
