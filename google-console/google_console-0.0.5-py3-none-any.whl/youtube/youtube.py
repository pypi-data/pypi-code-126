from ._mixin import YouTubeMixin


class YouTube(YouTubeMixin):
    
    def __init__(self, client_secret_file: str, api_version: str, recreate_service: bool = False,
                 prefix: str = "", suffix: str = "", token_dir: str = ""):
        scopes = ["full.access"]
        super(YouTube, self).__init__("youtube", client_secret_file, api_version,
                                      scopes, recreate_service, prefix, suffix, token_dir)
