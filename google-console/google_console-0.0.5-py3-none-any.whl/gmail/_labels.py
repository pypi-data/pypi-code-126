from .._pipeline import Base
from pprint import pprint as _pprint


# LABELS
class Labels(Base):
    
    def __init__(self, client_secret_file: str, api_version: str, recreate_service: bool = False,
                 prefix: str = "", suffix: str = "", token_dir: str = ""):
        scopes = []
        super(Labels, self).__init__("gmail", client_secret_file, api_version,
                                     scopes, recreate_service, prefix, suffix, token_dir)
    
    def create(self, name: str, label_list_visibility: str = "labelShow", message_list_visibility: str = "show",
               user_id: str = "me", pprint: bool = False, **kwargs):
        request_body = {"labelListVisibility": label_list_visibility,
                        "messageListVisibility": message_list_visibility,
                        "name": name, **kwargs}
        response = self.service.users().labels().create(userId=user_id, body=request_body).execute()
        return response if not pprint else _pprint(response)
    
    def delete(self, label_id: str = None, label_name: str = None, user_id: str = "me"):
        label_info = self.get(label_name=label_name) if label_name else {"id": label_id}
        self.service.users().labels().delete(userId=user_id, id=label_info.get("id")).execute()
    
    def get(self, label_id: str = None, label_name: str = None, user_id: str = "me", pprint: bool = False):
        if label_id:
            pass
        elif label_name:
            print("This process can take a little while!")
            _labels = self.list()

            label = {x.get("id"): x.get("name") for x in _labels if x.get("name") == label_name}
            if label:
                label_id = next(iter(label))
            else:
                raise ValueError("Label does not exist!")
        else:
            raise ValueError("Required one of parameter (label_id or label_name)")

        response = self.service.users().labels().get(userId=user_id, id=label_id).execute()
        return response if not pprint else _pprint(response)
    
    def list(self, user_id: str = "me", pprint: bool = False):
        response = self.service.users().labels().list(userId=user_id).execute().get("labels")
        return response if not pprint else _pprint(response)
    
    def patch(self, label_id: str = None, label_name: str = None, label_list_visibility: str = "labelShow",
              message_list_visibility: str = "show", name: str = None, user_id: str = "me", pprint: bool = False, **kwargs):
        response = self.__patch_n_update(label_id, label_name, label_list_visibility,
                                         message_list_visibility, name, user_id, **kwargs)
        return response if not pprint else _pprint(response)
    
    def update(self, label_id: str = None, label_name: str = None, label_list_visibility: str = "labelShow",
               message_list_visibility: str = "show", name: str = None, user_id: str = "me", pprint: bool = False, **kwargs):
        response = self.__patch_n_update(label_id, label_name, label_list_visibility,
                                         message_list_visibility, name, user_id, **kwargs)
        return response if not pprint else _pprint(response)
    
    # PRIVATE METHOD
    def __patch_n_update(self, label_id, label_name, label_list_visibility, message_list_visibility, name, user_id, **kwargs):
        label_info = self.get(label_name=label_name) if label_name else {"id": label_id}
        request_body = {**({"labelListVisibility": label_list_visibility} if label_list_visibility else {}),
                        **({"messageListVisibility": message_list_visibility} if message_list_visibility else {}),
                        **({"name": name} if name else {}), **kwargs}
        response = self.service.users().labels().update(userId=user_id,
                                                        id=label_info.get("id"), body=request_body).execute()
        return response
