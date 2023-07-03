from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ('create_by',)
    
    def get_total_price(self, obj):
        return obj.quantity * obj.product.price
       
    def create(self, validated_data):
        user = self.context.get('request').user
        validated_data['create_by'] = user
        return super().create(validated_data)