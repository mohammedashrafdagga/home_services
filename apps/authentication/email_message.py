# Here We Have Message foe Email
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from typing import Dict


def email_sending(context:Dict):
    message = render_to_string(template_name=context['template_name'], context=context['message_context'])
    send_mail(context['message_context']['title'], message='', from_email=settings.EMAIL_HOST_USER,
              recipient_list=context['email_to'], html_message=message)
    

# sending activation email
def send_activation_email(content:Dict):
    context =  {
    'email_to': [content['email']], 'template_name':  'email_message/activate_account.html',
    'message_context': {'title': 'Code for activate you account','activate_link': content['activate_link']}}
    email_sending(context=context)

# sending email for successfully activate account into user
def send_activation_thank_email(content):
    context =  {
    'template_name': 'email_message/is_activate.html','email_to': [content['email']],
    'message_context': {'title': 'Thank for Activation your Account'}}
    email_sending(context=context)


# sending email for Changing Password successfully message 
def send_change_password_email(content):
    context =  {
    'template_name': 'email_message/change_password.html', 'email_to': [content['email']],
    'message_context': {'title': 'Change Password is Update Successfully'}
    }
    email_sending(context=context)

# sending email for resend Code for rest password
def reset_password_code_email(content:Dict):
    context =  {
    'template_name':  'email_message/reset_password.html', 'email_to': [content['email']],
    'message_context': {'title': 'resend Code for apply to reset password', "rest_password_url": content['rest_password_url']}}
    email_sending(context=context)
    

    
def send_successfully_change_email(content:Dict):
    context =  {
    'template_name':  'email_message/change_successfully_email.html', 'email_to': [content['email']],
    'message_context': {'title': 'Your Change Email Successfully'}}
    email_sending(context=context)