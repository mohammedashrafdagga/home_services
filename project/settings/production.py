from .base import *



DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': config('DATABASE_PRODUCTION_NAME'),
       'USER': config('DATABASE_PRODUCTION_USER'),
       'PASSWORD': config('DATABASE_PRODUCTION_PASSWORD'),
       'HOST': config('DATABASE_PRODUCTION_HOST'),
       'PORT': config('DATABASE_PRODUCTION_PORT')

   }
}


ALLOWED_HOSTS = [config('production_host'),]