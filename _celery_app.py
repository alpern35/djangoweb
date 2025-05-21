import os
from celery import Celery        # <- import from the library, not your file

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'site79084.settings')

app = Celery('site79084')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
