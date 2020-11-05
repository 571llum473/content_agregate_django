import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cntnt_agrgtr.settings')
 
app = Celery('get_cntnt')
app.config_from_object('django.conf:settings')
 
# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
 
app.conf.beat_schedule = {
    'scrape': {
        'task': 'get_cntnt.tasks.scrape',
        'schedule': crontab(),  # change to `crontab(minute=0, hour=0)` if you want it to run daily at midnight
    },
}