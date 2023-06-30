from rest_framework import serializers
from .models import Location, Profile
from django.conf import settings
import os

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
    
    
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['image']
    
    def save(self, **kwargs):
        # get image and user
        image = self.validated_data.get('image')
        user = self.context.get('user')

        # if user already Have a image profile - remove
        if user.profile.image:
            existing_image_path = user.profile.image.path
            if os.path.exists(existing_image_path):
                os.remove(existing_image_path)
        
        # save new image with rename image
        user.profile.image = image
        user.profile.image.name = f'{user.username}.jpg'
        user.profile.save()
    
        
        return user.profile
    
