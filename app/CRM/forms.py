from django import forms
from django.contrib.auth.forms import AuthenticationForm

class StyledLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'style': 'margin-left:0;',
        'class':'login-card',
        'placeholder': 'Enter username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'login-card',

        'style': 'margin-left:0;',
        'placeholder': 'Enter password'
    }))
