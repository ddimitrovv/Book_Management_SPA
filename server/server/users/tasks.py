from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_registration_email_async(subject, message, from_email, recipient_list):
    """
    Celery task to send a registration email.

    Parameters:
    - subject (str): The subject of the email.
    - message (str): The message content of the email.
    - from_email (str): The sender's email address.
    - recipient_list (list): A list of recipient email addresses.

    Returns:
    - dict: A dictionary containing the status and a message indicating the result of the email sending attempt.
      Example: {'status': 'success', 'message': 'Email sent successfully to user@example.com.'}
             or {'status': 'error', 'message': 'Error sending email: <error_message>'}
    """

    try:
        send_mail(subject, message, from_email, recipient_list)
        return {'status': 'success', 'message': f'Email sent successfully to {recipient_list[0]}.'}
    except Exception as e:
        return {'status': 'error', 'message': f'Error sending email: {str(e)}'}
