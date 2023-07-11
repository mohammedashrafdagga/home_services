from rest_framework import generics
from rest_framework.response import Response
from .models import Order, CustomOrder
from .models import (
    under_review, underway
)
from .serializer import OrderSerializer, CustomOrderSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class OrderActiveListApiView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    
    # updating GetQuerySet
    def get(self, request):
        statuses = [under_review, underway]
        order_list = Order.objects.filter(create_by = request.user, order_status__in=statuses)
        order_queryset = OrderSerializer(order_list, many=True).data
        custom_order_list = CustomOrder.objects.filter(create_by = request.user, order_status__in=statuses)
        queryset2 = CustomOrderSerializer(custom_order_list, many=True).data
        return Response(order_queryset + queryset2)
    
    

class AllOrderListApiView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
  # updating GetQuerySet
    def get(self, request):
        order_list = Order.objects.filter(create_by = request.user)
        order_queryset = OrderSerializer(order_list, many=True).data
        custom_order_list = CustomOrder.objects.filter(create_by = request.user)
        queryset2 = CustomOrderSerializer(custom_order_list, many=True).data
        return Response(order_queryset + queryset2)
    
class OrderCreateAPIView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    
