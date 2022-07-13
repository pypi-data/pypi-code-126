from fiopy.models.base import BaseModel
from fiopy.models.comment import CommentModel


class ReviewLinkItemModel(BaseModel):
    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        self._review_link_id = kwargs.get("review_link_id")
        self._asset_id = kwargs.get("asset_id")
        self._index = kwargs.get("index")

        self._inserted_at = kwargs.get("inserted_at")
        self._deleted_at = kwargs.get("deleted_at")
        self._updated_at = kwargs.get("updated_at")

        super().cleanup_values()

    @property
    def review_link_id(self):
        return self._review_link_id

    @property
    def asset_id(self):
        return self._asset_id

    @property
    def index(self):
        return self._index

    @property
    def inserted_at(self):
        return self._inserted_at

    @property
    def deleted_at(self):
        return self._deleted_at

    @property
    def updated_at(self):
        return self._updated_at

