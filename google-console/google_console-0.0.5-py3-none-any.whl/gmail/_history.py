from .._pipeline import Base


# HISTORY
class History(Base):
    
    def __init__(self, client_secret_file: str, api_version: str, recreate_service: bool = False,
                 prefix: str = "", suffix: str = "", token_dir: str = ""):
        scopes = []
        super(History, self).__init__("gmail", client_secret_file, api_version,
                                      scopes, recreate_service, prefix, suffix, token_dir)
    
    def list(self, history_types: str = "messageAdded", label_id: str = None, max_results: int = 500,
             start_history_id: str = None, user_id: str = "me"):
        self.service.users().history().list().execute()
