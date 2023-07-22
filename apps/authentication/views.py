from rest_framework import generics
from .serializers import (
    UserRegistrationSerializer,
     ChangePasswordSerializer,
    SendRestPasswordUrlSerializer
)
from django.shortcuts import render
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response 
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from .utils import (
    rest_password_request,
    get_user_by_token
)
from .email_message import send_change_password_email



# allow user to create account into system
class UserRegisterAPIView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserRegistrationSerializer
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save(is_active=False)
            user.username = serializer.validated_data['email']
            user.set_password(serializer.validated_data['password'])
            user.save()
            return Response({'detail': 'الحساب ثم إنشاؤه بالفعل, قم بتفعيل الحساب'}, status=201)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
    


class  RestPasswordUrlAPIView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = SendRestPasswordUrlSerializer

    def post(self, request):
        serializer = SendRestPasswordUrlSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        rest_password_request(request=request, email = serializer.validated_data['email'])
        return Response(
                {'detail': "رابط إعادة تعيين كلمة المرور تم إرساله عبر البريد الألكتروني"}
            )

        
# Verify account for user
def verify_account_view(request):
    user= get_user_by_token(key_token=request.GET.get('token'))
    user.is_active = True
    user.save()
    return render(request, 'authentication/verify_account.html', context = {'name': 
        f"{user.first_name} {user.last_name}"})


# for rest password 
def verify_rest_password(request):
    error = ''
    if request.method == 'POST':
        # check password is matching or not
        if request.POST['new_password1'] == request.POST['new_password2']:
            user = get_user_by_token(key_token=request.POST.get('token'))
            user.set_password(request.POST['new_password1'])
            user.save()    
            send_change_password_email(content = {'email': user.email,
                'name': f"{user.first_name} {user.last_name}"})
            return render(request, 'authentication/rest_password_complete.html')
        error = 'The New Password and Confirm password Not Match'
        return render(request, 'authentication/rest_password_form.html', context = {'token': request.POST.get('token'), 'error': error})
    else:
        return render(request, 'authentication/rest_password_form.html', context = {'token': request.GET.get('token'), 'error': error})
    
    
# Delete User Account
class DeleteUserAccount(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    # For deleting Account
    def delete(self, request):
        request.user.delete()
        return Response(data={'detail': 'Your Account is delete Successfully'})