"""Celery Setup Module

This module is responsible for setting up Celery within the Django project.
It configures the Celery instance based on the project's settings and autodiscovers tasks.

Note: This script should be executed to initialize Celery before running tasks.

Example:
    $ celery -A server worker -l info

"""

import os

from django.conf import settings
from django.core.wsgi import get_wsgi_application
from celery import Celery


# Set the DJANGO_SETTINGS_MODULE environment variable to the project's settings module.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')
settings.configure()

# Initialize Celery instance
app = Celery('server')
app.config_from_object(settings, namespace='CELERY')
app.autodiscover_tasks()

# Load Django application
application = get_wsgi_application()

