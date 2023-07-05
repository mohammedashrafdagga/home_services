from django.db import models
from apps.services.models import Services
from django.contrib.auth.models import User

under_review = 'قيد المراجعة'
underway = 'قيد التنفيذ'
complete = 'مكتمل'
    
# Creating Order Model
class Order(models.Model):

    
    ORDER_STATUS = (
        (under_review, under_review),
        (underway, under_review),
        (complete, complete)
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
    
