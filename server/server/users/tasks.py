from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_registration_email_async(subject, message, from_email, recipient_list):
    try:
        send_mail(subject, message, from_email, recipient_list)
        return {'status': 'success', 'message': f'Email sent successfully to {recipient_list[0]}.'}
    except Exception as e:
        return {'status': 'error', 'message': f'Error sending email: {str(e)}'}
