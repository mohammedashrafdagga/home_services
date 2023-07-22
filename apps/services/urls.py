from django.urls import path
from .views import (
    CategoryListAPIView,
    CategoryCreateAPIView,
    CategoryDeleteAPIView,
    CategoryListServicesAPIView,
    ServicesDetailView,
    LatestServicesListAPIView, 
    SearchServicesAPIView,
    ServicesCreateAPIView,
    ServicesUpdateAPIView,
    ServicesDeleteAPIView
)


app_name = 'services'

urlpatterns = [
    path('', SearchServicesAPIView.as_view(), name = 'list'),
    path('categories/', CategoryListAPIView.as_view(), name='category-list'),
    path('categories/<int:id>/', CategoryListServicesAPIView.as_view(), name='category-detail'),
    # for admin
    path('categories/create/', CategoryCreateAPIView.as_view(), name='category-create'),
    path('categories/<int:id>/delete/', CategoryDeleteAPIView.as_view(), name='category-delete'),
    path('new/', ServicesCreateAPIView.as_view(), name = 'new-services'),
    # --- Allow Any --
    path('latest-add/', LatestServicesListAPIView.as_view(), name='latest-add'),
    path('<int:id>/detail/', ServicesDetailView.as_view(), name='detail'),
    # for admin --
    path('<int:id>/update/', ServicesUpdateAPIView.as_view(), name = 'services-update'),
    path('<int:id>/delete/', ServicesDeleteAPIView.as_view(), name = 'services-delete')
    
]