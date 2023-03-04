from .base import *
from .wsgi import env

if env == 'Coming_soon.dev':

    DEBUG = bool(os.getenv('DEVELOPMENT_DEBUG'))

    print('looks like you are on development')

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'loggers': {
            'django': {
                'handlers': ['file'],
                'level': 'DEBUG'
            }
        },
        'handlers': {
            'file': {
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'filename': './logs/debug.log',
                'formatter': 'simple',
            }
        },
        'formatters': {
            'simple': {
                'format': '{levelname} {message}',
                'style': '{',
            }
        },

    }
