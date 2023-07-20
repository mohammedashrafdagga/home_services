from django.urls import path
from .views import ( 
        OrderListCreateAPIView,
        OrderRetrieveDestroyAPIView,
        ReviewCreateAPiView,
        OrderTrackingListAPIView
)

# naming space
app_name = 'orders'


urlpatterns = [
    path('', OrderListCreateAPIView.as_view(),name='listCreate'),
    path('review/', ReviewCreateAPiView.as_view(),name='new-review'),
    path('<int:id>/', OrderRetrieveDestroyAPIView.as_view(),name='detailDelete'),
    path('<int:id>/tracking/', OrderTrackingListAPIView.as_view(),name='order-tracking'),
]