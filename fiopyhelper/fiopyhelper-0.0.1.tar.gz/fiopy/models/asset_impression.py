from fiopy.models.base import BaseModel


class AssetImpression(BaseModel):
    def __init__(self, **kwargs):

        super().__init__(**kwargs)
        self._anonymous_user_id = kwargs.get("anonymous_user_id")
        self._asset_id = kwargs.get("asset_id")
        self._count = kwargs.get("count")
        self._deleted_at = kwargs.get("deleted_at")
        self._inserted_at = kwargs.get("inserted_at")
        self._review_link_id = kwargs.get("review_link_id")
        self._type = kwargs.get("type")
        self._updated_at = kwargs.get("updated_at")
        self._user_id = kwargs.get("user_id")

        super().cleanup_values()

    @property
    def anonymous_user_id(self):
        return self._anonymous_user_id

    @property
    def asset_id(self):
        return self._asset_id

    @property
    def count(self):
        return self._count

    @property
    def deleted_at(self):
        return self._deleted_at

    @property
    def inserted_at(self):
        return self._inserted_at

    @property
    def review_link_id(self):
        return self._review_link_id

    @property
    def type(self):
        return self._type

    @property
    def updated_at(self):
        return self._updated_at

    @property
    def user_id(self):
        return self._user_id

