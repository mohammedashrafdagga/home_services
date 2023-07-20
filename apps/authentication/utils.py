from .email_message import reset_password_code_email
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
import threading
from django.utils.deprecation import MiddlewareMixin
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse



# Delete all Token for User
def delete_token(user):
    token = Token.objects.filter(user = user).all()
    if token:
        token.delete()

# rest password request
def rest_password_request(request, email: str):
    # get user with delete all token have
    user = User.objects.get(email = email)
    delete_token(user=user)
    
    # create new token with get domain for rest password
    token = Token.objects.create(user = user)
    domain = get_current_site(request=request).domain
    rest_password_url = f"http://{domain}{reverse('authentication:rest-password-verify')}?token={token.key}"
    
    # send email for rest password
    reset_password_code_email(content = {'email': user.email, 'rest_password_url': rest_password_url})



def get_user_by_token(key_token:str):
    user = Token.objects.get(key = key_token).user
    Token.objects.filter(key = key_token).delete()
    return user


# Create thread-local storage
_thread_locals = threading.local()

def get_current_request():
    return getattr(_thread_locals, "request", None)

def set_current_request(request):
    _thread_locals.request = request


# utils.py
class RequestMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Set the current request in thread-local storage
        set_current_request(request)
