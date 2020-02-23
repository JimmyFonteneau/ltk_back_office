from .base import *
import django_heroku
import dj_database_url

ALLOWED_HOSTS = ['los-artistos.herokuapp.com']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
DATABASES = {}
DATABASES['default'] = dj_database_url.config(conn_max_age=600)

django_heroku.settings(locals())
del DATABASES['default']['OPTIONS']['sslmode']