import os
import base64
import builtins
from .._pipeline import Base
from ._messages import Messages
from pprint import pprint as _pprint


# MESSAGES ATTACHMENT
class MessagesAttachment(Base):
    
    def __init__(self, client_secret_file: str, api_version: str, recreate_service: bool = False,
                 prefix: str = "", suffix: str = "", token_dir: str = ""):
        scopes = []
        super(MessagesAttachment, self).__init__("gmail", client_secret_file, api_version,
                                                 scopes, recreate_service, prefix, suffix, token_dir)
        
        try:
            __MIXIN__  # type: ignore
            remove = False
        except:
            builtins.__MIXIN__ = self.service
            remove = True
        
        args = (client_secret_file, api_version, recreate_service, prefix, suffix, token_dir)
        self.__messages = Messages(*args)
        
        if remove:
            del builtins.__MIXIN__  # type: ignore

    def get(self, messages_id: str, attachment_id: str, filename: str = None, decoded: bool = False,
            user_id: str = "me", pprint: bool = False):
        response = self.service.users().messages().attachments().get(userId=user_id,
                                                                     messageId=messages_id,
                                                                     id=attachment_id).execute()
        
        if (decoded and not pprint) or filename:
            response = base64.urlsafe_b64decode(response.get('data').encode('UTF-8'))
            
        if filename:
            with open(filename, "wb") as file:
                file.write(response)
            return
        
        return response if not pprint else _pprint(response)
    
    def get_all(self, messages_id: str, export: bool = True, decoded: bool = True, saving_dir: str = ""):
        message_info = self.__messages.get(messages_id, format="full", metadata_headers=["part"])
        message_payload = message_info.get('payload')
        
        files = {}
        if not os.path.exists(saving_dir) and export:
            os.mkdir(saving_dir)

        if 'parts' in message_payload:
            for payload in message_payload["parts"]:
                filename = payload["filename"]
                body = payload["body"]
                if 'attachmentId' in body:
                    attachment_id = body['attachmentId']
                    attachment_content = self.get(messages_id, attachment_id, decoded=decoded)
                    
                    if export:
                        with open(os.path.join(saving_dir, filename), 'wb') as file:
                            file.write(attachment_content)
                    else:
                        files[filename] = attachment_content
        
        if not export:
            return files
