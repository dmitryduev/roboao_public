from __future__ import absolute_import, unicode_literals

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!@q!f@k@fzn__w!tv0lwu#5=!)yy$y4$b8%@t#!ngk9jx8_hjo'


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

LOGIN_REDIRECT_URL = '/admin'


try:
    from .local import *
except ImportError:
    pass
