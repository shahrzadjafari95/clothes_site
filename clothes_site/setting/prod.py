from .base import *
from decouple import config


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['www.best-blog-travel.ir', 'best-blog-travel.ir']

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases


# Database in CPANEL for production
DATABASES = {
    'default': {
        'ENGINE': config('DB_ENGINE', default='django.db.backends.mysql'),
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST', default='localhost'),  # Use 'localhost' by default
        'PORT': config('DB_PORT', cast=int, default=3306),  # Use 3306 by default
    }
}

