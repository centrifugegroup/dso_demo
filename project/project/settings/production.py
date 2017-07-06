"""
This is the settings file that you use when you're working on the production.
"""

from .base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = SECRET_KEY = os.getenv('DJANGO_SECRET_KEY','5g3bqc$yp(+$obzr^z2=49grt%_ke5xp6i#5f$v17v7aldr!nr')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
# DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
# }

# Postgresql settings for production, replace it with mysql if wish.
# We will use gunicorn post activate script to set this up

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('DATABASE_NAME', 'boh'),
        'USER': os.getenv('DATABASE_USER', 'boh'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD', 'Uber_S0cr4te'),
        'HOST': os.getenv('DATABASE_HOST', '127.0.0.1'),
        'PORT': os.getenv('DATABASE_PORT', '5432'),
    }
}

ALLOWED_HOSTS = ['127.0.0.1', '192.168.33.18']

# Email
# https://docs.djangoproject.com/en/1.8/topics/email/#smtp-backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

# STATIC_ROOT = os.path.join(BASE_DIR, os.pardir, os.pardir, 'static')
# MEDIA_ROOT = os.path.join(BASE_DIR, os.pardir, os.pardir, 'media')
