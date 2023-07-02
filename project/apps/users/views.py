from rest_framework import generics
from .models import Location, Profile
from .serializers import LocationSerializer, ProfileSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsOwnerLocation
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from django.shortcuts import get_object_or_404



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

        return Response({'message': 'Image or user not provided.'}, status=400)
