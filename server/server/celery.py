from celery import Celery
from django.conf import settings


app = Celery('server')
app.config_from_object(settings, namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
