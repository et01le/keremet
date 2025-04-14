"""Django forms"""
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.utils.text import normalize_newlines
from .models import Term

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

class TermForm(forms.ModelForm):
    """Form for terms"""
    
    def validate_term(self):
        """Validate input term"""
        input = self.cleaned_data["term"]
        input_normalized = " ".join(normalize_newlines(input).strip().lower().split())
        for term in Term.objects.all():
            term_normalized = " ".join(normalize_newlines(term).strip().lower().split())
            if input_normalized == term_normalized:
                raise ValidationError("Данный термин уже существует")
        return input

    class Meta:
        model = Term
        fields = ("term", "translation")
