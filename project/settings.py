import os
from decouple import config, Csv

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('POSTGRES_NAME', default='checkpoint'),
        'USER': config('POSTGRES_USER', default='guard'),
        'PASSWORD': config('POSTGRES_PASSWORD', default='osim5'),
        'HOST': config('POSTGRES_HOST', default='checkpoint.devman.org'),
        'PORT': config('POSTGRES_PORT', default='5434'),
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = config('SECRET_KEY', default='default_secret_key_not_secure')

DEBUG = config('DEBUG', default=True, cast=bool)

ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv(), default='localhost')


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Samara'

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
