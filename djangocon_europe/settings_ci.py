# -*- coding: utf-8 -*-
from .settings import *  # NOQA

ALLOWED_HOSTS = ['*', ]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'travis_ci_test',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5432',
        'ADMINUSER': 'admin',
    },
}

RAVEN_CONFIG = {}
