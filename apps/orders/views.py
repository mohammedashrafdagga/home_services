from rest_framework import generics
from rest_framework.response import Response
from .permissions import OrderIsOwnerPermissions, IsCompleteReviewPermissions, IsOwnerTracking
from .models import Order, Review
from .serializer import OrderSerializer, ReviewSerializer, TrackingSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication



class OrderMixin():
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, OrderIsOwnerPermissions]
    authentication_classes = [JWTAuthentication]

# Create New Ordering for User
class OrderListCreateAPIView(OrderMixin, generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = super().get_queryset().filter(user = self.request.user)
        status = self.request.GET.get('status')
        if status:
            queryset = queryset.filter(order_status= status)
        return queryset

# for Retrieve Delete Order
class OrderRetrieveDestroyAPIView(OrderMixin, generics.RetrieveDestroyAPIView):
    lookup_field = 'id'
    
    
# Create Review for Order

# cerate review api view
class ReviewCreateAPiView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated, IsCompleteReviewPermissions]
    authentication_classes = [JWTAuthentication]
  
  
  
# Get List for Order View
class OrderTrackingListAPIView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = TrackingSerializer
    permission_classes = [IsAuthenticated, IsOwnerTracking]
    authentication_classes = [JWTAuthentication]
    lookup_field = 'id'
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance.tracks_list.all(), many=True)
        order_serializer = OrderSerializer(instance=instance).data
        return Response({
            'order': order_serializer,
            'tracking': serializer.data
            }
        )
        