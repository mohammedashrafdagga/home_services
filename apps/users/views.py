from rest_framework import generics
from .models import  Profile
from .serializers import (
    ProfileSerializer,
    EditUserSerializer, UserInformationSerializer
)
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from .mixins import LocationMixin, UserMixin


# for listing or create location
class UserLocationListCreateAPIeView(LocationMixin, generics.ListCreateAPIView):
    def get_queryset(self):
        return super().get_queryset().filter(user = self.request.user)
    

# for Retrieve, Update or delete Location
class UserLocationDetailAPIView(LocationMixin,
    generics.RetrieveUpdateDestroyAPIView
):
    lookup_field = 'id'
    lookup_url_kwarg = 'location_id'
    
    

# Profile Image View for adding or creating image view
class ProfileImageView(UserMixin, APIView):
    parser_classes = (MultiPartParser,)

    # Getting serializer
    def get(self, request):
        profile = get_object_or_404(Profile, user = request.user)
        serializer = ProfileSerializer(profile)
        return Response(data = serializer.data)
    
    
    def post(self, request):
        profile = get_object_or_404(Profile, user = request.user)
        serializer = ProfileSerializer(instance=profile, data=request.data, context = {'user': request.user})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)


# # Update User Information
class EditUserInformationAPIView(UserMixin, generics.GenericAPIView):
    def put(self, request):
        serializer = EditUserSerializer(instance=request.user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'detail': 'ثم تحديث البيانات بنجاح',
                            'data':serializer.validated_data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


# # For Getting User Information
class UserInformationAPIView(UserMixin, generics.GenericAPIView):
    def get(self, request):
        return Response(data = UserInformationSerializer(request.user).data)