from .models import Order, Tracking, Review
from .serializer import OrderSerializer, TrackingSerializer, ReviewSerializer
from .permissions import OrderIsOwnerPermissions, IsCompleteReviewPermissions
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication



# for Normal User
class OrderMixin:
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, OrderIsOwnerPermissions]
    authentication_classes = [JWTAuthentication]


# For Admin User
class OrderAdminMixin(OrderMixin):
    permission_classes = [IsAuthenticated, IsAdminUser]
    
    
    
# Review Mixin
class ReviewMixin:
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated, IsCompleteReviewPermissions]
    authentication_classes = [JWTAuthentication]