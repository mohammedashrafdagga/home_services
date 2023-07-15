from rest_framework import generics
from .models import Location, Profile, ChangeEmail
from .serializers import (
    LocationSerializer, ProfileSerializer,
    PasswordSerializer, ChangeEmailSerializer, EditUserSerializer,
    CustomServicesSerializer, ServiceProviderSerializer,
    UserInformationSerializer
)
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsOwnerLocation
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from apps.authentication.utils import send_change_email, check_activation_code
from apps.authentication.email_message import send_successfully_change_email
from apps.authentication.serializers import VerifyCodeSerializer
from apps.orders.models import CustomOrder, Notification


class LocationMixin():
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [IsAuthenticated,IsOwnerLocation]
    authentication_classes = [JWTAuthentication]
    def get_queryset(self):
        return super().get_queryset().filter(user = self.request.user)
    
class UserLocationListCreateAPIeView(LocationMixin, generics.ListCreateAPIView):
    ...
    

class UserLocationDetailAPIView(LocationMixin, generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    lookup_url_kwarg = 'location_id'



'''
    Profile Image View for adding or createing image view
'''
class ProfileImageView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    parser_classes = (MultiPartParser,)

    # Getting serializer
    def get(self, request):
        profile = get_object_or_404(Profile, user = request.user)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)
    
    
    def post(self, request):
        profile = get_object_or_404(Profile, user = request.user)
        serializer = ProfileSerializer(instance=profile, data=request.data, context = {'user': request.user})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)

# Verify password for user
class VerifyPasswordAPIView(generics.GenericAPIView):
    serializer_class = PasswordSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    def post(self, request):
        serializer = PasswordSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            return Response({'detail': 'كلمة المرور صحيحة'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# Allow to User to Change Email View
class ChangeEmailAPIView(generics.GenericAPIView):
    serializer_class = ChangeEmailSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    def post(self, request):
        serializer = ChangeEmailSerializer(data=request.data)
        if serializer.is_valid():
            new_email = serializer.validated_data['email']
            ChangeEmail.objects.create(user=request.user, new_email = new_email)
            send_change_email(context={'user': request.user,'new_email': new_email})
            return Response({'detail': 'تم إرسال كود التفعيل عل الإيميل الجديد'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# VerifyCode change email
class VerifyCodeChangeEmailAPIView(generics.GenericAPIView):
    serializer_class = VerifyCodeSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    
    def post(self, request):
        user = check_activation_code(code = request.data['code'])
        if user is not None:
            user_email = ChangeEmail.objects.filter(user=request.user).first()
            user.email = user_email.new_email
            user.username = user_email.new_email
            user.save()
            ChangeEmail.objects.filter(user = request.user).delete()
            send_successfully_change_email(content={'email': user_email.new_email})
            return Response({'detail': 'ثم تحديث البريد الإكتروني الخاص بك بنجاح'}, status=status.HTTP_200_OK)
        return Response({'detail': 'إدخال كود التفعيل الخاطئ'}, status=status.HTTP_400_BAD_REQUEST)
    
# Update User Information
class EditUserInformationAPIView(generics.GenericAPIView):
    serializer_class = EditUserSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    
    def put(self, request):
        serializer = EditUserSerializer(instance=request.user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'detail': 'ثم تحديث البيانات بنجاح', 'data':serializer.validated_data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

class CreateCustomServicesAPIView(generics.GenericAPIView):
    serializer_class = CustomServicesSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    
    def post(self, request):
        serializer = CustomServicesSerializer(data = request.data)
        if serializer.is_valid():
            custom_service = serializer.save(request_by = request.user)
            name = f"{custom_service.name}-{custom_service.id}-{request.user.id}"
            service_slug = name.strip().lower().replace(' ', '-')
            custom_service.slug = service_slug
            custom_service.save()
            order = CustomOrder.objects.create(create_by = request.user,
                service = custom_service, date_order = serializer.validated_data['request_date'],
                time_order = serializer.validated_data['request_time'], location = custom_service.location)
            Notification.objects.create(
            user = request.user,
            custom_order = order,
            order_status = order.order_status,
            text = f"تم طلب خدمة مخصصة جديدة بنجاح")
            return Response(
                {'detail': {
                    'status': 'تم إنشاء طلب خدمة مخصصة بنجاح',
                    'services': CustomServicesSerializer(custom_service).data,
                    'order_status': order.order_status
                }}, status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class CreateServicesProviderAPIView(generics.CreateAPIView):
    serializer_class = ServiceProviderSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(user = self.request.user)
            return Response(
                    {'detail': {
                        'status': 'تم إنشاء طلب لتقديم الخدمات عبر التطبيق بنجاح',
                        'services': serializer.validated_data
                    }}, status=status.HTTP_201_CREATED
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# For Getting User Information
class UserInformationAPIView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    def get(self, request):
        serializer = UserInformationSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)