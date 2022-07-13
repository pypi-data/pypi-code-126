from fiopy.models.base_container import BaseContainerModel


class BaseAssetModel(BaseContainerModel):
    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        self._archived_at = kwargs.get("archived_at")
        self._autoversion_id = kwargs.get("autoversion_id")
        self._comment_count = kwargs.get("comment_count")
        self._copy = kwargs.get("copy")

        self._deleted_at = kwargs.get("deleted_at")
        self._description = kwargs.get("description")

        self._duration = kwargs.get("duration")
        self._filesize = kwargs.get("filesize")
        self._filetype = kwargs.get("filetype")
        self._fps = kwargs.get("fps")
        self._frames = kwargs.get("frames")

        self._is_360 = kwargs.get("is_360")
        self._label = kwargs.get("label")

        self._private = kwargs.get("private")
        self._properties = kwargs.get("properties")
        self._rating = kwargs.get("rating")

    @property
    def archived_at(self):
        return self._archived_at

    @property
    def autoversion_id(self):
        return self._autoversion_id

    @property
    def comment_count(self):
        return self._comment_count

    @property
    def copy(self):
        return self._copy

    @property
    def deleted_at(self):
        return self._deleted_at

    @property
    def description(self):
        return self._description

    @property
    def duration(self):
        return self._duration

    @property
    def filesize(self):
        return self._filesize

    @property
    def filetype(self):
        return self._filetype

    @property
    def fps(self):
        return self._fps

    @property
    def frames(self):
        return self._frames

    @property
    def is_360(self):
        return self._is_360

    @property
    def label(self):
        return self._label

    @property
    def private(self):
        return self._private

    @property
    def properties(self):
        return self._properties

    @property
    def rating(self):
        return self._rating

