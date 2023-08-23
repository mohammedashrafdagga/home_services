from rest_framework import generics
from .mixins import NotificationMixin
from rest_framework.response import Response
from .serializers import NotificationSerializer

# Listing all Notification
class NotificationListAPIView(NotificationMixin, generics.ListAPIView):

   def get_queryset(self):
       return super().get_queryset().filter(user = self.request.user)


# Change Notification from unread to read
class NotificationMarkAsReadAPIView(NotificationMixin, generics.GenericAPIView):
    lookup_field = 'pk'

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_read = True
        instance.save()
        return Response(NotificationSerializer(instance=instance).datao)
