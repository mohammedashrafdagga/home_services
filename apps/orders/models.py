from django.db import models
from apps.services.models import Services
from apps.users.models import  Location
from django.contrib.auth.models import User

under_review = 'قيد المراجعة'
underway = 'قيد التنفيذ'
complete = 'مكتمل'
rejected = 'مرفوض'

ORDER_STATUS = (
    (under_review, under_review),
    (underway, underway),
    (complete, complete),
    (rejected, rejected)
)


# Creating Order Model
class Order(models.Model):
    user = models.ForeignKey(User, related_name='orders', on_delete=models.SET_NULL, null=True, blank=True)
    service = models.ForeignKey(Services, related_name='orders', on_delete=models.CASCADE)
    order_status = models.CharField(max_length=12, choices=ORDER_STATUS, default=under_review)
    
    # Delivery Date and time
    delivery_date = models.DateField()
    delivery_time = models.TimeField()
    
    # location for user create order to delivery on.
    user_location= models.ForeignKey(Location, models.SET_NULL, null=True, blank=True)
    
    # Time the Order create on.
    order_create = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f'طلب خدمة {self.service} بتاريخ {self.order_create.date()}'
    

# # Create your models here.
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
    # Order related with review
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    rating = models.CharField(choices=RATING_CHOICES,default='1')
    comment = models.TextField(null=True, blank=True)
    
    # created at & implementation at
    create_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f'review: {self.rating}'