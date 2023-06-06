from django.urls import path
from .views import (
    OrderActiveListApiView,
    AllOrderListApiView,
    OrderCreateAPIView
)


# naming space
app_name = 'orders'


urlpatterns = [
    path('', OrderCreateAPIView.as_view(),name='create-order'),
    path('active-order/', OrderActiveListApiView.as_view(), name='active-order'),
    path('all-order/', AllOrderListApiView.as_view(), name='all-order')
]