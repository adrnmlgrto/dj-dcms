from typing import override

from django import forms

from user.models import Profile, User


class UserCreateForm(forms.Form):
    """
    Form for creating a new user instance.
    """
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(
            attrs={
                'autocomplete': 'email'
            }
        )
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'new-password'
            }
        )
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'new-password'
            }
        )
    )

    def clean_email(self):
        """
        Check if email already exists in the database.
        """
        email = self.cleaned_data['email'].lower()
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'A user with this email already exists.'
            )
        return email

    @override
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        # Verify that password and confirm password match.
        if password1 and password2 and password1 != password2:
            self.add_error('password2', 'Passwords do not match.')

        return cleaned_data


class ProfileCreateForm(forms.ModelForm):
    """
    Form for creating a new profile instance.
    """
    class Meta:
        model = Profile
        fields = [
            'first_name',
            'middle_name',
            'last_name',
            'gender',
            'birthday',
            'avatar',
        ]
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }
