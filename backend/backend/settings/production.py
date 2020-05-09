"""
    Serves end-users/clients.
"""

from .base import *

# print(__file__)

DEBUG = bool(strtobool(os.getenv('DEBUG', 'False')))
