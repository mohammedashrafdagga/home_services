from django.urls import path
from .views import (
    UserLocationListCreateAPIeView,
    UserLocationDetailAPIView,
    UserInformationAPIView,
    EditUserInformationAPIView,
    ProfileImageView
)

app_name = 'users'

urlpatterns = [
    path('', UserInformationAPIView.as_view(), name='user-data'),
    path('edit/', EditUserInformationAPIView.as_view(), name='edit-user'),
    path('image/', ProfileImageView.as_view(), name='profile-image'),
    path('location/',UserLocationListCreateAPIeView.as_view(), name='list-create-location'),
    path('location/<int:location_id>/', UserLocationDetailAPIView.as_view(),name='get-update-delete-location'),
]