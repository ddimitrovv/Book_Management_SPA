from django.db import models


class BookStatusChoices(models.TextChoices):
    """
    Choices for the status of a book.

    This class defines predefined choices for the status of a book. Each choice
    consists of a human-readable name and its corresponding database value.

    Choices:
    - READ: The book has been read.
    - IN_PROGRESS: The book is currently being read.
    - UNREAD: The book has not been read.
    - TO_BUY: The user wants to buy this book.
    """

    READ = 'Read', 'Read'
    IN_PROGRESS = 'Reading', ' Reading'
    UNREAD = 'Unread', 'Unread'
    TO_BUY = 'Want to Buy', 'Want to Buy'
