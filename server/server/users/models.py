from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator

from server.users.choices import Gender


class CustomUserManager(BaseUserManager):
    """
    Custom user manager model.

    This manager provides methods to create regular users and superusers.

    Methods:
    - create_user: Create and return a regular user.
    - create_superuser: Create and return a superuser.
    """

    def create_user(self, username, email, password=None, is_staff=False, is_superuser=False):
        """
        Create and return a regular user with an email and password.

        Parameters:
        - username (str): The username for the new user.
        - email (str): The email address for the new user.
        - password (str): The password for the new user.
        - is_staff (bool): Whether the user is a staff member.
        - is_superuser (bool): Whether the user is a superuser.

        Returns:
        - CustomUser: The newly created user.
        """

        if not username:
            raise ValueError("The Username field must be set.")
        user = self.model(username=username, email=email, is_staff=is_staff, is_superuser=is_superuser)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        """
        Create and return a superuser with an email and password.

        Parameters:
        - username (str): The username for the new superuser.
        - email (str): The email address for the new superuser.
        - password (str): The password for the new superuser.
        - extra_fields (dict): Additional fields for the new superuser.

        Returns:
        - CustomUser: The newly created superuser.
        """

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, email, password, **extra_fields)


class CustomUser(PermissionsMixin, AbstractBaseUser):
    """
    Custom user model.

    This model represents users in the system.

    Fields:
    - username (CharField): The username for the user.
    - email (EmailField): The email address for the user.
    - is_active (BooleanField): Whether the user is active.
    - is_staff (BooleanField): Whether the user is a staff member.
    - is_superuser (BooleanField): Whether the user is a superuser.
    - confirmation_token (CharField): Token for email confirmation.
    - is_email_confirmed (BooleanField): Whether the user's email is confirmed.
    - is_deleted (BooleanField): Whether the user is deleted.

    Attributes:
    - USERNAME_FIELD (str): The field used as the unique identifier for the user.
    - REQUIRED_FIELDS (list): Additional fields required for creating a user via createsuperuser.

    Methods:
    - deactivate_user: Deactivate the user by setting is_active to False.
    - __str__: Human-readable representation of the user.
    """

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

    is_superuser = models.BooleanField(
        default=False
    )

    confirmation_token = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )

    is_email_confirmed = models.BooleanField(
        default=False
    )

    is_deleted = models.BooleanField(
        default=False
    )

    USERNAME_FIELD = 'username'

    """Add the fields required for creating a user via the createsuperuser management command."""
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def deactivate_user(self):
        """
        Deactivate the user by setting is_active to False.
        """
        self.is_active = False
        self.save()

    def __str__(self):
        """
        Human-readable representation of the user.

        Returns:
        - str: A string representation of the user.
        """
        return self.username


class UserProfile(models.Model):
    """
    User Profile model.

    This model represents additional information about a user.

    Fields:
    - first_name (CharField): The first name of the user.
    - last_name (CharField): The last name of the user.
    - profile_picture (ImageField): The profile picture of the user.
    - gender (CharField): The gender of the user.
    - user (OneToOneField): The associated user.

    Constants:
    - FIRST_NAME_MAX_LEN (int): Maximum length for the first name.
    - FIRST_NAME_MIN_LEN (int): Minimum length for the first name.
    - LAST_NAME_MAX_LEN (int): Maximum length for the last name.
    - LAST_NAME_MIN_LEN (int): Minimum length for the last name.

    Methods:
    - __str__: Human-readable representation of the user profile.
    """

    FIRST_NAME_MAX_LEN = 20
    FIRST_NAME_MIN_LEN = 2
    LAST_NAME_MAX_LEN = 20
    LAST_NAME_MIN_LEN = 2

    first_name = models.CharField(
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LEN),
            MaxLengthValidator(FIRST_NAME_MAX_LEN),
        ),
        max_length=FIRST_NAME_MAX_LEN,
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LEN),
            MaxLengthValidator(LAST_NAME_MAX_LEN),
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
        """
        Human-readable representation of the user.

        Returns:
        - str: A string representation of the user.
        """
        return f'Username: {CustomUser.objects.get(id=self.pk)}'
