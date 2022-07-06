from .._pipeline import Base
from pprint import pprint as _pprint


# USERS
class Users(Base):
    
    def __init__(self, client_secret_file: str, api_version: str, recreate_service: bool = False,
                 prefix: str = "", suffix: str = "", token_dir: str = ""):
        scopes = ["full.access"]
        super(Users, self).__init__("gmail", client_secret_file, api_version,
                                    scopes, recreate_service, prefix, suffix, token_dir)
    
    def getProfile(self, user_id: str = "me", pprint: bool = False):
        profile_info = self.service.users().getProfile(userId=user_id).execute()
        return profile_info if not pprint else _pprint(profile_info)
    
    def stop(self, user_id: str = "me"):
        self.service.users().stop(userId=user_id).execute()
    
    def watch(self, user_id: str = "me", label_ids: list = None, label_filter_action=None, topic_name: str = None):
        request_body = {}
        self.service.users().watch(userId=user_id, body=request_body).execute()
