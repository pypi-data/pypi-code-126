from fiopy.models.base_folder import BaseFolderModel


class ProjectRootFolderModel(BaseFolderModel):
    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        self._size = kwargs.get("size")

        self._archived_at = kwargs.get("archived_at")
        self._copy = kwargs.get("copy")
        self._creator_id = kwargs.get("creator_id")

    @property
    def size(self):
        return self._size

    @property
    def archived_at(self):
        return self._archived_at

    @property
    def copy(self):
        return self._copy

    @property
    def creator_id(self):
        return self._creator_id

