from pytpp import Scope
from pytpp.plugins import Authenticate, Features, logger
from pytpp.plugins.api import Aperture, WebSDK
import logging


logging.basicConfig(level=logging.DEBUG)

api = WebSDK('10.100.211.57', 'admin', 'newPassw0rd!', application_id='Unrestricted', scope=Scope().configuration(read=True))
api = WebSDK('10.100.211.57', 'admin', 'newPassw0rd!', application_id='Unrestricted', scope=Scope().configuration(read=True))
api = WebSDK('10.100.211.57', 'admin', 'newPassw0rd!', application_id='Unrestricted', scope=Scope().configuration(read=True))
