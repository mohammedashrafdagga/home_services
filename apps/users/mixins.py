from .models import Location
from .serializers import LocationSerializer
from .permissions import IsOwnerLocation
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class LocationMixin:
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [IsAuthenticated,IsOwnerLocation]
    authentication_classes = [JWTAuthentication]
    
    
class UserMixin:
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
