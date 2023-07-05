from django.db import models
from django.contrib.auth.models import User
from apps.services.models import Services

# Create your models here.
class Review(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    user = models.ForeignKey(User, related_name='reviews',on_delete=models.CASCADE)
    service = models.ForeignKey(Services, related_name='reviews', on_delete=models.CASCADE)
    review = models.IntegerField(choices=RATING_CHOICES,default=1)
    comment = models.TextField(blank=True, null=True)
    
    # created at & implementation at
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return f'review: {self.review}'