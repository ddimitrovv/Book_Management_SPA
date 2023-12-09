from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from server.books.choices import BookStatusChoices, BookGenreChoices
from server.users.models import UserProfile


class Book(models.Model):
    """
    Model representing a book.

    Attributes:
    - NAME_MAX_LEN (int): Maximum length for the book name.
    - AUTHOR_MAX_LEN (int): Maximum length for the author's name.
    - RATING_MIN_VALUE (int): Minimum allowed rating value.
    - RATING_MAX_VALUE (int): Maximum allowed rating value.
    - PRICE_MAX_DIGITS (int): Maximum number of digits for the price.
    - PRICE_DECIMAL_PLACES (int): Number of decimal places for the price.

    Fields:
    - name (CharField): The name of the book.
    - author (CharField): The author of the book.
    - picture (ImageField): An optional image associated with the book.
    - description (TextField): An optional description of the book.
    - rating (PositiveIntegerField): The rating of the book (if provided).
    - status (CharField): The status of the book, chosen from predefined choices.
    - price (DecimalField): The price of the book (if provided).
    - owner (ForeignKey): The user profile who owns the book.

    Methods:
    - __str__: Human-readable representation of the book instance.
    """

    NAME_MAX_LEN = 150
    AUTHOR_MAX_LEN = 50
    PRICE_MAX_DIGITS = 4
    PRICE_DECIMAL_PLACES = 2

    name = models.CharField(
        max_length=NAME_MAX_LEN
    )

    author = models.CharField(
        max_length=AUTHOR_MAX_LEN
    )

    picture = models.URLField(
        null=True,
        blank=True,
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    genre = models.TextField(
        choices=BookGenreChoices.choices
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

    ratings = models.ManyToManyField(
        UserProfile,
        through='BookRating',
        related_name='rated_books',
        blank=True,
    )

    def average_rating(self):
        """
        Calculate the average rating for the book.

        Returns:
        - float: The average rating or None if there are no ratings.
        """
        ratings = self.ratings.values_list('bookrating__rating', flat=True)
        if ratings:
            return sum(ratings) / len(ratings)
        return None

    def __str__(self):
        """
        Human-readable representation of the book instance.

        Returns:
        - str: A string representation of the book.
        """

        return f"{self.name} by {self.author}"


class BookRating(models.Model):
    """
    Model representing a user's rating for a book.

    Attributes:
    - user (ForeignKey): The user who rated the book.
    - book (ForeignKey): The book that is being rated.
    - rating (PositiveIntegerField): The rating given by the user.

    Meta:
    - unique_together: Ensures that a user can rate a book only once.

    Methods:
    - __str__: Human-readable representation of the book rating instance.
    """

    RATING_MIN_VALUE = 1
    RATING_MAX_VALUE = 5

    userprofile = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        related_name='book_ratings',
    )

    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='book_ratings',
    )

    rating = models.PositiveIntegerField(
        validators=[
            MinValueValidator(RATING_MIN_VALUE),
            MaxValueValidator(RATING_MAX_VALUE),
        ],
    )

    class Meta:
        unique_together = ('userprofile', 'book')

    def __str__(self):
        """
        Human-readable representation of the book rating instance.

        Returns:
        - str: A string representation of the book rating.
        """
        return f"{self.userprofile.user.username}'s rating ({self.rating}) for {self.book.name} by {self.book.author}"
