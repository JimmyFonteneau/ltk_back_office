from .base import *

ALLOWED_HOSTS = ['127.0.0.1']
URL_TEST = 'http://127.0.0.1:8000/'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# EMAIL_HOST = "127.0.0.1"
# EMAIL_PORT = 1025