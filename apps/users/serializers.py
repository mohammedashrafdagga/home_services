from rest_framework import serializers
from .models import Location, Profile, CustomServices, ServiceProvider
from django.contrib.auth.models import User
import os

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
        fields = '__all__'
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
        
class UserSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = ('first_name','last_name', 'image')
    
    def get_image(self, obj):
        return obj.profile.image.url
    
class PasswordSerializer(serializers.Serializer):
    password = serializers.CharField(required=True, write_only=True)

    def validate_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError(detail='خطا في إدخال كلمة المرور')
        return value


class ChangeEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True, write_only=True)
    
    def validate(self, data):
        user = User.objects.filter(email = data.get('email')).first()
        if user is not None:
            raise serializers.ValidationError(detail={'detail': 'هذا الإيميل موجود بالفعل ,قمت بتجربة أخر'})
        return data
    
class EditUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', )
        
        

class CustomServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomServices
        fields ='__all__'
        read_only_fields = ('request_by',)
        
        
class ServiceProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceProvider
        fields = '__all__'
        read_only_fields = ('user',)