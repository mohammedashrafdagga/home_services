from rest_framework import generics 
from .models import Category, Services
from .serializers import (
    CategorySerializer,
    CategoryWithServicesSerializer,
    ServicesSerializer
)
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

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
    serializer_class = ServicesSerializer
    lookup_field = 'id'
    