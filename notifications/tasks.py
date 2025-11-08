from celery import shared_task
from tasks.models import Task
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
from django.core.mail import send_mail



@shared_task
def send_reminder_email(task_id):
    try:
        task = Task.objects.get(id=task_id)
        user_email = task.owner.email
        task_title = task.title

        subject = f'reminder {task_title}'
        message = (
            f'hello {task.owner.username}\n\n'
            f'you have this task {task_title}'
            f'good luck'
        )

        send_mail(
            subject,
            message,
            'noreply@taskflow.com',
            [user_email],
            fail_silently=False,
        )
        print(f'remdiner email for {task_title}to {user_email} send!')
    
    except Task.DoesNotExist:
        print('task id not found')

@shared_task
def check_upcoming_tasks():
    now = timezone()
    tomorrow = now + timedelta(days=1)
    upcoming_tasks = Task.objects.filter(
        due_date_gte=now,
        due_date_lt=tomorrow,
        status_in=['TODO','IN_PROGRESS']
    )
    print(f'{upcoming_tasks.count()} found!')
    for task in upcoming_tasks:
        send_reminder_email.delay(task.id)