from rest_framework import generics
from rest_framework.response import Response
from .serializer import OrderSerializer, TrackingSerializer
from .mixins import OrderMixin, ReviewMixin, OrderAdminMixin


# Create New Ordering for User or Listing
class OrderListCreateAPIView(OrderMixin, generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = super().get_queryset().filter(user = self.request.user)
        status = self.request.GET.get('status')
        if status:
            queryset = queryset.filter(order_status= status)
        return queryset

# For Admin User
# Listing all Order
class OrderListAPIView(OrderAdminMixin, generics.ListAPIView):
    def get_queryset(self):
        queryset = super().get_queryset()
        status = self.request.GET.get('status')
        if status:
            queryset = queryset.filter(order_status= status)
        return queryset


# for Retrieve Delete Order
class OrderRetrieveDestroyAPIView(OrderMixin, generics.RetrieveDestroyAPIView):
    lookup_field = 'id'
    
# update Order for Admin user
class OrderUpdateAPIView(OrderAdminMixin, generics.UpdateAPIView):
    lookup_field = 'id'
    
# cerate review api view
class ReviewCreateAPiView(ReviewMixin, generics.CreateAPIView):
    ...
  

# Get List for Order View
class OrderTrackingListAPIView(OrderMixin, generics.RetrieveAPIView):
    lookup_field = 'id'
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = TrackingSerializer(instance.tracks_list.all(), many=True)
        order_serializer = OrderSerializer(instance=instance).data
        return Response({
            'order': order_serializer,
            'tracking': serializer.data
            }
        )
        