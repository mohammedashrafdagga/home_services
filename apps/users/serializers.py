from rest_framework import serializers
from .models import Location, Profile
from django.contrib.auth.models import User
import os

# Location Serializer 
class LocationSerializer(serializers.ModelSerializer):
    detail = serializers.HyperlinkedIdentityField(
        read_only=True,
        view_name='users:get-update-delete-location',
        lookup_field = 'id',lookup_url_kwarg = 'location_id'
        )
    class Meta:
        model = Location
        fields = '__all__'
        read_only_fields = ('user','detail',)

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().update(instance, validated_data)
    
    
# Profile User      
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['image']
        read_only_fields = ('user',)
    
    
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
        
# Related With Reviews 
class UserSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = ('first_name','last_name', 'image')
    
    def get_image(self, obj):
        return obj.profile.image.url
 
# For editing only firstname and lastname
class EditUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', )
        
# Related with Settings Pages
class UserInformationSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'image',)
    
    def get_image(self, obj):
        return obj.profile.image.url
