# base.py
MAINTENANCE_MODE = False  # Set to False when your site is live


COMPRESS_ENABLED = True  # Enable Django Compressor
COMPRESS_OFFLINE = True  # Enables offline compression (recommended for production)

# Static files settings
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'

