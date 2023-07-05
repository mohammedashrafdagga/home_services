import random
from .models import CodeActivate
from .email_message import (
    send_activation_email, send_activation_thank_email,
    reset_password_code_email, send_emailing_change_email, send_successfully_change_email)
from apps.users.models import Profile
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

# Generate Activation Code for User
def generate_activation_code(user):
    code = ""
    for _ in range(5):
        digit = random.randint(0, 9)
        code += str(digit)

    return code
    
# Check Code Activation For user
def check_activation_code( code):
    active_code = CodeActivate.objects.filter(code = code).last()
    if active_code is not None:
        user = active_code.user
        CodeActivate.objects.filter(user = user).all().delete()
        return user
    return None

def create_activation_code(user):
    code = generate_activation_code(user = user)
    CodeActivate.objects.create(user = user, code = code)
    send_activation_email(content = {'email': user.email, 'code': code})
    
    
def activate_account(user):
    user.is_active = True
    user.save()
    Profile.objects.create(user = user)
    send_activation_thank_email(content = {'email': user.email})
    
# Delete all Token for User
def delete_token(user):
    token = Token.objects.filter(user = user).all()
    if token:
        token.delete()

# rest password request
def rest_password_request(email: str):
    user = User.objects.get(email = email)
    delete_token(user=user)
    code = generate_activation_code(user)
    CodeActivate.objects.create(user = user, code = code)
    reset_password_code_email(content = {'email': user, 'code': code})
    
    
def generate_token(user):
    token,created=Token.objects.get_or_create(user=user)
    return token.key

def get_user_by_token(key_token:str):
    user = Token.objects.get(key = key_token).user
    Token.objects.get(key = key_token)
    return user


def send_change_email(context):
    code = generate_activation_code(user = context['user'])
    CodeActivate.objects.create(user = context['user'], code = code)
    send_emailing_change_email(content = {'email': context['new_email'], 'code': code})
    
