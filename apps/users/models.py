from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(upload_to='profile_images', null=True, blank=True, help_text='صورة شخصية')

    def __str__(self):
        return self.user.username

class Location(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='locations')
    country = models.CharField(max_length=100, default='فلسطين')
    city = models.CharField(max_length=100, help_text='المدينة')
    building = models.CharField(max_length=100, help_text='البناية')
    apartment_number = models.CharField(max_length=20, help_text='رقم الشقة')
    phone_number = models.CharField(max_length=20, help_text='رقم الهاتف')

    def __str__(self):
        return f"{self.country}, {self.city}, {self.building}-{self.apartment_number}"
