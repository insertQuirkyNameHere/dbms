from django import forms
from django.forms.widgets import PasswordInput

class LoginForm(forms.Form):
    email       = forms.EmailField(max_length=255, required=True, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password    = forms.CharField(required=True, widget=PasswordInput(attrs={'placeholder':'Password'}))
