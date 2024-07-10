from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send(data):
    send_mail(
        data['subject'],
        data['message'],
        settings.EMAIL_HOST_USER,
        recipient_list=[data['recipient']]
    )