from .base import *



DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': config('DATABASE_LOCAL_NAME'),
       'USER': config('DATABASE_LOCAL_USER'),
       'PASSWORD': config('DATABASE_LOCAL_PASSWORD'),
       'HOST': config('DATABASE_LOCAL_HOST'),
       'PORT': config('DATABASE_LOCAL_PORT'),
       'OPTIONS': {
            'options': '-c search_path=public',
        },
        'TEST': {
            'CHARSET': 'utf8',
        },
   }
}

ALLOWED_HOSTS = ['*']