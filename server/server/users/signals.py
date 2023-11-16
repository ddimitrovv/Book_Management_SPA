from django.db.models.signals import post_save
from django.dispatch import receiver

from rest_framework.authtoken.models import Token

from server.users.models import CustomUser, UserProfile

from .tasks import send_registration_email_async


@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=CustomUser)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


@receiver(post_save, sender=CustomUser)
def send_registration_email(sender, instance, created, **kwargs):
    if created:
        subject = 'Welcome to Your App'
        message = 'Thank you for registering!'
        from_email = 'your_email@gmail.com'
        recipient_list = [instance.email]
        send_registration_email_async.delay(subject, message, from_email, recipient_list)


# @shared_task
# def send_registration_email_async(subject, message, from_email, recipient_list):
#     send_mail(subject, message, from_email, recipient_list)
