from django.urls import path
from .views import (
    CategoryListAPIView,
    CategoryListServicesAPIView,
    ServicesDetailView,
    LatestServicesListAPIView, 
    SearchServicesAPIView
)


app_name = 'services'

urlpatterns = [
    path('', SearchServicesAPIView.as_view(), name = 'list'),
    
    path('categories/', CategoryListAPIView.as_view(), name='category-list'),
    path('latest-add/', LatestServicesListAPIView.as_view(), name='latest-add'),
    path('category/<int:id>/services/', CategoryListServicesAPIView.as_view(), name='category-detail'),
    path('<int:id>/detail/', ServicesDetailView.as_view(), name='detail')
    
]