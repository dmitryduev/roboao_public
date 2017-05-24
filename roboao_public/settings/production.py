from __future__ import absolute_import, unicode_literals

from .base import *

DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!@q!f@k@fzn__w!tv0lwu#5=!)yy$y4$b8%@t#!ngk9jx8_hjo'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

LOGIN_REDIRECT_URL = '/admin'

# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True

# SECURE_SSL_REDIRECT = True

SECURE_BROWSER_XSS_FILTER = True

SECURE_CONTENT_TYPE_NOSNIFF = True

DEFAULT_FROM_EMAIL = 'roboao@caltech.edu'

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]', 'roboao.caltech.edu', '131.215.198.215', 'public_server']
# ALLOWED_HOSTS = ['*']

try:
    from .local import *
except ImportError:
    pass
