from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.core.validators import MinLengthValidator

from custom.custom_choices import Gender


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, is_staff=False, is_superuser=False):
        if not username:
            raise ValueError("The Username field must be set.")
        user = self.model(username=username, is_staff=is_staff, is_superuser=is_superuser)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, password, **extra_fields)


class CustomUser(PermissionsMixin, AbstractBaseUser):
    class Meta:
        verbose_name = 'Users'
        verbose_name_plural = 'Users'

    username = models.CharField(
        max_length=50,
        unique=True,
    )

    email = models.EmailField(
        unique=True,
    )

    is_active = models.BooleanField(
        default=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

    # Add the fields required for creating a user via the createsuperuser management command.
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    # Deactivate user instead of deleting the user.
    def deactivate_user(self):
        self.is_active = False
        self.save()

    def __str__(self):
        return self.username


class UserProfile(models.Model):
    FIRST_NAME_MAX_LEN = 20
    FIRST_NAME_MIN_LEN = 2
    LAST_NAME_MAX_LEN = 20
    LAST_NAME_MIN_LEN = 2

    first_name = models.CharField(
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LEN),
        ),
        max_length=FIRST_NAME_MAX_LEN,
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LEN),
        ),
        max_length=LAST_NAME_MAX_LEN,
        null=True,
        blank=True,
    )

    profile_picture = models.ImageField(
        null=True,
        blank=True,
    )

    gender = models.CharField(
        choices=Gender.choices,
        max_length=10,
        blank=True,
        null=True,
    )
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'Username: {CustomUser.objects.get(id=self.pk)}'

