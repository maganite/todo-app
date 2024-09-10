from celery import shared_task
from django.core.mail import send_mail
from project import settings
from .models import Todo
from datetime import datetime, timezone, timedelta
from pytz import timezone

@shared_task(bind=True)
def check_reminder(self):
    now=datetime.now(timezone("Asia/Kolkata"))

    todo_obj=Todo.objects.filter(id=15).first()
    reminder_time=todo_obj.reminder_time
    time_diff = reminder_time - now
    margin = timedelta(seconds=10)
    if timedelta(minutes=5) - margin <= time_diff <= timedelta(minutes=5) + margin:
        print(time_diff)
        send_reminder_mail.delay(todo_obj.id)
        print("sent")
    else:
        print(f"time left for reminder{reminder_time-now}")

@shared_task
def send_reminder_mail(idd):
    todo_obj=Todo.objects.filter(id=idd).first()
    mail_subject = f"reminder for {todo_obj.title}"
    mail_message = f"5 minutes left for this todo {todo_obj.title}"
    from_user = settings.EMAIL_HOST_USER
    to_user = settings.EMAIL_HOST_USER

    send_mail(
    subject=mail_subject,
    message=mail_message,
    from_email=from_user,
    recipient_list=[to_user]
    )
    print("the mail have been sent successfully")
    return "done the work"

