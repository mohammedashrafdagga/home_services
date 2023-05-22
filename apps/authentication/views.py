from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import UserRegistrationSerializer, ChangePasswordSerializer, ResetPasswordSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response 
from .utils import (
    check_activation_code, generate_activation_code
)
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .email_message import resend_activation_email, reset_password_code_email, change_password_email
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token


# User Creation Code
class UserRegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]
    
    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)

            return Response({
                'access': str(refresh.access_token),
                'refresh': str(refresh),
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
        
# Now Verifying Code for User
class  UserVerifyingCodeAPIView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        activation_code = request.data.get('activation_code')
        user = check_activation_code( activation_code=activation_code)
        if user:
            user.is_active = True
            user.save()
            return Response({'detail': 'Account activated successfully'})
        return Response({
                'detail': 'code you enter to check is not correct',
            }, status=status.HTTP_400_BAD_REQUEST)
        
        
# Now Verifying Code for User
class  UserResendCodeAPIView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        email = request.data.get('email')
        user = User.objects.get(email = email)
        if user.is_active:
            return Response(
                {'detail': 'already you active, not needed to resend code to active'},
                status=status.HTTP_400_BAD_REQUEST
            )
        code = generate_activation_code(user = user)
        resend_activation_email(user=user, activation_code=code)
        return Response(
            {'detail': 'activation code is sending into your email'}
        )
        
        
# Now Verifying Code for User
class  ChangePasswordAPIView(APIView):
  
    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data,
                                              context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            change_password_email(user = request.user)
            return Response({'detail': 'Password changed successfully'})

        return Response(serializer.errors, status=400)
    

# Now Verifying Code for User
class  RestPasswordGenerateCodeAPIView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        email = request.data.get('email')
        user = User.objects.get(email = email)
        if not user.is_active:
            return Response(
                {'detail': 'already you is not active, must be active to reset-password'},
                status=status.HTTP_400_BAD_REQUEST
            )
        token = Token.objects.filter(user = user).all()
        if token:
            token.delete()
        code = generate_activation_code(user = user)
        reset_password_code_email(email=email, reset_password_code =code)
        return Response(
            {'detail': 'activation code is sending into your email'}
        )
        
        
# Now Verifying Code for User
class  VerifyingResetPasswordCodeAPIView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        reset_code = request.data.get('code')
        user = check_activation_code( activation_code=reset_code)
        if user:
            # generate token for user then send into response
            token = Token.objects.create(user = user) 
            return Response({'token': token.key})
        return Response({
                'detail': 'code you enter to check is not correct',
            }, status=status.HTTP_400_BAD_REQUEST)
        
        
        
# Now Verifying Code for User
class  ResetPasswordAPIView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        user = get_object_or_404(Token, key = request.data['token']).user
        if user:
            request.user = user
            serializer = ResetPasswordSerializer(data=request.data,
                                                context={'request': request})
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                Token.objects.get(user = request.user).delete()
                return Response({'detail': 'Password Reset successfully'})

        return Response(serializer.errors, status=400)
    