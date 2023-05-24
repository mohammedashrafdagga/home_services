from django.db import models
from django.contrib.auth.models import User


# Category Model
class Category(models.Model):
    created_by = models.ForeignKey(User,
                                   on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=20, unique=True)
    slug = models.CharField(max_length=20, null=True, blank=True)
    
    create_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name


class Services(models.Model):
    created_by = models.ForeignKey(User,
                                   on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(Category, related_name='services' ,on_delete=models.SET_NULL, null=True, blank=True)

    # name with slug
    name = models.CharField(max_length=255, unique=True)
    name_en = models.CharField(max_length=255, null=True, blank=True)
    slug = models.CharField(max_length=255, null=True, blank=True)
    
    # price
    price_from = models.PositiveIntegerField(default=30)
    price_to = models.PositiveIntegerField(default=50)
    
    # is active
    is_active = models.BooleanField(default=True)
    
    # date for services
    create_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.name
    
    
    
class IncludeServices(models.Model):
    services = models.ForeignKey(Services,related_name='include_services',
                                 on_delete=models.SET_NULL, null=True, blank=True)
    descriptions = models.CharField(max_length=255)
    
    def __str__(self):
        return self.descriptions
    
    
    
class NotIncludeServices(models.Model):
    services = models.ForeignKey(Services,related_name='not_include_services',
                                 on_delete=models.SET_NULL, null=True, blank=True)
    descriptions = models.CharField(max_length=255)
    
    def __str__(self):
        return self.descriptions