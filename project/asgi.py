
import os

from project.settings.base import DEBUG

if DEBUG:
    setting_module = "project.settings.local"
else:
    setting_module = "project.settings.production"



from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", setting_module)
application = get_asgi_application()
