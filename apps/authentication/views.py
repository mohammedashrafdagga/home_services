from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import (
    UserRegistrationSerializer,
     ChangePasswordSerializer,
    ResetPasswordSerializer,
    SendCodeSerializer,
    VerifyCodeSerializer
    )
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response 
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from .utils import (
    create_activation_code, check_activation_code,
    activate_account, rest_password_request, generate_token,
    get_user_by_token, delete_token
)
from .email_message import send_change_password_email



# allow user to create account into system
class UserRegisterAPIView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserRegistrationSerializer
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.username = serializer.validated_data['email']
            user.set_password(serializer.validated_data['password'])
            user.save()
            create_activation_code(user)
            return Response({'detail': 'الحساب ثم إنشاؤه بالفعل, قم بتفعيل الحساب'}, status=201)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# verify code user enter to activate code
class  UserVerifyingCodeAPIView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = VerifyCodeSerializer
    def post(self, request):
        user = check_activation_code(request.data['code'])
        if user is not None:
            activate_account(user=user)
            return Response({'detail': 'الحساب ثم تفعيله, قم بتسحيل الدخول'})

        return Response({'detail': 'الكود الذي قمت بإدخاله غير صحيح'}, status=400)
        
# allow to user to request sending code into email
class  UserResendCodeAPIView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = SendCodeSerializer
    
    def post(self, request):
        serializer = SendCodeSerializer(data = request.data)
        if serializer.is_valid():
            user = User.objects.get(email = serializer.validated_data['email'])
            create_activation_code(user)
            return Response(
                {'detail':'كود التفعيل تم إرساله عبر الإيميل، تفقد ذلك'}
            )
        return Response(serializer.errors, status=400)
  
# allow to user to change password 
class  ChangePasswordAPIView(generics.GenericAPIView):
    serializer_class =  ChangePasswordSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data,
                                              context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.update(instance=request.user, validated_data=serializer.validated_data)
            send_change_password_email(content = {'email': request.user.email})
            return Response({'detail': 'ثم تغيير كلمة المرور بنجاح'})

        return Response(serializer.errors, status=400)
    


class  RestPasswordRequestCodeAPIView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = SendCodeSerializer

    def post(self, request):
        serializer = SendCodeSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        rest_password_request(email = serializer.validated_data['email'])
        return Response(
                {'detail': 'كود التاكيد ثم إرساله عبر الإيميل، تفقد إيميلك'}
            )
        
'''
    Verify Code send for verifying Account
'''
class  VerifyingResetPasswordCodeAPIView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = VerifyCodeSerializer
    
    def post(self, request):
        user = check_activation_code(code=request.data['code'])
        if user is not None:
            token = generate_token(user=user)
            return Response({
                    'detail': 'يمكن الإن تحديث كلمة المرور',
                    'token': token
                })
        return Response({'detail': 'الكود الذي قمت بإدخال غير صحيح'})
        
        
'''
    After checking Verifying allow to user to reset password
'''
class  ResetPasswordAPIView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = ResetPasswordSerializer
    
    def post(self, request):
        serializer = ResetPasswordSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = get_user_by_token(key_token=serializer.validated_data['token'])
            serializer.update(instance=user, validated_data=serializer.validated_data)
            delete_token(user=user)
            return Response({'detail': 'تم تحديث كلمة المرور بنجاح'})
        return Response(serializer.errors, status=400)
    