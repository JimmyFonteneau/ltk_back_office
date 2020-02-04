from django import forms

from .models import UserProfile

class LoginForm(forms.Form):

    username = forms.CharField(
        label = "Nom d'utilisateur",
        max_length=64,
        required=True,
    )
    password = forms.CharField(
        label = "Mot de passe",
        max_length=256,
        required=True,
        widget=forms.PasswordInput(),
    )
