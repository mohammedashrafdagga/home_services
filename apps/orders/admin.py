from django.contrib import admin
from .models import Order, CustomOrder

# register Order for admin
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'create_by','service','order_status','quantity']
    list_editable = ['order_status']
    
    
@admin.register(CustomOrder)
class CustomOrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'create_by','service','order_status','quantity']
    list_editable = ['order_status']