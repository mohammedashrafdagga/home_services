from django.db import models
from django.contrib.auth.models import User
from apps.services.models import Services

# Create your models here.
class Review(models.Model):
    user = models.ForeignKey(User, related_name='reviews',on_delete=models.CASCADE)
    service = models.ForeignKey(Services, related_name='reviews', on_delete=models.CASCADE)
    review = models.PositiveSmallIntegerField()
    comment = models.TextField(blank=True, null=True)
    
    # created at & implementation at
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return f'review: {self.review}'