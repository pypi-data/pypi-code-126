from ._mixin import GmailMixin
from typing import List, Union


class Gmail(GmailMixin):
    
    def __init__(self, client_secret_file: str, api_version: str, recreate_service: bool = False,
                 prefix: str = "", suffix: str = "", token_dir: str = ""):
        scopes = ["full.access", "labels", "send", "readonly", "compose", "insert",
                  "modify", "settings.basic", "settings.sharing"]
        super(Gmail, self).__init__("gmail", client_secret_file, api_version,
                                    scopes, recreate_service, prefix, suffix, token_dir)
    
    # USERS
    def users_getProfile(self, user_id: str = "me", pprint: bool = False):
        self.users.getProfile(user_id, pprint)
    
    def users_stop(self):
        self.users.stop()
    
    def users_watch(self):
        self.users.watch()
    
    # DRAFTS
    def drafts_create(self, to: str, message: str, subject: str = None, file_attachment: Union[List[str], str] = None,
                      cc: str = None, bcc: str = None, message_mode: str = "plain", user_id: str = "me", pprint: bool = False):
        return self.drafts.create(to, message, subject, file_attachment, cc, bcc, message_mode, user_id, pprint)
    
    def drafts_delete(self, draft_id: str, user_id: str = "me"):
        self.drafts.delete(draft_id, user_id)
    
    def drafts_get(self, draft_id: str, format: str = "full", user_id: str = "me", pprint: bool = False):
        return self.drafts.get(draft_id, format, user_id, pprint)
    
    def drafts_list(self, include_spam_trash: bool = False, max_results: int = 500, q: str = None, user_id: str = "me", pprint: bool = False):
        return self.drafts.list(include_spam_trash, max_results, q, user_id, pprint)
    
    def drafts_send(self, draft_id: str, message: dict = None, user_id: str = "me", pprint: bool = False):
        return self.drafts.send(draft_id, message, user_id, pprint)
    
    def drafts_update(self, draft_id: str, to: str, message: str, subject: str = None, file_attachment: Union[List[str], str] = None,
                      cc: str = None, bcc: str = None, message_mode: str = "plain", user_id: str = "me", pprint: bool = False):
        self.drafts.update(draft_id, to, message, subject, file_attachment, cc, bcc, message_mode, user_id, pprint)
    
    # HISTORY
    def history_list(self):
        self.history.list()
    
    # LABELS
    def labels_create(self, name: str, label_list_visibility: str = "labelShow", message_list_visibility: str = "show",
                      user_id: str = "me", pprint: bool = False, **kwargs):
        return self.labels.create(name, label_list_visibility, message_list_visibility, user_id, pprint, **kwargs)
    
    def labels_delete(self, label_id: str = None, label_name: str = None, user_id: str = "me"):
        self.labels.delete(label_id, label_name, user_id)
    
    def labels_get(self, label_id: str = None, label_name: str = None, user_id: str = "me", pprint: bool = False):
        return self.labels.get(label_id, label_name, user_id, pprint)
    
    def labels_list(self, user_id: str = "me", pprint: bool = False):
        return self.labels.list(user_id, pprint)
    
    def labels_patch(self, label_id: str = None, label_name: str = None,
                     label_list_visibility: str = "labelShow", message_list_visibility: str = "show",
                     name: str = None, user_id: str = "me", pprint: bool = False, **kwargs):
        return self.labels.patch(label_id, label_name, label_list_visibility, message_list_visibility,
                                 name, user_id, pprint, **kwargs)
    
    def labels_update(self, label_id: str = None, label_name: str = None,
                      label_list_visibility: str = "labelShow", message_list_visibility: str = "show",
                      name: str = None, user_id: str = "me", pprint: bool = False, **kwargs):
        return self.labels.update(label_id, label_name, label_list_visibility, message_list_visibility,
                                  name, user_id, pprint, **kwargs)
    
    # MESSAGES
    def messages_batchDelete(self, messages_ids: list, user_id: str = "me"):
        self.messages.batchDelete(messages_ids, user_id)
    
    def messages_batchModify(self, messages_ids: list, add_label_ids: list = None, remove_label_ids: list = None, user_id: str = "me"):
        self.messages.batchModify(messages_ids, add_label_ids, remove_label_ids, user_id)
    
    def messages_delete(self, messages_id: str, user_id: str = "me"):
        self.messages.delete(messages_id, user_id)
    
    def messages_get(self, messages_id: str, user_id: str = "me", format: str = "minimal",
                     metadata_headers: list = None, pprint: bool = False):
        return self.messages.get(messages_id, user_id, format, metadata_headers, pprint)
    
    def messages_import(self):
        self.messages.import_()
    
    def messages_insert(self):
        self.messages.insert()
    
    def messages_list(self, max_results: int = 500, label_ids: str = None, include_spam_trash: bool = False,
                      q: str = None, user_id: str = "me", pprint: bool = False):
        return self.messages.list(max_results, label_ids, include_spam_trash, q, user_id, pprint)
    
    def messages_modify(self, messages_id: str, add_label_ids: list = None, remove_label_ids: list = None,
                        user_id: str = "me", pprint: bool = False):
        return self.messages.modify(messages_id, add_label_ids, remove_label_ids, user_id, pprint)
    
    def messages_send(self, to: str, message: str, subject: str = None, file_attachment: Union[List[str], str] = None,
                      cc: str = None, bcc: str = None, message_mode: str = "plain", user_id: str = "me", pprint: bool = False):
        return self.messages.send(to, message, subject, file_attachment, cc, bcc, message_mode, user_id, pprint)
    
    def messages_trash(self, messages_id: str, user_id: str = "me", pprint: bool = False):
        return self.messages.trash(messages_id, user_id, pprint)
    
    def messages_untrash(self, messages_id: str, user_id: str = "me", pprint: bool = False):
        return self.messages.untrash(messages_id, user_id, pprint)
    
    # MESSAGES ATTACHMENT
    def messages_attachment_get(self, messages_id: str, attachment_id: str, filename: str = None, decoded: bool = False,
                                user_id: str = "me", pprint: bool = False):
        return self.messages.attachment.get(messages_id, attachment_id, filename, decoded, user_id, pprint)

    def messages_attachment_get_all(self, messages_id: str, export: bool = True, decoded: bool = True, saving_dir: str = ""):
        return self.messages.attachment.get_all(messages_id, export, decoded, saving_dir)

    # SETTINGS
    def settings_getAutoForwarding(self, user_id: str = "me", pprint: bool = False):
        return self.settings.getAutoForwarding(user_id, pprint)
    
    def settings_getImap(self, user_id: str = "me", pprint: bool = False):
        return self.settings.getImap(user_id, pprint)
    
    def settings_getLanguage(self, user_id: str = "me", pprint: bool = False):
        return self.settings.getLanguage(user_id, pprint)
    
    def settings_getPop(self, user_id: str = "me", pprint: bool = False):
        return self.settings.getPop(user_id, pprint)
    
    def settings_getVacation(self, user_id: str = "me", pprint: bool = False):
        return self.settings.getVacation(user_id, pprint)
    
    def settings_updateAutoForwarding(self):
        self.settings.updateAutoForwarding()
    
    def settings_updateImap(self, auto_expunge: bool = True, enabled: bool = False, expunge_behavior: str = "archive",
                            max_folder_size: int = 0, user_id: str = "me", pprint: bool = False):
        return self.settings.updateImap(auto_expunge, enabled, expunge_behavior, max_folder_size, user_id, pprint)
    
    def settings_updateLanguage(self, display_language: str = "en", user_id: str = "me", pprint: bool = False):
        return self.settings.updateLanguage(display_language, user_id, pprint)
    
    def settings_updatePop(self, access_window: str = "disabled", disposition: str = "leaveInInbox",
                           user_id: str = "me", pprint: bool = False):
        return self.settings.updatePop(access_window, disposition, user_id, pprint)
    
    def settings_updateVacation(self):
        self.settings.updateVacation()
    
    # SETTINGS DELEGATES
    def settings_delegates_create(self):
        self.settings.delegates.create()
    
    def settings_delegates_get(self):
        self.settings.delegates.get()
    
    def settings_delegates_list(self):
        self.settings.delegates.list()

    # SETTINGS FILTERS
    def settings_filters_create(self):
        self.settings.filters.create()

    def settings_filters_delete(self):
        self.settings.filters.delete()

    def settings_filters_get(self):
        self.settings.filters.get()

    def settings_filters_list(self):
        self.settings.filters.list()

    # SETTINGS FORWARDING ADDRESS
    def settings_forwardingAddresses_create(self):
        self.settings.forwardingAddresses.create()

    def settings_forwardingAddresses_delete(self):
        self.settings.forwardingAddresses.delete()

    def settings_forwardingAddresses_get(self):
        self.settings.forwardingAddresses.get()

    def settings_forwardingAddresses_list(self):
        self.settings.forwardingAddresses.list()

    # SETTINGS SEND AS
    def settings_sendAs_create(self):
        self.settings.sendAs.create()

    def settings_sendAs_delete(self):
        self.settings.sendAs.delete()

    def settings_sendAs_get(self):
        self.settings.sendAs.get()

    def settings_sendAs_list(self):
        self.settings.sendAs.list()

    def settings_sendAs_patch(self):
        self.settings.sendAs.patch()

    def settings_sendAs_update(self):
        self.settings.sendAs.update()

    def settings_sendAs_verify(self):
        self.settings.sendAs.verify()

    # SETTINGS SEND AS SMIME INFO
    def settings_sendAs_smimeInfo_delete(self):
        self.settings.sendAs.smimeInfo.delete()

    def settings_sendAs_smimeInfo_get(self):
        self.settings.sendAs.smimeInfo.get()

    def settings_sendAs_smimeInfo_insert(self):
        self.settings.sendAs.smimeInfo.insert()

    def settings_sendAs_smimeInfo_list(self):
        self.settings.sendAs.smimeInfo.list()

    def settings_sendAs_smimeInfo_setDefault(self):
        self.settings.sendAs.smimeInfo.setDefault()

    # THREADS
    def threads_delete(self):
        self.threads.delete()

    def threads_get(self):
        self.threads.get()

    def threads_list(self):
        self.threads.list()

    def threads_modify(self):
        self.threads.modify()

    def threads_trash(self):
        self.threads.trash()

    def threads_untrash(self):
        self.threads.untrash()
    