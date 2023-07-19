from django.db import models
from django.contrib.auth.models import User

# Code Activate Model
class CodeActivate(models.Model):
    STATUS_CHOICES = (
        ('rest_password','rest_password'),
        ('verify_account','verify_account')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=5)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='verify_account')
    
    def __str__(self):
        return self.code