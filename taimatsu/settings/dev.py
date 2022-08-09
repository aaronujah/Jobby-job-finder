from .base import *
import os

SECRET_KEY = 'SECRET_KEY'

DEBUG = True

ALLOWED_HOSTS = ['*']

STATIC_URL = 'static/'

STATIC_ROOT = BASE_DIR / 'staticfiles' 

MEDIA_URL = 'images/' 

MEDIA_ROOT = BASE_DIR / 'static/images' 