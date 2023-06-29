from rest_framework import serializers
from .models import Location

class LocationSerializer(serializers.ModelSerializer):
    detail = serializers.HyperlinkedIdentityField(read_only=True,
                                                  view_name='users:get-update-delete-location',
                                                  lookup_field = 'id',
                                                  lookup_url_kwarg = 'location_id')

    class Meta:
        model = Location
        fields = '__all__'
        read_only_fields = ('user','detail',)
        #fields = ['id', 'user', 'country', 'city', 'building', 'apartment_number', 'phone_number']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().update(instance, validated_data)