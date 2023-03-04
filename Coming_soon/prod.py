from .base import *
from .wsgi import env


if env == 'Coming_soon.prod':

    DEBUG = bool(os.getenv('PRODUCTION_DEBUG'))

    CSRF_COOKIE_SECURE = bool(os.getenv('CSRF_COOKIE_SECURE'))

    SECURE_SSL_REDIRECT = bool(os.getenv('SECURE_SSL_REDIRECT'))

    SESSION_COOKIE_SECURE = bool(os.getenv('SESSION_COOKIE_SECURE'))

    print('looks like you are on production')
