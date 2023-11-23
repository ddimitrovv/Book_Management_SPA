"""Celery Initialization Module

This module initializes the Celery instance for the Django project.
It configures Celery based on the project's settings and autodiscovers tasks.

Note: This script should be executed to initialize Celery before running tasks.

Example:
    $ celery -A server worker -l info

"""

from celery import Celery
from django.conf import settings

# Create Celery instance
app = Celery('server')

# Configure Celery with Django settings
app.config_from_object(settings, namespace='CELERY')

# Autodiscover tasks from installed apps
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
