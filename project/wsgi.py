
import os

from django.core.wsgi import get_wsgi_application
from project.settings.base import DEBUG

if DEBUG:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings.local")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings.production")

application = get_wsgi_application()
