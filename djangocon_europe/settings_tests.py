# -*- coding: utf-8 -*-
from .settings import *  # NOQA

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
        'ADMINUSER': 'admin',
    },

}

RAVEN_CONFIG = {}
