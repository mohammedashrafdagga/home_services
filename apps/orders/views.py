from rest_framework import generics
from rest_framework.response import Response
from .models import Order, CustomOrder, Notification
from .models import (
    under_review, underway, complete, rejected
)
from .serializer import OrderSerializer, CustomOrderSerializer, NotificationSerializer
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


# return only reading All Notification (Last 5)
class ReadNotificationsAPIView(generics.ListAPIView):
    queryset = Notification
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    
    def get_queryset(self):
        return Notification.objects.filter(user = self.request.user, status = 'مقروءة')[:5]
    
# return only unreading All Notification and  (Last 5)
class NonReadNotificationsAPIView(generics.ListAPIView):
    queryset = Notification
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    
    def get_queryset(self):
        orders = Order.objects.filter(create_by = self.request.user)
        custom_order = CustomOrder.objects.filter(create_by = self.request.user)
        un_read_order = Notification.objects.filter(user = self.request.user,order__in = orders)
        un_read_custom_order = Notification.objects.filter(user = self.request.user,
                                                           custom_order__in = custom_order)
        
        for un_order in un_read_order:
            if un_order.order_status != un_order.order.order_status:
                if un_order.status == 'مقروءة':
                    un_order.status = 'غير مقروءة'
                if un_order.order_status == underway:
                    un_order.text = f'الطلب {un_order.service.name} قيد التنفيذ الأن'
                    un_order.order_status = underway
                    un_order.save()
                if un_order.order_status == complete:
                    un_order.text = f'الطلب {un_order.service.name} اصبح مكتمل الأن'
                    un_order.order_status = complete
                    un_order.save()
            
                if un_order.order_status == rejected:
                    un_order.text = f'تم رفض طلب {un_order.service.name}'
                    un_order.order_status = rejected
                    un_order.save()
                
        for un_order in un_read_custom_order:
            if un_order.order_status != un_order.custom_order.order_status:
                if un_order.status == 'مقروءة':
                    un_order.status = 'غير مقروءة'
                    
                if un_order.order_status == underway:
                    un_order.text = f'الطلب {un_order.service.name} قيد التنفيذ الأن'
                    un_order.order_status = underway
                    un_order.save()
                if un_order.order_status == complete:
                    un_order.text = f'الطلب {un_order.service.name} اصبح مكتمل الأن'
                    un_order.order_status = complete
                    un_order.save()
            
                if un_order.order_status == rejected:
                    un_order.text = f'تم رفض طلب {un_order.service.name}'
                    un_order.order_status = rejected
                    un_order.save()
        return Notification.objects.filter(user = self.request.user, status = 'غير مقروءة')
    
    
class ChangeNotificationAPIView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    
    def post(self, request):
        unread_notification = Notification.objects.filter(user = request.user, status = 'غير مقروءة')
        for notification in unread_notification:
            notification.status = 'مقروءة'
            notification.save()
            
        return Response(status=200)