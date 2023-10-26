from celery import shared_task
from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER


@shared_task
def send_update(followers_email_list: list, program_title: str) -> None:
    send_mail(
        f'Hello, student!',
        f'Your studing program {program_title} has been updated!',
        EMAIL_HOST_USER,
        followers_email_list,
    )
