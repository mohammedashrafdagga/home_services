from django.db import models
from django.contrib.auth.models import User


# Notification Model
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
   
    
    class Meta:
        ordering = ('create_at',)
        
    def __str__(self):
        return self.message