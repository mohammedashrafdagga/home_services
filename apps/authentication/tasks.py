from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from celery import shared_task


@shared_task()
def send_email_message(context: dict):
    message = render_to_string(
        template_name=context['template_name'], context=context['message_context'])
    send_mail(context['message_context']['title'], message='', from_email=settings.EMAIL_HOST_USER,
              recipient_list=context['email_to'], html_message=message)
