# base.py
MAINTENANCE_MODE = False  # Set to False when your site is live


COMPRESS_ENABLED = True  # Enable Django Compressor
COMPRESS_OFFLINE = True  # Enables offline compression (recommended for production)

# Static files settings
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'

STATICFILES_DIRS = [
    BASE_DIR / "statics",  # Your uncompressed CSS/JS
]

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',  # Default finder
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',  # Default finder
    'compressor.finders.CompressorFinder',  # Required for Django Compressor
]


# Django Compressor settings
COMPRESS_ROOT = STATIC_ROOT
COMPRESS_URL = STATIC_URL
COMPRESS_STORAGE = 'compressor.storage.CompressorFileStorage'

