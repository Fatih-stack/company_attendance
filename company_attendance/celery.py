# Celery Konfigürasyonu (company_attendance/celery.py)
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
import multiprocessing

multiprocessing.set_start_method('spawn', force=True)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'company_attendance.settings')

app = Celery('company_attendance')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)