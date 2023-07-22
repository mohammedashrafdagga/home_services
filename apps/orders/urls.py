from django.urls import path
from .views import ( 
        OrderListCreateAPIView,
        OrderRetrieveDestroyAPIView,
        ReviewCreateAPiView,
        OrderTrackingListAPIView,
        OrderListAPIView,
        OrderUpdateAPIView
)

# naming space
app_name = 'orders'


urlpatterns = [
    path('', OrderListCreateAPIView.as_view(),name='listCreate'),
    # listing all order or (Depend on Order status) (only for admin)
    path('list/', OrderListAPIView.as_view(), name = 'list'),
    path('review/', ReviewCreateAPiView.as_view(),name='new-review'),
    path('<int:id>/', OrderRetrieveDestroyAPIView.as_view(),name='detailDelete'),
    # update for admin (change order status )
    path('<int:id>/update/', OrderUpdateAPIView.as_view(),name='update'),
    path('<int:id>/tracking/', OrderTrackingListAPIView.as_view(),name='order-tracking'),
]