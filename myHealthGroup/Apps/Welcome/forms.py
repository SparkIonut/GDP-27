from django import forms
from django.contrib.auth.models import User

class User_Login(forms.Form):
	username = forms.CharField(label='Username', max_length=30)
	password = forms.CharField(widget=forms.PasswordInput,label='Password', max_length=30)