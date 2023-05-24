from django.urls import path
from .views import (
    CategoryListAPIView,
    CategoryListServicesAPIView,
    ServicesDetailView
)


app_name = 'services'

urlpatterns = [
    path('categories/', CategoryListAPIView.as_view(), name='category-list'),
    path('category/<int:id>/services/', CategoryListServicesAPIView.as_view(), name='category-detail'),
    path('<int:id>/detail/', ServicesDetailView.as_view(), name='detail')
    
]