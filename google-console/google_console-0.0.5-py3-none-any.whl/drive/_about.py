from .._pipeline import Base
from pprint import pprint as _pprint


class About(Base):
    
    def __init__(self, client_secret_file: str, api_version: str, recreate_service: bool = False,
                 prefix: str = "", suffix: str = "", token_dir: str = ""):
        scopes = ["full.access"]
        super(About, self).__init__("drive", client_secret_file, api_version,
                                    scopes, recreate_service, prefix, suffix, token_dir)
    
    def get(self, fields: str = "*", pprint: bool = False):
        response = self.service.about().get(fields=fields).execute()
        return response if not pprint else _pprint(response)
    