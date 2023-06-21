from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import (
    UserRegistrationSerializer,
     ChangePasswordSerializer,
    ResetPasswordSerializer,
    ResendCodeSerializer,
    ResetPasswordRequestSerializer,
    VerifyRestPasswordCodeSerializer,
    VerifyCodeSerializer
    )
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response 

from rest_framework.permissions import AllowAny, IsAuthenticated


'''
    User register Account - allow user to create account into system
'''
class UserRegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]
    
    
    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({
                'detail': 'The Account is create, must activate account to used'
            }, status=201)
        return Response(serializer.errors, status=400)
        
        
'''
    endpoint for verifying code send to user to activate account
'''
class  UserVerifyingCodeAPIView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = VerifyCodeSerializer
    def post(self, request):
        serializer = VerifyCodeSerializer(data=request.data)
        if serializer.is_valid():
            return Response({'detail': 'Account activated successfully, can login into app'})
        return Response(serializer.errors, status=400)
        
        
'''
    Allow to user to send in another time Code to email
'''
class  UserResendCodeAPIView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = ResendCodeSerializer
    
    def post(self, request):
        serializer = ResendCodeSerializer(data = request.data)
        if serializer.is_valid():
            return Response(
                {'detail':'Code is sending into you email, checkout!!'}
            )
        return Response(serializer.errors, status=400)
  
  
        
'''
    Allow to User to Change Password 
'''
class  ChangePasswordAPIView(generics.GenericAPIView):
    serializer_class =  ChangePasswordSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data,
                                              context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'detail': 'Password changed successfully'})

        return Response(serializer.errors, status=400)
    

'''
    Allow To User when forget password, request to reset password
'''
class  RestPasswordRequestCodeAPIView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = ResetPasswordRequestSerializer

    def post(self, request):
        serializer = ResetPasswordRequestSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        return Response(
                {'detail': 'activation code is sending into your email'}
            )
        
'''
    Verify Code send for verifying Account
'''
class  VerifyingResetPasswordCodeAPIView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = VerifyRestPasswordCodeSerializer
    
    def post(self, request):
        serializer = VerifyRestPasswordCodeSerializer(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            token = serializer.create_token()
            print(token)
            return Response({
                    'detail': 'you allow to enter new password and confirm new password',
                    'token': token
                })
        return Response(serializer.error_messages, status=400)
        
        
'''
    After checking Verifying allow to user to reset password
'''
class  ResetPasswordAPIView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = ResetPasswordSerializer
    
    def post(self, request):
        serializer = ResetPasswordSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'detail': 'Password Reset successfully'})
        return Response(serializer.errors, status=400)
    