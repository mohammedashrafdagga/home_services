from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import CodeActivate
from apps.users.models import Profile
from .utils import generate_activation_code
from .email_message import (send_activation_email, send_activation_thank_email, reset_password_code_email)


# create new User
@receiver(post_save, sender = User)
def user_post_save(sender, instance, created, **kwargs):
    if created:
        # create New Code Activation, 
        code = generate_activation_code()
        instance.is_active = False
        CodeActivate.objects.create(user = instance, code = code)
        
    
    # when update user (for example verify Code)
    if instance.is_active:
        if not Profile.objects.filter(user = instance).exists():
            Profile.objects.create(user = instance)
            send_activation_thank_email(content = {'email': instance.email})
            


# # when create Coed Activation that Mean Send Activation Code into User
@receiver(post_save, sender=CodeActivate)
def code_post_save(sender, instance, created, **kwargs):
    if created:
        if instance.status == 'verify_account':
            send_activation_email(content={'email': instance.user.email,'code': instance.code})
        else:
            reset_password_code_email(content = {'email': instance.user.email, 'code': instance.code})
