from django.db import models


class Gender(models.TextChoices):
    """
    Choices for the gender field in the UserProfile model.

    This class defines predefined choices for the gender field in the UserProfile model.
    Each choice consists of a human-readable name and its corresponding database value.

    Choices:
    - FEMALE: Represents the female gender.
    - MALE: Represents the male gender.
    - OTHER: Represents a gender option other than female or male.
    """

    FEMALE = 'Female', 'Female'
    MALE = 'Male', 'Male'
    OTHER = 'Other', 'Other'
