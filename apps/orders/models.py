from django.db import models
from apps.services.models import Services
from apps.users.models import CustomServices
from django.contrib.auth.models import User

under_review = 'قيد المراجعة'
underway = 'قيد التنفيذ'
complete = 'مكتمل'
rejected = 'مرفوض'
    
# Creating Order Model
class Order(models.Model):

    
    ORDER_STATUS = (
        (under_review, under_review),
        (underway, underway),
        (complete, complete),
        (rejected, rejected)
    )
    create_by = models.ForeignKey(User, related_name='orders',
                                  on_delete=models.SET_NULL, null=True, blank=True)
    
    service = models.ForeignKey(Services, related_name='orders', on_delete=models.SET_NULL, 
                                null=True, blank=True)
    
    order_status = models.CharField(max_length=12, choices=ORDER_STATUS, default=under_review)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.PositiveIntegerField(null=True, blank=True)
    
    date_order = models.DateField()
    time_order = models.TimeField()
    
    # created at & implementation at
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return f'طلب خدمة {self.service} بتاريخ {self.date_order}'
    

 
# Creating Order Model
class CustomOrder(models.Model):

    
    ORDER_STATUS = (
        (under_review, under_review),
        (underway, underway),
        (complete, complete),
        (rejected,rejected)
    )
    create_by = models.ForeignKey(User, related_name='custom_orders',
                                  on_delete=models.SET_NULL, null=True, blank=True)
    
    service = models.ForeignKey(CustomServices, related_name='custom_orders', on_delete=models.SET_NULL, 
                                null=True, blank=True)
    
    order_status = models.CharField(max_length=12, choices=ORDER_STATUS, default=under_review)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.PositiveIntegerField(null=True, blank=True)
    
    date_order = models.DateField()
    time_order = models.TimeField()
    
    # created at & implementation at
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return f'طلب خدمة {self.service} بتاريخ {self.date_order}'
    

class Notification(models.Model):
    NOTIFICATION_STATUS = (
        ('غير مقروءة', 'غير مقروءة'),
        ('مقروءة','مقروءة')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    order = models.ForeignKey(Order, on_delete=models.CASCADE,null=True, blank=True, related_name='notifications')
    custom_order = models.ForeignKey(CustomOrder, on_delete=models.CASCADE,null=True, blank=True, related_name='notifications')
    text = models.TextField()
    order_status = models.CharField(max_length=15)
    status = models.CharField(default='غير مقروءة', max_length=10, choices=NOTIFICATION_STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.text
    
    class Meta:
        ordering = ('-create_at',)