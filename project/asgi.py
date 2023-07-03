import os
from django.core.asgi import get_asgi_application

# Set settings Module File
if os.environ.get('DEBUG') == 'True':
    settings_module = 'project.settings.local'
else:
    settings_module = 'project.settings.production'
    
    
os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)
application = get_asgi_application()
