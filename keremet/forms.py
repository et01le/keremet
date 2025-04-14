"""Django forms"""
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import MinLengthValidator, MaxLengthValidator

class CustomUserCreationForm(UserCreationForm):
    """Form for user registartion"""
    username = forms.CharField(
        label = "Логин",
        validators = [
            MinLengthValidator(3, "Логин не может быть короче 3 символов"),
            MaxLengthValidator(255, "Логин не может быть длиннее 255 символов")
        ],
        widget = forms.TextInput(attrs = {
            "class": "form-control"
        })
    )

    class Meta(UserCreationForm.Meta):
        fields = ("username", "password1", "password2")
