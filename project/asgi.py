
import os
from .settings import base


from django.core.asgi import get_asgi_application

if base.DEBUG:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings.local")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings.production")

application = get_asgi_application()
