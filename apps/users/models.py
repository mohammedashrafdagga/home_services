from django.db import models
from django.contrib.auth.models import User
from apps.services.models import Category
from django.utils.timezone import now


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(upload_to='profile_images', default='profile_images/placeholder.jpg', help_text='صورة شخصية')

    def __str__(self):
        return self.user.username

class Location(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='locations')
    address_name = models.CharField(max_length=250)
    country = models.CharField(max_length=100, default='فلسطين')
    city = models.CharField(max_length=100, help_text='المدينة')
    building = models.CharField(max_length=100, help_text='البناية')
    apartment_number = models.CharField(max_length=20, help_text='رقم الشقة')
    phone_number = models.CharField(max_length=20, help_text='رقم الهاتف')

    def __str__(self):
        return self.address_name


class ChangeEmail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='emails')
    new_email = models.EmailField()
    
    def __str__(self):
        return self.new_email
