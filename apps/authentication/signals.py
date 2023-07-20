from django.db.models.signals import post_save
from django.urls import reverse
from django.dispatch import receiver
from django.contrib.auth.models import User
from apps.users.models import Profile
from .email_message import (
    send_activation_email,
    send_activation_thank_email
)
from django.contrib.sites.shortcuts import get_current_site
from .utils import get_current_request
from rest_framework.authtoken.models import Token


# create new User
@receiver(post_save, sender = User)
def user_post_save(sender, instance, created, **kwargs):
    if created:
        # create New Code Activation, 
        token = Token.objects.create(user = instance)
        request = get_current_request()
        domain = get_current_site(request=request).domain
        activate_link = f"http://{domain}{reverse('authentication:verify-account')}?token={token.key}"
        send_activation_email(content={'email': instance.email,'activate_link': activate_link})
        
    
    # when update user (for example verify Code)
    if instance.is_active:
        if not Profile.objects.filter(user = instance).exists():
            Profile.objects.create(user = instance)
            send_activation_thank_email(content = {'email': instance.email})
            


