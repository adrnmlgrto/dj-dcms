from django import forms
from django.contrib.auth.forms import AuthenticationForm

__all__ = ['CustomAuthenticationForm']


class CustomAuthenticationForm(AuthenticationForm):
    """
    Modified authentication form for our own defined user model.

    Since our user model accepts email as the username field,
    we need to modify the form to accept email as the username field.
    """
    username = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(
            attrs={
                'autocomplete': 'email',
                'autofocus': True
            }
        )
    )
    password = forms.CharField(
        label='Password',
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'current-password'
            }
        )
    )
