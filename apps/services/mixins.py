from .models import Category, Services
from .serializers import CategorySerializer, ServicesSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication




# Category Mixin 
class CategoryMixin:
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# Mixins For admin (additional such create, delete)
class CategoryAdminMixin(CategoryMixin):
    permission_classes = [IsAuthenticated, IsAdminUser]
    authentication_classes = [JWTAuthentication]
    
    
    
# Services Mixins
class ServicesMixin:
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer
    permission_classes = [AllowAny]
    
    
# Services Admin Mixin
class ServicesAdminMixin(ServicesMixin):
    permission_classes = [IsAuthenticated, IsAdminUser]
    authentication_classes = [JWTAuthentication]