from rest_framework import generics 
from .models import Category, Services
from .serializers import (
    CategorySerializer,
    CategoryWithServicesSerializer,
    ServicesSerializer,
    ServicesDetailSerializer
)
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


class LatestServicesListAPIView(generics.ListAPIView):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer
    permission_classes = [AllowAny]
    
    def get_queryset(self):
        return super().get_queryset().order_by('-create_at')[:10]
    
class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]

    
class CategoryListServicesAPIView(generics.GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryWithServicesSerializer
    permission_classes = [AllowAny]
    
    def get(self, *args, **kwargs):
        category = Category.objects.get(pk = self.kwargs.get('id'))
        serializer = CategoryWithServicesSerializer(instance=category, context={'request': self.request})
        return Response(
            {'detail': serializer.data}
        )


class ServicesDetailView(generics.RetrieveAPIView):
    queryset = Services.objects.all()
    serializer_class = ServicesDetailSerializer
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
    