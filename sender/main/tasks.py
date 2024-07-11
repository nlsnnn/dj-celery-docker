from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send(data):
    send_mail(
        data['subject'],
        data['message'],
        settings.EMAIL_HOST_USER,
        recipient_list=[data['recipient']],
        fail_silently=False
    )


@shared_task
def subscription_register(data):
    send_mail(
        subject='Подписка на рассылку',
        message='Спасибо что подписались на рассылку! Теперь мы будем спамить вам каждый день',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[data['email']],
        fail_silently=False
    )


@shared_task
def subscription_sending(data, emails):
    send_mail(
        data['subject'],
        data['message'],
        settings.EMAIL_HOST_USER,
        recipient_list=emails,
        fail_silently=False
    )