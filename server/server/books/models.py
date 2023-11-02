from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from custom.custom_choices import BookStatysChoices
from server.users.models import UserProfile


class Book(models.Model):
    NAME_MAX_LEN = 150
    AUTHOR_MAX_LEN = 50

    name = models.CharField(
        max_length=NAME_MAX_LEN
    )

    author = models.CharField(
        max_length=AUTHOR_MAX_LEN
    )

    picture = models.ImageField(
        null=True,
        blank=True,
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    rating = models.PositiveIntegerField(
        validators=(
            MinValueValidator(1),
            MaxValueValidator(5)
        ),
        blank=True,
        null=True
    )

    status = models.TextField(
        choices=BookStatysChoices.choices
    )

    price = models.PositiveIntegerField(
        blank=True,
        null=True
    )

    owner = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        related_name='books',
    )
