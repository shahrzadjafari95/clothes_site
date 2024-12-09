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


STATICFILES_DIRS = [
    BASE_DIR / "statics",
]

# settings in cpanel
STATIC_ROOT = '/home/bestblog/public_html/static'  # setting for collect statics command
MEDIA_ROOT = '/home/bestblog/public_html/media'


AUTHENTICATION_BACKENDS = [
    'accounts.backends.EmailOrUsernameModelBackend',  # Ensure this path is correct
    'django.contrib.auth.backends.ModelBackend',  # Default Django authentication backend
]

# Email setting for SMTP
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # e.g., 'smtp.gmail.com' for Gmail
EMAIL_PORT = 587  # or 465 for SSL
EMAIL_USE_TLS = True  # Use True if using TLS (587)
EMAIL_USE_SSL = False  # Use False if using TLS
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL')  # From email (same as host email)

