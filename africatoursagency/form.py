from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(
        widget=forms.PasswordInput, label="Confirm Password")


class Meta:
    model = User
    fields = [
        'username',
        'password',
        'password_confirm'
    ]


def clean(self):
    cleaned_data = super().clean()
    password = cleaned_data.get('password')
    password_confrim = cleaned_data.get('password_confirm')

    # check if the passwords match
    if password and password_confrim and password != password_confrim:
        raise forms.ValidationError('Passwords do not match')
    return cleaned_data
