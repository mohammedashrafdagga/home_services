from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
	TokenBlacklistView
)
from .views import (
  UserRegisterAPIView,
  ChangePasswordAPIView,
  RestPasswordUrlAPIView,
  verify_account_view,
  verify_rest_password
)

app_name = 'authentication'

urlpatterns = [
  path('register/', UserRegisterAPIView.as_view(), name = 'register'),
  path('login/', TokenObtainPairView.as_view(), name='login'),
  path('login-refresh/', TokenRefreshView.as_view(), name='login-refresh'),
  path('logout/', TokenBlacklistView.as_view(), name= 'logout'),
  path('verify-account/', verify_account_view, name='verify-account'),
  path('change-password/', ChangePasswordAPIView.as_view(), name='change-password'),
  path('reset-password/', RestPasswordUrlAPIView.as_view(), name ='reset-password'),
  path('rest-password-verify/', verify_rest_password, name='rest-password-verify'),
]