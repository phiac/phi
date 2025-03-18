# forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=255, label='Username')
    password = forms.CharField(max_length=255, label='Password', widget=forms.PasswordInput)
