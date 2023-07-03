from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
	TokenBlacklistView
)
from .views import (
  UserRegisterAPIView,
  UserVerifyingCodeAPIView,
  UserResendCodeAPIView,
  ChangePasswordAPIView,
  RestPasswordRequestCodeAPIView,
  VerifyingResetPasswordCodeAPIView,
  ResetPasswordAPIView
)

app_name = 'authentication'

urlpatterns = [
  path('register/', UserRegisterAPIView.as_view(), name = 'register'),
  path('login/', TokenObtainPairView.as_view(), name='login'),
  path('login-refresh/', TokenRefreshView.as_view(), name='login-refresh'),
  path('logout/', TokenBlacklistView.as_view(), name= 'logout'),
  path('verify-code/', UserVerifyingCodeAPIView.as_view(), name='verify-code'),
  path('resend-code/', UserResendCodeAPIView.as_view(), name='resend-code'),
  path('change-password/', ChangePasswordAPIView.as_view(), name='change-password'),
  path('reset-password-code/', RestPasswordRequestCodeAPIView.as_view(), name ='reset-password-code'),
  path('verify-reset-password-code/', VerifyingResetPasswordCodeAPIView.as_view(), name='verify-reset-password-code'),
  path('reset-new-password/', ResetPasswordAPIView.as_view(),name='reset-new-password')
]