from rest_framework import generics, response
from django.shortcuts import get_object_or_404
from .permissions import OrderIsOwnerPermissions, IsCompleteReviewPermissions
from .models import Order, Review, complete
from .serializer import OrderSerializer, ReviewSerializer
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
  