from rest_framework import generics 
from .models import Category, Services
from .serializers import (
    CategorySerializer,
    ServicesSerializer
    )
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response


#  get latest 10 services adding in system
class LatestServicesListAPIView(generics.ListAPIView):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer
    permission_classes = [AllowAny]
    
    def get_queryset(self):
        return super().get_queryset().order_by('-create_at')[:10]
    
# list all category
class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]

# only for admin - create new category
class CategoryCreateAPIView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    authentication_classes = [JWTAuthentication]
    
class CategoryListServicesAPIView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    
    def get(self, *args, **kwargs):
        category = Category.objects.get(pk = self.kwargs.get('id'))
        serializer = CategorySerializer(instance=category, context={'request': self.request})
        services = ServicesSerializer(category.services,
                                      many=True, context = {'request': self.request}).data
        return Response(
            {
                'category': serializer.data.get('name'),
                'services': services
            }
        )


class ServicesDetailView(generics.RetrieveAPIView):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer
    lookup_field = 'id'
    
    
class SearchServicesAPIView(generics.ListAPIView):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer
    permission_classes = [AllowAny]
    
    def get_queryset(self):
        q = self.request.GET.get('q')
        queryset = super().get_queryset()
        if q is not None:
            return queryset.filter(name__icontains = q).all()
        return queryset
    
