from rest_framework import serializers
from .models import Order, Review, complete, Tracking
from apps.users.serializers import UserSerializer

class OrderSerializer(serializers.ModelSerializer):
    service_name = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ('user',)
    
    # for Getting Services Name
    def get_service_name(self, obj):
        return str(obj.service.name)
    
    # define user for order
    def create(self, validated_data):
        validated_data['user'] = self.context.get('request').user
        return super().create(validated_data)
    
    
#  Review for Ordering

class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields  =('user',)
    
    def validate(self, attrs):
        if attrs.get('order').order_status != complete:
            raise serializers.ValidationError(detail={'detail': "can't allow to create review for non-complete order"})
        return super().validate(attrs)
    
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
    
    
    
# Create Tracking Serializer
class TrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tracking
        fields = ['descriptions','icons','status']