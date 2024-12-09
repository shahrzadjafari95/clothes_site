from .base import *

# SECURITY WARNING: don't run with debug turned off in development!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# sitemap setting
SITE_ID = 2

# Static and Media files handling for development
STATIC_ROOT = BASE_DIR / 'static'  # setting for collect statics command
MEDIA_ROOT = BASE_DIR / 'media'

STATICFILES_DIRS = [
    BASE_DIR / "statics",
]

