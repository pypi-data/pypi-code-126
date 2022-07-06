from .._pipeline import Base
from pprint import pprint as _pprint


class Files(Base):
    
    def __init__(self, client_secret_file: str, api_version: str, recreate_service: bool = False,
                 prefix: str = "", suffix: str = "", token_dir: str = ""):
        scopes = ["full.access"]
        super(Files, self).__init__("drive", client_secret_file, api_version,
                                    scopes, recreate_service, prefix, suffix, token_dir)
    
    def create(self, metadata: dict = None, upload_files: list[str] = None, pprint: bool = False):
        request_body = {**metadata}
        response = self.service.files().create().execute()
        return response if not pprint else _pprint(response)
    