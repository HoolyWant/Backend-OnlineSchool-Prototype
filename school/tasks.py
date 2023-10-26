from datetime import datetime

from celery import shared_task
from dateutil.relativedelta import relativedelta
from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER
from users.models import User


@shared_task
def send_update(followers_email_list: list, program_title: str) -> None:
    send_mail(
        f'Hello, student!',
        f'Your studing program {program_title} has been updated!',
        EMAIL_HOST_USER,
        followers_email_list,
    )


@shared_task
def check_user_activity() -> None:
    users = User.objects.all()
    for user in users:
        month = user.last_login + relativedelta(months=1)
        email_list = []
        if user.is_active and datetime.now() >= month:
            user.is_active = False
            email_list.append(user.email)
        send_mail(
            'Dear, student',
            'Your account now is not active(\nPlease, reply this message'
            ' to be active again <3',
            EMAIL_HOST_USER,
            email_list
        )


