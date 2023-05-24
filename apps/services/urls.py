from django.urls import path
from .views import (
    CategoryListAPIView,
    CategoryListServicesAPIView
)


app_name = 'services'

urlpatterns = [
    path('categories/', CategoryListAPIView.as_view(), name='category-list'),
    path('category/<int:id>/services/', CategoryListServicesAPIView.as_view(), name='category-detail'),
]