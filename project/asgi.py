
import os


from django.core.asgi import get_asgi_application

from project.settings.base import DEBUG

if DEBUG:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings.local")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings.production")

application = get_asgi_application()
