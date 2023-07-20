from django.contrib import admin
from .models import Order, Review, Tracking

# register Order for admin
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user','service','order_status']
    list_editable = ['order_status']
    
    
admin.site.register(Review)


@admin.register(Tracking)
class TrackingAdmin(admin.ModelAdmin):
    list_display = ['id', 'order','descriptions', 'icons']