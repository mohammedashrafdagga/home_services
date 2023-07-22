from rest_framework import generics 
from .models import Category
from .serializers import (
    CategorySerializer,
    ServicesSerializer
    )
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .mixins import CategoryMixin, CategoryAdminMixin, ServicesMixin, ServicesAdminMixin



# list all category
class CategoryListAPIView(CategoryMixin, generics.ListAPIView):
    permission_classes = [AllowAny]

# only for admin - create new category
class CategoryCreateAPIView(CategoryAdminMixin, generics.CreateAPIView):
    ...
    
# Delete Category for admin
class CategoryDeleteAPIView(CategoryAdminMixin, generics.DestroyAPIView):
    lookup_field = 'id'

# listing ALl Services Depend Category  
class CategoryListServicesAPIView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    
    def get(self, *args, **kwargs):
        category = get_object_or_404(Category, pk = self.kwargs.get('id'))
        
        serializer = CategorySerializer(instance=category, context={'request': self.request})
        services = ServicesSerializer(category.services,
                                      many=True, context = {'request': self.request}).data
        return Response(
            {
                'category': serializer.data,
                'services': services
            }
        )


# Create New Services (admin Only)
class ServicesCreateAPIView(ServicesAdminMixin, generics.CreateAPIView):
    ...
    
# Delete Services Using Id of that
class ServicesDeleteAPIView(ServicesAdminMixin, generics.DestroyAPIView):
    lookup_field = 'id'
    
    
#  Update Services
class ServicesUpdateAPIView(ServicesAdminMixin, generics.UpdateAPIView):
    lookup_field = 'id'
       
# Getting Details for Services
class ServicesDetailView(ServicesMixin, generics.RetrieveAPIView):
    lookup_field = 'id'
    
# allow to user to search about Services Using name of the services
class SearchServicesAPIView(ServicesMixin, generics.ListAPIView):
    def get_queryset(self):
        q = self.request.GET.get('q')
        queryset = super().get_queryset()
        if q is not None:
            return queryset.filter(name__icontains = q).all()
        return queryset
    

#  get latest 10 services adding in system
class LatestServicesListAPIView(ServicesMixin, generics.ListAPIView):
    ...
    
    def get_queryset(self):
        return super().get_queryset().order_by('-create_at')[:10]
    
    
    
