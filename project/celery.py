from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

# create a Celery instance
celery_app = Celery('request')

# the configuration object to child processes.
celery_app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app project.
celery_app.autodiscover_tasks()
