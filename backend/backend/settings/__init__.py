# from .local import *
# from .development import *
# from .integration import *
# from .testing import *
# from .staging import *
# from .production import *

import os
from dotenv import load_dotenv

load_dotenv()

APPLICATION_ENVIROMENT = os.getenv('APPLICATION_ENVIROMENT')
# print('APPLICATION_ENVIROMENT', APPLICATION_ENVIROMENT)
IMPORT_SETTINGS_ENVIROMENT = 'from .' + APPLICATION_ENVIROMENT + ' import *'
# print('IMPORT_SETTINGS_ENVIROMENT', IMPORT_SETTINGS_ENVIROMENT)
exec(IMPORT_SETTINGS_ENVIROMENT)
