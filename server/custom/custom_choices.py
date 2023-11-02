from django.db import models


class Gender(models.TextChoices):
    FEMALE = 'Female', 'Female'
    MALE = 'Male', 'Male'
    OTHER = 'Other', 'Other'


class BookStatysChoices(models.TextChoices):
    READ = 'Read', 'Read'
    IN_PROGRESS = 'Reading', ' Reading'
    UNREAD = 'Unread', 'Unread'
    TO_BUY = 'Want to Buy', 'Want to Buy'
