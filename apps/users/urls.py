from django.urls import path
from .views import (
    UserLocationListCreateAPIeView,
    UserLocationDetailAPIView, ProfileImageView,
    VerifyPasswordAPIView, ChangeEmailAPIView,
    VerifyCodeChangeEmailAPIView,
    EditUserInformationAPIView,
    CreateCustomServicesAPIView,
    CreateServicesProviderAPIView
)

app_name = 'users'

urlpatterns = [
    path('verify-password/', VerifyPasswordAPIView.as_view(), name='verify-password'),
    path('change-email/', ChangeEmailAPIView.as_view(), name='change-email'),
    path('verify-new-email/', VerifyCodeChangeEmailAPIView().as_view(), name='verify-new-email'),
    path('profile/image/', ProfileImageView.as_view(), name='profile-image'),
    path('edit-user/', EditUserInformationAPIView.as_view(), name='edit-user'),
    path('location/',UserLocationListCreateAPIeView.as_view(), name='list-create-location'),
    path('create-custom-service/', CreateCustomServicesAPIView.as_view(), name = 'custom-service'),
    path('create-service-provider/', CreateServicesProviderAPIView.as_view(), name = 'service-provider'),
    path('location/<int:location_id>/', UserLocationDetailAPIView.as_view(),name='get-update-delete-location'),
]