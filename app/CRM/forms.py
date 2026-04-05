from django import forms
from django.contrib.auth.forms import AuthenticationForm

class StyledLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-input',
        'placeholder': 'Enter username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-input',
        'placeholder': 'Enter password'
    }))
