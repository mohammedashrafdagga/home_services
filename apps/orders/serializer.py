from rest_framework import serializers
from .models import Order, CustomOrder, Notification


class OrderSerializer(serializers.ModelSerializer):
    service_name = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ('create_by',)
    
    def get_service_name(self, obj):
        return str(obj.service.name)
    
    def get_total_price(self, obj):
        return obj.quantity * obj.product.price
       
    def create(self, validated_data):
        user = self.context.get('request').user
        validated_data['create_by'] = user
        order = super().create(validated_data)
        Notification.objects.create(
            user = user,
            order = order,
            order_status = validated_data['order_status'],
            text = f"تم طلب الخدمة ' {order.service.name} ' بنجاح"
        )
        return order
    


class CustomOrderSerializer(serializers.ModelSerializer):
    service_name = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = CustomOrder
        fields = '__all__'
        read_only_fields = ('create_by',)
    
    def get_service_name(self, obj):
        return "خدمة مخصصة"
    
    def get_total_price(self, obj):
        return obj.quantity * obj.product.price
       
       
class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ('id','text', 'order_status')
    