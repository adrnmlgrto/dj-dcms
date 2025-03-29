import hashlib
import os
from typing import override

from django.conf import settings
from django.core.validators import validate_image_file_extension
from django.db import models

from .utils import GenderChoices

__all__ = ['Profile']


def avatar_upload_to(instance: 'Profile', filename: str) -> str:
    """
    The avatar upload path for the profile model.

    This generates a hashed file name and directory
    structure for the uploaded avatar.

    Args:
        instance (Profile): The profile instance.
        filename (str): The original filename of the avatar.

    Returns:
        str: The hashed file name and directory structure.
    """
    # Extract file extension.
    _, ext = os.path.splitext(filename)
    ext = ext.lower()

    # Read image content and compute SHA256 hash.
    image_data: bytes = instance.avatar.read()
    hashed_name: str = hashlib.sha256(image_data).hexdigest()

    # Organize into a hashed directory structure.
    # NOTE: The first 2 characters are folders.
    return f'avatars/{hashed_name[:2]}/{hashed_name}{ext}'


class Profile(models.Model):
    """
    The profile model for user in the system.
    """
    # Associated User
    # NOTE: Can be accessed as `user.profile`.
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profile'
    )

    # Profile Data
    avatar = models.ImageField(
        upload_to=avatar_upload_to,
        blank=True,
        null=True,
        validators=[validate_image_file_extension]
    )
    first_name = models.CharField(
        max_length=50
    )
    middle_name = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )
    last_name = models.CharField(
        max_length=50
    )
    birthday = models.DateField(
        blank=True,
        null=True
    )
    gender = models.CharField(
        max_length=10,
        blank=True,
        null=True,
        choices=GenderChoices.choices
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    @property
    def full_name(self) -> str:
        if self.middle_name:
            return f'{self.first_name} {self.middle_name} {self.last_name}'
        return f'{self.first_name} {self.last_name}'

    @property
    def name_initials(self) -> str:
        return f'{self.first_name[0]}{self.last_name[0]}'

    @override
    def __str__(self) -> str:
        return self.full_name

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
