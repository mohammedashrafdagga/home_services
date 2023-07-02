
import os
from project.settings.base import DEBUG

if DEBUG:
    setting_module = "project.settings.local"
else:
    setting_module = "project.settings.production"



from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", setting_module)
application = get_wsgi_application()
