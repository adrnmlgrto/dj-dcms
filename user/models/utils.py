from django.db.models import TextChoices


class GenderChoices(TextChoices):
    MALE = 'M', 'Male'
    FEMALE = 'F', 'Female'
    OTHER = 'O', 'Others'
