from ._mixin import DriveMixin


class Drive(DriveMixin):
    
    def __init__(self, client_secret_file: str, api_version: str, recreate_service: bool = False,
                 prefix: str = "", suffix: str = "", token_dir: str = ""):
        scopes = ["full.access"]
        super(Drive, self).__init__("drive", client_secret_file, api_version,
                                    scopes, recreate_service, prefix, suffix, token_dir)
    
    def about_get(self, fields: str = "*", pprint: bool = False):
        return self.about.get(fields, pprint)
    