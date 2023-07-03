
import os
from django.core.wsgi import get_wsgi_application

# Set settings Module File

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

application = get_wsgi_application()
