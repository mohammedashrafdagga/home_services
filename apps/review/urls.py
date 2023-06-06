from django.urls import path
from .views import (
    ReviewCreateAPiView
)


# naming space
app_name = 'reviews'


urlpatterns = [
    path('', ReviewCreateAPiView.as_view(),name='create-review'),
]