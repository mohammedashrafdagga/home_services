from rest_framework import serializers
from .models import Order, CustomOrder


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
        return super().create(validated_data)
    


class CustomOrderSerializer(serializers.ModelSerializer):
    service_name = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = CustomOrder
        fields = '__all__'
        read_only_fields = ('create_by',)
    
    def get_service_name(self, obj):
        return str(obj.service.name)
    
    def get_total_price(self, obj):
        return obj.quantity * obj.product.price
       