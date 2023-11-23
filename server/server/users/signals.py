from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
import secrets

from rest_framework.authtoken.models import Token

from server.users.models import CustomUser, UserProfile

from .tasks import send_registration_email_async


@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Signal handler to create a user profile when a CustomUser is created.

    :param sender: The sender of the signal.
    :param instance: The instance of the CustomUser model.
    :param created: A boolean indicating whether the instance was created.
    :param kwargs: Additional keyword arguments.
    """

    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=CustomUser)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    """
    Signal handler to create an authentication token when a CustomUser is created.

    :param sender: The sender of the signal.
    :param instance: The instance of the CustomUser model.
    :param created: A boolean indicating whether the instance was created.
    :param kwargs: Additional keyword arguments.
    """

    if created:
        Token.objects.create(user=instance)


@receiver(post_save, sender=CustomUser)
def send_registration_email(sender, instance, created, **kwargs):
    """
    Signal handler to send a registration email when a CustomUser is created.

    :param sender: The sender of the signal.
    :param instance: The instance of the CustomUser model.
    :param created: A boolean indicating whether the instance was created.
    :param kwargs: Additional keyword arguments.
    """

    if created:
        """Generate a unique confirmation token"""
        confirmation_token = secrets.token_urlsafe(30)

        """Save the token in the user model"""
        instance.confirmation_token = confirmation_token
        instance.save()

        subject = 'Welcome to Your App'
        message = (f'Thank you for registering!\n\n Please click the link below to confirm your email:'
                   f'\n{settings.BASE_URL}/users/confirm-email/{confirmation_token}/')
        from_email = 'your_email@gmail.com'
        recipient_list = [instance.email]
        send_registration_email_async.delay(subject, message, from_email, recipient_list)
