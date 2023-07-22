from django.urls import path
from .views import (
    CategoryListAPIView,
    CategoryCreateAPIView,
    CategoryListServicesAPIView,
    ServicesDetailView,
    LatestServicesListAPIView, 
    SearchServicesAPIView
)


app_name = 'services'

urlpatterns = [
    path('', SearchServicesAPIView.as_view(), name = 'list'),
    path('categories/', CategoryListAPIView.as_view(), name='category-list'),
    # for admin
    path('categories/create/', CategoryCreateAPIView.as_view(), name='category-create'),
    # path('categories/<int:id>/delete', CategoryListAPIView.as_view(), name='category-list'),
    # ---- 
    path('latest-add/', LatestServicesListAPIView.as_view(), name='latest-add'),
    path('category/<int:id>/', CategoryListServicesAPIView.as_view(), name='category-detail'),
    path('<int:id>/detail/', ServicesDetailView.as_view(), name='detail')
    
]