from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/auth/', include('project.apps.authentication.urls', namespace='authentication')),
    path('api/services/', include('project.apps.services.urls', namespace='services')),
    path('api/orders/', include('project.apps.orders.urls', namespace='orders')),
    path('api/reviews/', include('project.apps.review.urls', namespace='reviews')),
    path('api/users/', include('project.apps.users.urls', namespace='users')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/docs/', SpectacularSwaggerView.as_view(url_name = 'schema')),
]



if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)