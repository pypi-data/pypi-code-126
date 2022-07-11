import os
try:
    import requests , user_agent , names , uuid , urllib , hashlib , instaloader , mechanize
except ModuleNotFoundError:
    os.system('pip install requests')
    os.system('pip install user_agent')
    os.system('pip install names')
    os.system('pip install urllib')
    os.system('pip install hashlib')
    os.system('pip install uuid')
    os.system('pip install instaloader')
    os.system('pip install mechanize')

from .gdo_drow import *
from .check_email import *
from .gdo_order import *
from .IG import *
from .info_face import *
from .info_tiktok import *
from .login import *