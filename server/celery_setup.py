import os

from django.conf import settings
from django.core.wsgi import get_wsgi_application
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')
settings.configure()

# Initialize Celery instance
app = Celery('server')
app.config_from_object(settings, namespace='CELERY')
app.autodiscover_tasks()

# Load Django application
application = get_wsgi_application()

