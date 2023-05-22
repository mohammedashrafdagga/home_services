from django.db import models
from django.contrib.auth.models import User


class CodeActivate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=5)
    
    def __str__(self):
        return self.code