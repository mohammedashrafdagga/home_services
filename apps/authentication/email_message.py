# Here We Have Message foe Email
from .tasks import send_email_message
from typing import Dict


# sending activation email
def send_activation_email(content: Dict):
    context = {
        'email_to': [content['email']], 'template_name':  'email_message/activate_account.html',
        'message_context': {'title': 'Activate User Account',
                            'activate_link': content['activate_link'], 'name': content['name']}}
    send_email_message.delay(context=context)

# sending email for successfully activate account into user


def send_activation_thank_email(content):
    context = {
        'template_name': 'email_message/is_activate.html', 'email_to': [content['email']],
        'message_context': {'title': 'Thank for Activation your Account', 'name': content['name']}}
    send_email_message.delay(context=context)


# sending email for Changing Password successfully message
def send_change_password_email(content):
    context = {
        'template_name': 'email_message/change_password.html', 'email_to': [content['email']],
        'message_context': {'title': 'Update User password', 'name': content['name']}
    }
    send_email_message.delay(context=context)

# sending email for resend Code for rest password


def reset_password_code_email(content: Dict):
    context = {
        'template_name':  'email_message/reset_password.html', 'email_to': [content['email']],
        'message_context': {'title': 'Confirm Reset Password Links',
                            "rest_password_url": content['rest_password_url'], 'name': content['name']}}
    send_email_message.delay(context=context)


def send_successfully_change_email(content: Dict):
    context = {
        'template_name':  'email_message/change_successfully_email.html', 'email_to': [content['email']],
        'message_context': {'title': 'Your Change Email Successfully'}}
    send_email_message.delay(context=context)
