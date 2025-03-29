from typing import override

from django.contrib.auth.models import AbstractUser
from django.core.validators import validate_email
from django.db import models

from ..managers import CustomUserManager

__all__ = ['User']


class User(AbstractUser):
    """
    The custom user model for system authentication.

    Fields `email`, and `password` would be used for authentication.

    For suspension of users, see the `is_active` field.
    Please do not delete the instance of a user.
    """
    # Define the manager for the custom user model.
    objects = CustomUserManager()

    # Remove username, and set email as the unique identifier.
    username = None
    email = models.EmailField(
        unique=True,
        validators=[validate_email]
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    @override
    def __str__(self) -> str:
        return self.email
