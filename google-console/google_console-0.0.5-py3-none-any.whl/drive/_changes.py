from .._pipeline import Base
from pprint import pprint as _pprint


class Changes(Base):
    
    def __init__(self, client_secret_file: str, api_version: str, recreate_service: bool = False,
                 prefix: str = "", suffix: str = "", token_dir: str = ""):
        scopes = []
        super(Changes, self).__init__("drive", client_secret_file, api_version,
                                      scopes, recreate_service, prefix, suffix, token_dir)
    
    def getStartPageToken(self):
        pass
    
    def list(self):
        pass
    
    def watch(self):
        pass
    