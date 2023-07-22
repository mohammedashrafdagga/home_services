from .models import Category, Services
from rest_framework import serializers
from apps.orders.serializer import ReviewSerializer


class CategorySerializer(serializers.ModelSerializer):
    count_services = serializers.SerializerMethodField(read_only=True)
    category_services = serializers.HyperlinkedIdentityField(
        read_only=True, view_name='services:category-detail', lookup_field = 'id')

    class Meta:
        model = Category
        fields = ('id','name','icon', 'count_services',  'category_services',)
        
        
    def get_count_services(self, obj):
        return obj.services.count()

    # create category 
    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        return super().create(validated_data)


class ServicesSerializer(serializers.ModelSerializer):  
    detail = serializers.HyperlinkedIdentityField(
        read_only=True,
        view_name='services:detail',
        lookup_field = 'id'
    )
    reviews = ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = Services
        fields = ('name','category','content','reviews','detail',)
        read_only_fields = ('user','image',)
