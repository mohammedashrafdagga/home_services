from django.db import models
from django.contrib.auth.models import User
from apps.services.models import Category
from django.utils.timezone import now


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


class ChangeEmail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='emails')
    new_email = models.EmailField()
    
    def __str__(self):
        return self.new_email
    
# (name, email, phone_number, location, category, year_experience, explain_experience, additional)
class ServiceProvider(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=180)
    phone_number = models.CharField(max_length=15)
    location = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    year_experience = models.IntegerField()
    summary_experience = models.CharField(max_length=250)
    additional = models.TextField(null=True, blank=True)
    
    
    def __str__(self):
        return self.name
    

class CustomServices(models.Model):
    request_by = models.ForeignKey(User, related_name='custom_services', on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    category = models.ForeignKey(Category, models.CASCADE)
    descriptions = models.TextField(null=True, blank=True)    
    request_date = models.DateField(default=now)
    request_time = models.TimeField()
    location = models.OneToOneField(Location, on_delete=models.CASCADE)

    def __str__(self):
        return f'custom order services for {self.request_by.username}'
    
    