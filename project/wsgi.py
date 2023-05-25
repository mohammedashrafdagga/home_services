
import os
from settings import base

from django.core.wsgi import get_wsgi_application

if base.DEBUG:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings.local")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings.production")

application = get_wsgi_application()
