from .._pipeline import Base
from pprint import pprint as _pprint


# SETTINGS
class Settings(Base):
    
    def __init__(self, client_secret_file: str, api_version: str, recreate_service: bool = False,
                 prefix: str = "", suffix: str = "", token_dir: str = ""):
        scopes = []
        super(Settings, self).__init__("gmail", client_secret_file, api_version,
                                       scopes, recreate_service, prefix, suffix, token_dir)
    
    def getAutoForwarding(self, user_id: str = "me", pprint: bool = False):
        response = self.service.users().settings().getAutoForwarding(userId=user_id).execute()
        return response if not pprint else _pprint(response)
    
    def getImap(self, user_id: str = "me", pprint: bool = False):
        response = self.service.users().settings().getImap(userId=user_id).execute()
        return response if not pprint else _pprint(response)
    
    def getLanguage(self, user_id: str = "me", pprint: bool = False):
        response = self.service.users().settings().getLanguage(userId=user_id).execute()
        return response if not pprint else _pprint(response)
    
    def getPop(self, user_id: str = "me", pprint: bool = False):
        response = self.service.users().settings().getPop(userId=user_id).execute()
        return response if not pprint else _pprint(response)
    
    def getVacation(self, user_id: str = "me", pprint: bool = False):
        response = self.service.users().settings().getVacation(userId=user_id).execute()
        return response if not pprint else _pprint(response)
    
    def updateAutoForwarding(self, enabled: bool = False, email_address: str = None, disposition: str = None,
                             user_id: str = "me", pprint: bool = False):
        pass
        # request_body = {"enabled": enabled,
        #                 "emailAddress": email_address,
        #                 "disposition": disposition}
        # response = self.service.users().settings().updateAutoForwarding(userId=user_id, body=request_body).execute()
        # return response if not pprint else _pprint(response)
    
    def updateImap(self, auto_expunge: bool = True, enabled: bool = False, expunge_behavior: str = "archive",
                   max_folder_size: int = 0, user_id: str = "me", pprint: bool = False):
        request_body = {"autoExpunge": auto_expunge,
                        "enabled": enabled,
                        "expungeBehavior": expunge_behavior,
                        "maxFolderSize": max_folder_size}
        response = self.service.users().settings().updateImap(userId=user_id, body=request_body).execute()
        return response if not pprint else _pprint(response)
    
    def updateLanguage(self, display_language: str = "en", user_id: str = "me", pprint: bool = False):
        response = self.service.users().settings().updateLanguage(userId=user_id,
                                                                  body={"displayLanguage": display_language}).execute()
        return response if not pprint else _pprint(response)
    
    def updatePop(self, access_window: str = "disabled", disposition: str = "leaveInInbox", user_id: str = "me", pprint: bool = False):
        response = self.service.users().settings().updatePop(userId=user_id,
                                                             body={"accessWindow": access_window,
                                                                   "disposition": disposition}).execute()
        return response if not pprint else _pprint(response)
    
    def updateVacation(self):
        pass
