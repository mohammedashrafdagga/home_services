# Here We Have Message foe Email
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string


def send_activation_email(user, activation_code):
    
    '''
        This for Sending Message Contains Activation Code for the User
    '''
    template = 'email_message/activate_code.html'
    subject = 'Account Activation'
    context = {
        "title": subject,
        "activation_code": activation_code
    }
    html_content = render_to_string(template, context)
    from_email = settings.EMAIL_HOST_USER
    to_email = user.email
    send_mail(subject, message='', from_email=from_email, recipient_list=[to_email], html_message=html_content)




def thank_activation_email(user):
    
    '''
        This for Sending Message For thank User for Activate Account
    '''
    template = 'email_message/is_activate.html'
    subject = 'Thank for activation your account '
    context = {
        "title": subject,
    }
    html_content = render_to_string(template, context)
    from_email = settings.EMAIL_HOST_USER
    to_email = user.email
    send_mail(subject, message='', from_email=from_email, recipient_list=[to_email], html_message=html_content)

def resend_activation_email(user, activation_code):
    
    '''
        This for Sending Message Contains Activation Code for the User
    '''
    template = 'email_message/activate_code.html'
    subject = 'Resend Code for Account Activation'
    context = {
        "title": subject,
        "activation_code": activation_code
    }
    html_content = render_to_string(template, context)
    from_email = settings.EMAIL_HOST_USER
    to_email = user.email
    send_mail(subject, message='', from_email=from_email, recipient_list=[to_email], html_message=html_content)

def change_password_email(user):
    '''
        Change Password Successfully sending email
    '''
    template = 'email_message/change_password.html'
    subject = 'Change Password Successfully'
    html_content = render_to_string(template, {
        "title": subject
    })
    from_email = settings.EMAIL_HOST_USER
    to_email = user.email
    send_mail(subject, message='', from_email=from_email, recipient_list=[to_email], html_message=html_content)


def reset_password_code_email(email, reset_password_code):
    
    '''
        This for Sending Message Contains resetpassword Code for the User
    '''
    template = 'email_message/reset_password.html'
    subject = 'Resend Code for reset password'
    context = {
        "title": subject,
        "reset_password_code": reset_password_code
    }
    html_content = render_to_string(template, context)
    from_email = settings.EMAIL_HOST_USER
    to_email = email
    send_mail(subject, message='', from_email=from_email, recipient_list=[to_email], html_message=html_content)