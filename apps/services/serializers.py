from .models import Category, Services, IncludeServices, NotIncludeServices
from rest_framework import serializers

class ServicesCategorySerializer(serializers.ModelSerializer):  
    detail = serializers.HyperlinkedIdentityField(read_only=True, view_name='services:detail',lookup_field = 'id')
    class Meta:
        model = Services
        fields = ('name', 'image', 'price_from', 'price_to', 'detail',)
    


class CategorySerializer(serializers.ModelSerializer):
    count_services = serializers.SerializerMethodField(read_only=True)
    category_services = serializers.HyperlinkedIdentityField(read_only=True,
                                                             view_name='services:category-detail',
                                                             lookup_field = 'id')

    class Meta:
        model = Category
        fields = ('name','icon', 'count_services',  'category_services',)
        
        
    def get_count_services(self, obj):
        return obj.services.count()


class CategoryWithServicesSerializer(serializers.ModelSerializer):
    services = ServicesCategorySerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ('name', 'icon', 'services',)
        
        

class IncludeServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncludeServices
        fields = ('descriptions',)
        
class NotIncludeServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotIncludeServices
        fields = ('descriptions',)
        

class ServicesSerializer(serializers.ModelSerializer):
    include_services = IncludeServicesSerializer(many=True, read_only=True)
    not_include_services = NotIncludeServicesSerializer(many=True, read_only=True)
    class Meta:
        model = Services
        fields = ('id','name','image' ,'price_from','price_to', 'include_services', 'not_include_services',)