from django.urls import path

from .views import NotificationListAPIView, NotificationMarkAsReadAPIView

app_name = 'notification'


urlpatterns = [
    path('', NotificationListAPIView.as_view(), name='notification-list'),
    path('<int:pk>/mark_as_read/', NotificationMarkAsReadAPIView.as_view(), name='notification-mark-as-read'),
]
