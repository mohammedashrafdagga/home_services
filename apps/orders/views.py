from rest_framework import generics
from .models import Order
from .models import (
    under_review, underway
)
from .serializer import OrderSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class OrderActiveListApiView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    
    # updating GetQuerySet
    def get_queryset(self):
        statuses = [under_review, underway]
        queryset = super().get_queryset().filter(create_by = self.request.user, order_status__in=statuses)
        return queryset
    
    

class AllOrderListApiView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    # updating GetQuerySet
    def get_queryset(self):
        return super().get_queryset().filter(create_by = self.request.user)
    
class OrderCreateAPIView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    
