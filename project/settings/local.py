from .base import *


# DATABASES Settings
DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': os.environ.get('DATABASE_NAME'),
       'USER': os.environ.get('DATABASE_USER'),
       'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
       'HOST': os.environ.get('DATABASE_HOST'),
       'PORT': os.environ.get('DATABASE_PORT')
   }
}
