import os
from celery import Celery
from celery.schedules import crontab

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
app = Celery('project')
app.conf.enable_utc = False

app.conf.update(timezone = 'Asia/kolkata')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.


app.config_from_object('django.conf:settings', namespace='CELERY')
# Load task modules from all registered Django app configs.


#for Scheduling tasks i.e (Celery Beat Settings)
app.conf.beat_schedule = {
'send-todo-reminder': {
    'task': 'todo.tasks.check_reminder',
    'schedule': crontab(minute='*'),
  },
}

app.autodiscover_tasks()
