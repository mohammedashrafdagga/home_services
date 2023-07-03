from django.contrib.auth.models import User
from rest_framework import serializers
from .utils import generate_activation_code, check_activation_code
from .email_message import (
    send_activation_email, thank_activation_email,
    change_password_email,reset_password_code_email
)
from django.contrib.auth.hashers import make_password
from rest_framework.authtoken.models import Token
from .models import CodeActivate
from apps.users.models import Profile

'''
    User Register Serializer 
    - Take email, first_name, last_name, password
'''
class UserRegistrationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    first_name = serializers.CharField(max_length = 100)
    last_name = serializers.CharField(max_length = 100)
    password = serializers.CharField(write_only=True, min_length=8)


    def validate(self, attrs):
        try:
            user = User.objects.get(email = attrs.get('email'))
            if user.is_active:
                raise serializers.ValidationError(
                    {'detail': 'already exists, you can logging into system'}
                )
            if not user.is_active:
                raise serializers.ValidationError({'detail': 'already register, must active you account to continue'})
        
        except User.DoesNotExist:
            return super().validate(attrs)
        
    
    def create(self, validated_data):
        self.validate(validated_data)
        user = User.objects.create_user(
            username=validated_data['email'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            is_active=False,
        )
        code = self.generate_code(user)
        self.send_code(user=user, code=code)
        return user
        
    
    def generate_code(self, user):
        return generate_activation_code(user=user)
    
    
    def send_code(self, user, code):
        return send_activation_email(user=user, activation_code=code)
    
    
# Verify Code Activate For Activate Account
class VerifyCodeSerializer(serializers.Serializer):
    code = serializers.CharField(max_length = 5, required=True, write_only=True)
    def validate_code(self, code):
        user = check_activation_code(code)
        if user:
            self.active_account(user=user)
            Profile.objects.create(user = user)
        else:
            raise serializers.ValidationError(detail='The code you enter is not correct!!, try enter again')
        

    def active_account(self, user):
        user.is_active = True
        user.save()
        thank_activation_email(user=user)
        

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
            raise serializers.ValidationError(detail={'detail':'New password and confirmation dose not match'})
        return data

    def save(self):
        user = self.context['request'].user
        new_password = self.validated_data['new_password1']
        user.password = make_password(new_password)
        user.save()
        change_password_email(user = user)
        
   
        
        
        
class ResendCodeSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True, write_only=True)
    
    def validate_email(self, email):
        user = User.objects.filter(email = email).first()
        if not user:
            raise serializers.ValidationError(detail={'detail': 'we not have account with this email!'})
        if not user.is_active:
            raise serializers.ValidationError(detail={'detail': 'your account is not activate, activate now'})
        self.send_code(user=user)
   
   
    def send_code(self, user):
        # generate code, then send into user
        code = generate_activation_code(user)
        send_activation_email(user, code)


class ResetPasswordRequestSerializer(ResendCodeSerializer):
    def send_code(self, user):
        self.remove_token(user)
        code = generate_activation_code(user)
        reset_password_code_email(email = user.email, reset_password_code=code)
    
    def remove_token(self, user):
        token = Token.objects.filter(user = user).all()
        if token:
            token.delete()
        
        
        
class VerifyRestPasswordCodeSerializer(serializers.Serializer):
    code = serializers.CharField(required=True, write_only=True)
    
    def validate(self, attrs):
        if not CodeActivate.objects.filter(code=attrs.get('code')).exists():
            raise serializers.ValidationError(
                {'detail': 'The code enter is not correct, try again!!'}
            )
        return super().validate(attrs)
    
    def get_user(self, code):
        user = check_activation_code(code=code)
        return user

    def create_token(self):
        return Token.objects.create(user = self.get_user(code = self.validated_data.get('code'))).key

       
     
# Rest password for the user
class ResetPasswordSerializer(serializers.Serializer):
    token = serializers.CharField(required=True, write_only=True)
    new_password1 = serializers.CharField(required=True, write_only=True)
    new_password2 = serializers.CharField(required=True, write_only=True)
    
    def validate_token(self, token):
        if not Token.objects.get(key = token).user:
            raise serializers.ValidationError(detail='Token is not valid')
        return token
        
    def validate(self, data):
        new_password = data.get('new_password1')
        confirm_new_password = data.get('new_password2')
        if new_password != confirm_new_password:
            raise serializers.ValidationError(detail={'detail':'New password and confirmation do not match'})
        return data

    def get_user(self):
        user = Token.objects.get(key = self.validated_data.get('token')).user
        Token.objects.get(key = self.validated_data.get('token')).delete()
        return user
    
    def save(self):
        user = self.get_user()
        new_password = self.validated_data['new_password1']
        user.password = make_password(new_password)
        user.save()
        change_password_email(user)
        