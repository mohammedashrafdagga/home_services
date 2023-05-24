from .models import Category, Services
from rest_framework import serializers
from urllib.parse import quote
from django.urls import reverse

class ServicesCategorySerializer(serializers.ModelSerializer):  
    class Meta:
        model = Services
        fields = ('name', 'price_from', 'price_to')
    


class CategorySerializer(serializers.ModelSerializer):
    count_services = serializers.SerializerMethodField(read_only=True)
    category_services = serializers.HyperlinkedIdentityField(read_only=True,
                                                             view_name='services:category-detail',
                                                             lookup_field = 'id')

    class Meta:
        model = Category
        fields = ('name', 'count_services',  'category_services')
        
        
    def get_count_services(self, obj):
        return obj.services.count()


class CategoryWithServicesSerializer(serializers.ModelSerializer):
    services = ServicesCategorySerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ('name',  'services')
        
        
