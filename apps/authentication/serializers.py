from django.contrib.auth.models import User
from rest_framework import serializers


# User register Serializer
class UserRegistrationSerializer(serializers.ModelSerializer):
    is_active  = serializers.BooleanField(default=False, read_only=True)
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name','password', 'is_active']
        read_only_fields = ['username']

    def validate(self, attrs):
        try:
            user = User.objects.get(username = attrs.get('email'))
            if user.is_active:
                raise serializers.ValidationError(
                    {'detail': 'المستخدم مسجل بالفعل, قم بتسجيل الدخول'}
                )
            if not user.is_active:
                raise serializers.ValidationError({'detail': 'المستخدم مسجل بالفعل , قم بتفعيل الحساب'})
        
        except User.DoesNotExist:
            return super().validate(attrs)
        


# SendCodeSerializer      
class SendRestPasswordUrlSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True, write_only=True)
    
    def validate(self, data):
        user = User.objects.filter(email = data.get('email')).first()
        if user is None:
            raise serializers.ValidationError(detail={'detail': 'ليس لديك حساب, قم بالتسجيل'})
        return data


# Password Mixins
class PasswordSerializerMixin:
    def validate(self, data):
        if data['new_password1'] != data['new_password2']:
            raise serializers.ValidationError(detail = {'detail':'تاكيد كلمة المرور لا تتشابه مع كلمة المرور الجديدة'})
        return data
    
    def update(self, instance, validated_data):
        instance.set_password(validated_data['new_password1'])
        instance.save()
        return instance   
        
# Change Password Serializer
class ChangePasswordSerializer(PasswordSerializerMixin, serializers.Serializer):
    old_password = serializers.CharField(required=True, write_only=True)
    new_password1 = serializers.CharField(required=True, write_only=True)
    new_password2 = serializers.CharField(required=True, write_only=True)

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError(detail='خطا في إدخال كلمة المرور')
        return value


