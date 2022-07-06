from config import settings
from decouple import config

from celery import Celery

app = Celery('gsheets')

obj = config('GSHEETS_SETTINGS', settings)
app.config_from_object(obj, namespace='gsheets')

app.autodiscover_tasks()
