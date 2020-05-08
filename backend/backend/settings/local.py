"""
    Developer's desktop/workstation.
"""

from .base import *

print(__file__)

print('DEBUG', DEBUG)
DEBUG = bool(strtobool(os.getenv('DEBUG', 'True')))

print('ALLOWED_HOSTS', ALLOWED_HOSTS)
ALLOWED_HOSTS.append('localhost')
ALLOWED_HOSTS.append('127.0.0.1')

print('DATABASES', DATABASES)
DATABASES = {}
if 'DATABASES_DEFAULT' in os.environ:
    DATABASES['default'] = eval(os.getenv('DATABASES_DEFAULT'))
else:
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }

print('CORS_ORIGIN_ALLOW_ALL', CORS_ORIGIN_ALLOW_ALL)
CORS_ORIGIN_ALLOW_ALL = bool(strtobool(os.getenv('CORS_ORIGIN_ALLOW_ALL', 'False')))

print('CORS_ORIGIN_WHITELIST', CORS_ORIGIN_WHITELIST)
CORS_ORIGIN_WHITELIST.append('http://localhost:3000')

print('DEBUG', DEBUG)
print('ALLOWED_HOSTS', ALLOWED_HOSTS)
print('DATABASES', DATABASES)
print('CORS_ORIGIN_ALLOW_ALL', CORS_ORIGIN_ALLOW_ALL)
print('CORS_ORIGIN_WHITELIST', CORS_ORIGIN_WHITELIST)
