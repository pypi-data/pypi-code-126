from deepmerge import Merger


class ProjectSettings:
    def __init__(self):
        self._settings = {
            "project": {"name": "", "private": "0", "team_id": "JTNullValue", "shared": "0", "ignore_archive": "0"},
            "project_preferences": {
                "collaborator_can_download": "1",
                "collaborator_can_invite": "1",
                "collaborator_can_share": "1",
                "email_for_new_comment": "1",
                "email_for_new_person": "1",
                "email_for_new_video": "1",
                "notify_on_updated_label": "1",
            },
            "preferences": {
                "email_for_new_comment": "1",
                "email_for_new_person": "1",
                "email_for_new_video": "1",
                "notify_on_updated_label": "1",
            },
            "slack_notifications_pref": "0",
            "private": "0",
        }

    def update(self, *, new_settings):
        merger = Merger([(list, ["append"]), (dict, ["merge"])], ["override"], ["override"])
        merger.merge(self._settings, new_settings)

    @property
    def settings(self):
        return self._settings

    @property
    def name(self):
        return self._settings["project"]["name"]

    @name.setter
    def name(self, value):
        self._settings["project"]["name"] = value

    @property
    def private(self):
        return self._settings["project"]["private"]

    @private.setter
    def private(self, value):
        self._settings["project"]["private"] = "0" if value == False else "1"
        self._settings["preferences"]["private"] = "0" if value == False else "1"

    @property
    def team_id(self):
        return self._settings["project"]["team_id"]

    @team_id.setter
    def team_id(self, value):
        self._settings["project"]["team_id"] = value

    @property
    def shared(self):
        return self._settings["project"]["shared"]

    @shared.setter
    def shared(self, value):
        self._settings["project"]["shared"] = "0" if value == False else "1"

    @property
    def ignore_archive(self):
        return self._settings["project"]["ignore_archive"]

    @ignore_archive.setter
    def ignore_archive(self, value):
        self._settings["project"]["ignore_archive"] = "0" if value == False else "1"

    @property
    def collaborator_can_download(self):
        return self._settings["project_preferences"]["collaborator_can_download"]

    @collaborator_can_download.setter
    def collaborator_can_download(self, value):
        self._settings["project_preferences"]["collaborator_can_download"] = "0" if value == False else "1"

    @property
    def collaborator_can_invite(self):
        return self._settings["project_preferences"]["collaborator_can_invite"]

    @collaborator_can_invite.setter
    def collaborator_can_invite(self, value):
        self._settings["project_preferences"]["collaborator_can_invite"] = "0" if value == False else "1"

    @property
    def collaborator_can_share(self):
        return self._settings["project_preferences"]["collaborator_can_share"]

    @collaborator_can_share.setter
    def collaborator_can_share(self, value):
        self._settings["project_preferences"]["collaborator_can_share"] = "0" if value == False else "1"

    @property
    def email_for_new_comment(self):
        return self._settings["project_preferences"]["email_for_new_comment"]

    @email_for_new_comment.setter
    def email_for_new_comment(self, value):
        self._settings["project_preferences"]["email_for_new_comment"] = "0" if value == False else "1"
        self._settings["preferences"]["email_for_new_comment"] = "0" if value == False else "1"

    @property
    def email_for_new_person(self):
        return self._settings["project_preferences"]["email_for_new_person"]

    @email_for_new_person.setter
    def email_for_new_person(self, value):
        self._settings["project_preferences"]["email_for_new_person"] = "0" if value == False else "1"
        self._settings["preferences"]["email_for_new_person"] = "0" if value == False else "1"

    @property
    def email_for_new_video(self):
        return self._settings["project_preferences"]["email_for_new_video"]

    @email_for_new_video.setter
    def email_for_new_video(self, value):
        self._settings["project_preferences"]["email_for_new_video"] = "0" if value == False else "1"
        self._settings["preferences"]["email_for_new_video"] = "0" if value == False else "1"

    @property
    def notify_on_updated_label(self):
        return self._settings["project_preferences"]["notify_on_updated_label"]

    @notify_on_updated_label.setter
    def notify_on_updated_label(self, value):
        self._settings["project_preferences"]["notify_on_updated_label"] = "0" if value == False else "1"
        self._settings["preferences"]["notify_on_updated_label"] = "0" if value == False else "1"

    @property
    def slack_notifications_pref(self):
        return self._settings["preferences"]["slack_notifications_pref"]

    @slack_notifications_pref.setter
    def slack_notifications_pref(self, value):
        self._settings["preferences"]["slack_notifications_pref"] = "0" if value == False else "1"

