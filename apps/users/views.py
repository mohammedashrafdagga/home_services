from rest_framework import generics
from .models import Location
from .serializers import LocationSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsOwnerLocation

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
