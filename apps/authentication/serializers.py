from django.contrib.auth.models import User
from rest_framework import serializers
from .utils import generate_activation_code
from .email_message import send_activation_email
from django.contrib.auth.hashers import make_password



class UserRegistrationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    first_name = serializers.CharField(max_length = 100)
    last_name = serializers.CharField(max_length = 100)
    password = serializers.CharField(write_only=True, min_length=8)

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['email'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            is_active=False,
        )
        code = generate_activation_code(user = user)
        send_activation_email(user=user, activation_code=code)
        return user
    
    

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True, write_only=True)
    new_password1 = serializers.CharField(required=True, write_only=True)
    new_password2 = serializers.CharField(required=True, write_only=True)

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError('Invalid current password')
        return value

    def validate(self, data):
        new_password = data.get('new_password1')
        confirm_new_password = data.get('new_password2')
        if new_password != confirm_new_password:
            raise serializers.ValidationError('New password and confirmation do not match')
        return data

    def save(self):
        user = self.context['request'].user
        new_password = self.validated_data['new_password1']
        user.password = make_password(new_password)
        user.save()
        
# Change password for the user
class ResetPasswordSerializer(serializers.Serializer):
    new_password1 = serializers.CharField(required=True, write_only=True)
    new_password2 = serializers.CharField(required=True, write_only=True)

    def validate(self, data):
        new_password = data.get('new_password1')
        confirm_new_password = data.get('new_password2')
        if new_password != confirm_new_password:
            raise serializers.ValidationError('New password and confirmation do not match')
        return data

    def save(self):
        user = self.context['request'].user
        new_password = self.validated_data['new_password1']
        user.password = make_password(new_password)
        user.save()