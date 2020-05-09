import os
from dotenv import load_dotenv

load_dotenv()

APPLICATION_ENVIRONMENT = os.getenv('APPLICATION_ENVIRONMENT')
IMPORT_SETTINGS_ENVIRONMENT = 'from .' + APPLICATION_ENVIRONMENT + ' import *'
exec(IMPORT_SETTINGS_ENVIRONMENT)
