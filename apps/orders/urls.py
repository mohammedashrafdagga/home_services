from django.urls import path
from .views import (
    OrderActiveListApiView,
    AllOrderListApiView,
    OrderCreateAPIView,
    NonReadNotificationsAPIView,
    ReadNotificationsAPIView,
    ChangeNotificationAPIView
)


# naming space
app_name = 'orders'


urlpatterns = [
    path('', OrderCreateAPIView.as_view(),name='create-order'),
    path('active-order/', OrderActiveListApiView.as_view(), name='active-order'),
    path('all-order/', AllOrderListApiView.as_view(), name='all-order'),
    path('read-notification/', ReadNotificationsAPIView.as_view(), name='read-notification'),
    path('unread-notification/', NonReadNotificationsAPIView.as_view(),name='unread-notification'),
    path('notification/change/', ChangeNotificationAPIView.as_view(), name='change-notification')
]