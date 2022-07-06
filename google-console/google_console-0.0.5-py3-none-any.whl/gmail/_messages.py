from .._pipeline import Base
from ._base import PrivateMethods as _PrivateMethods
from typing import List, Union
from pprint import pprint as _pprint


# MESSAGES
class Messages(Base, _PrivateMethods):
    
    def __init__(self, client_secret_file: str, api_version: str, recreate_service: bool = False,
                 prefix: str = "", suffix: str = "", token_dir: str = ""):
        scopes = ["full.access", "labels", "send", "readonly", "compose", "insert",
                  "modify", "settings.basic", "settings.sharing"]
        super(Messages, self).__init__("gmail", client_secret_file, api_version,
                                       scopes, recreate_service, prefix, suffix, token_dir)
    
    def batchDelete(self, messages_ids: list, user_id: str = "me"):
        self.service.users().messages().batchDelete(userId=user_id, body={"ids": messages_ids}).execute()
    
    def batchModify(self, messages_ids: list, add_label_ids: list = None, remove_label_ids: list = None, user_id: str = "me"):
        if add_label_ids is None and remove_label_ids is None:
            raise ValueError("Required one of parameter (add_label_ids or remove_label_ids)")
        request_body = {"ids": messages_ids,
                        **({"addLabelIds": add_label_ids} if add_label_ids else {}),
                        **({"removeLabelIds": remove_label_ids} if remove_label_ids else {})}
        self.service.users().messages().batchModify(userId=user_id, body=request_body).execute()
    
    def delete(self, messages_id: str, user_id: str = "me"):
        self.service.users().messages().delete(userId=user_id, id=messages_id).execute()
    
    def get(self, messages_id: str, user_id: str = "me", format: str = "minimal",
            metadata_headers: list = None, pprint: bool = False):
        response = self.service.users().messages().get(userId=user_id, id=messages_id,
                                                       format=format, metadataHeaders=metadata_headers).execute()
        return response if not pprint else _pprint(response)
    
    def import_(self):
        pass
    
    def insert(self):
        pass
    
    def list(self, max_results: int = 500, label_ids: str = None, include_spam_trash: bool = False, q: str = None,
             user_id: str = "me", pprint: bool = False):
        response = self.service.users().messages().list(userId=user_id, includeSpamTrash=include_spam_trash,
                                                        maxResults=max_results, labelIds=label_ids, q=q).execute()
        messages = response.get("messages")
        nextPageToken = response.get("nextPageToken")

        while nextPageToken:
            response = self.service.users().messages().list(userId=user_id, includeSpamTrash=include_spam_trash,
                                                            maxResults=max_results, labelIds=label_ids, q=q,
                                                            pageToken=nextPageToken).execute()
            if response.get("messages"):
                messages.extend(response.get("messages"))
            nextPageToken = response.get("nextPageToken")

        return messages if not pprint else _pprint(messages)
    
    def modify(self, messages_id: str, add_label_ids: list = None, remove_label_ids: list = None,
               user_id: str = "me", pprint: bool = False):
        if add_label_ids is None and remove_label_ids is None:
            raise ValueError("Required one of parameter (add_label_ids or remove_label_ids)")
        request_body = {**({"addLabelIds": add_label_ids} if add_label_ids else {}),
                        **({"removeLabelIds": remove_label_ids} if remove_label_ids else {})}
        response = self.service.users().messages().modify(userId=user_id, id=messages_id, body=request_body).execute()
        return response if not pprint else _pprint(response)
    
    def send(self, to: str, message: str, subject: str = None, file_attachment: Union[List[str], str] = None,
             cc: str = None, bcc: str = None, message_mode: str = "plain", user_id: str = "me", pprint: bool = False):
        raw_string = self._create_email(to, message, subject, file_attachment, cc, bcc, message_mode)
        response = self.service.users().messages().send(userId=user_id, body={"raw": raw_string}).execute()
        return response if not pprint else _pprint(response)
    
    def trash(self, messages_id: str, user_id: str = "me", pprint: bool = False):
        response = self.service.users().messages().trash(userId=user_id, id=messages_id).execute()
        return response if not pprint else _pprint(response)
    
    def untrash(self, messages_id: str, user_id: str = "me", pprint: bool = False):
        response = self.service.users().messages().untrash(userId=user_id, id=messages_id).execute()
        return response if not pprint else _pprint(response)
