from rest_framework import generics
from .serializer import ReviewSerializer
from .models import Review
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


# cerate review api view
class ReviewCreateAPiView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    
    def perform_create(self, serializer):
        # filter Here if User already Have Review Service can't add another review
        return super().perform_create(serializer)