from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from server.books.choices import BookStatusChoices
from server.users.models import UserProfile


class Book(models.Model):
    NAME_MAX_LEN = 150
    AUTHOR_MAX_LEN = 50
    RATING_MIN_VALUE = 1
    RATING_MAX_VALUE = 5
    PRICE_MAX_DIGITS = 4
    PRICE_DECIMAL_PLACES = 2

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
            MinValueValidator(RATING_MIN_VALUE),
            MaxValueValidator(RATING_MAX_VALUE)
        ),
        blank=True,
        null=True
    )

    status = models.TextField(
        choices=BookStatusChoices.choices
    )

    price = models.DecimalField(
        max_digits=PRICE_MAX_DIGITS,
        decimal_places=PRICE_DECIMAL_PLACES,
        blank=True,
        null=True
    )

    owner = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        related_name='books',
    )

    def __str__(self):
        return f"{self.name} by {self.author}"
