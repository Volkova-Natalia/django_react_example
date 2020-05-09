"""
    Developer's desktop/workstation.
"""

from .base import *

# print(__file__)


DEBUG = bool(strtobool(os.getenv('DEBUG', 'True')))

ALLOWED_HOSTS.append('localhost')
ALLOWED_HOSTS.append('127.0.0.1')

DATABASES = {}
if 'DATABASES_DEFAULT' in os.environ:
    DATABASES['default'] = eval(os.getenv('DATABASES_DEFAULT'))
else:
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }

CORS_ORIGIN_ALLOW_ALL = bool(strtobool(os.getenv('CORS_ORIGIN_ALLOW_ALL', 'False')))

CORS_ORIGIN_WHITELIST.append('http://localhost:3000')
