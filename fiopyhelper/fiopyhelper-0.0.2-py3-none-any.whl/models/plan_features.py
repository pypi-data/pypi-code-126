from fiopy.models.base import BaseModel

__all__ = ["PlanFeaturesModel"]


class PlanFeaturesModel(BaseModel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._custom_branded_emails = kwargs.get("custom_branded_emails")
        self._custom_branded_presentations = kwargs.get("custom_branded_presentations")
        self._reel_player = kwargs.get("reel_player")
        self._team_only_comments = kwargs.get("team_only_comments")
        self._archival_storage = kwargs.get("archival_storage")
        self._session_based_watermarking = kwargs.get("session_based_watermarking") 
        self._secure_sharing = kwargs.get("secure_sharing")
        super().cleanup_values()

    @property
    def custom_branded_emails(self):
        return self._custom_branded_emails

    @property
    def custom_branded_presentations(self):
        return self._custom_branded_presentations

    @property
    def reel_player(self):
        return self._reel_player

    @property
    def team_only_comments(self):
        return self._team_only_comments

    @property
    def archival_storage(self):
        return self._archival_storage
 
    @property
    def session_based_watermarking(self):
        return self._session_based_watermarking

    @property
    def secure_sharing(self):
        return self._secure_sharing
