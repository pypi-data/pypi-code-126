from .._pipeline import Base
from ._base import PrivateMethods
from typing import List, Union
from pprint import pprint as _pprint


# DRAFT
class Drafts(Base, PrivateMethods):
    
    def __init__(self, client_secret_file: str, api_version: str, recreate_service: bool = False,
                 prefix: str = "", suffix: str = "", token_dir: str = ""):
        scopes = ["full.access"]
        super(Drafts, self).__init__("gmail", client_secret_file, api_version,
                                     scopes, recreate_service, prefix, suffix, token_dir)

    def create(self, to: str, message: str, subject: str = None, file_attachment: Union[List[str], str] = None,
               cc: str = None, bcc: str = None, message_mode: str = "plain", user_id: str = "me", pprint: bool = False):
        raw_string = self._create_email(to, message, subject, file_attachment, cc, bcc, message_mode)
        response = self.service.users().drafts().create(userId=user_id, body={"message": {"raw": raw_string}}).execute()
        return response if not pprint else _pprint(response)
    
    def delete(self, draft_id: str, user_id: str = "me"):
        self.service.users().drafts().delete(userId=user_id, id=draft_id).execute()
    
    def get(self, draft_id: str, format: str = "full", user_id: str = "me", pprint: bool = False):
        response = self.service.users().drafts().get(userId=user_id, id=draft_id, format=format).execute()
        return response if not pprint else _pprint(response)
    
    def list(self, include_spam_trash: bool = False, max_results: int = 500, q: str = None, user_id: str = "me", pprint: bool = False):
        response = self.service.users().drafts().list(userId=user_id, includeSpamTrash=include_spam_trash, q=q,
                                                      maxResults=max_results).execute()
        drafts = response.get("drafts")
        nextPageToken = response.get("nextPageToken")
        
        while nextPageToken:
            response = self.service.users().drafts().list(userId=user_id, includeSpamTrash=include_spam_trash, q=q,
                                                          maxResults=max_results, pageToken=nextPageToken).execute()
            if response.get("drafts"):
                drafts.extend(response.get("drafts"))
            nextPageToken = response.get("nextPageToken")
        
        return drafts if not pprint else _pprint(drafts)
    
    def send(self, draft_id: str, message: dict = None, user_id: str = "me", pprint: bool = False):
        request_body = {"id": draft_id, **({"message": message} if message else {})}
        response = self.service.users().drafts().send(userId=user_id, body=request_body).execute()
        return response if not pprint else _pprint(response)
    
    def update(self, draft_id: str, to: str, message: str, subject: str = None, file_attachment: Union[List[str], str] = None,
               cc: str = None, bcc: str = None, message_mode: str = "plain", user_id: str = "me", pprint: bool = False):
        raw_string = self._create_email(to, message, subject, file_attachment, cc, bcc, message_mode)
        response = self.service.users().drafts().update(userId=user_id, id=draft_id,
                                                        body={"message": {"raw": raw_string}}).execute()
        return response if not pprint else _pprint(response)
