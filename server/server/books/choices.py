from django.db import models


class BookStatusChoices(models.TextChoices):
    READ = 'Read', 'Read'
    IN_PROGRESS = 'Reading', ' Reading'
    UNREAD = 'Unread', 'Unread'
    TO_BUY = 'Want to Buy', 'Want to Buy'
