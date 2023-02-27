# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

from .base import *


DEBUG = True

ALLOWED_HOSTS = []



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbbiblioteca',
        'USER': 'promx123',
        'PASSWORD':'facundogus123',
        'HOST':'localhost',
        'PORT':'5432',
        
    }
}

STATIC_URL = '/static/'
STATICFILES_DIRS = [
     BASE_DIR / "../static"
]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / '../media'


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
