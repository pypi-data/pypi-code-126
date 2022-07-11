#
# Copyright 2022 DataRobot, Inc. and its affiliates.
#
# All rights reserved.
#
# DataRobot, Inc.
#
# This is proprietary source code of DataRobot, Inc. and its
# affiliates.
#
# Released under the terms of DataRobot Tool and Utility Agreement.
from typing import List, Optional, Union

import trafaret as t

from datarobot.enums import PROJECT_STAGE
from datarobot.models.api_object import APIObject
from datarobot.models.project import Project

__all__ = ["DocumentThumbnailFile", "DocumentThumbnail"]


class DocumentThumbnailFile(APIObject):
    """Thumbnail file of a document contained in the project dataset.

    Attributes
    ----------
    project_id : str
        ID of the project record belongs to.
    document_page_id : str
        ID of the document page.
    height : int
         Height of the document thumbnail in pixels.
    width : int
         Width of the document thumbnail in pixels.
    thumbnail_bytes : bytes
        Raw bytes of the document thumbnail image. Accessing this may
        require a server request and an associated delay in fetching the resource.
    mime_type : str
        Mime image type of the document thumbnail. Example: `'image/png'`
    """

    _bytes_path = "projects/{project_id}/documentPages/{document_page_id}/file/"

    _converter = t.Dict(
        {
            t.Key("project_id", optional=True): t.String(),
            t.Key("document_page_id", optional=True): t.String(),
            t.Key("height", optional=True): t.Int(),
            t.Key("width", optional=True): t.Int(),
        }
    ).ignore_extra("*")

    def __init__(
        self,
        project_id: str,
        document_page_id: str,
        height: int = 0,
        width: int = 0,
    ):
        self.project_id = project_id
        self.document_page_id = document_page_id
        self.height = height
        self.width = width
        self.__thumbnail_bytes: bytes
        self.__mime_type: str

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}(project_id={self.project_id}, document_page_id={self.document_page_id}, "
            f"height={self.height}, width={self.width})"
        )

    @property
    def thumbnail_bytes(self) -> bytes:
        """Document thumbnail as bytes.

        Returns
        -------
        bytes
            Document thumbnail.
        """
        if not getattr(self, "__thumbnail_bytes", None):
            self.__get_thumbnail_bytes()
        return self.__thumbnail_bytes

    @property
    def mime_type(self) -> str:
        """Mime image type of the document thumbnail. Example: `'image/png'`

        Returns
        -------
        str
            Mime image type of the document thumbnail.
        """
        if not getattr(self, "__mime_type", None):
            # Getting and setting thumbnail bytes also gets and sets mime type
            self.__get_thumbnail_bytes()
        return self.__mime_type

    def __get_thumbnail_bytes(self) -> None:
        """Method that fetches document thumbnail from the server and
         sets the `mime_type` and `thumbnail_bytes` properties.

        Returns
        -------
        None
        """
        path = self._bytes_path.format(
            project_id=self.project_id, document_page_id=self.document_page_id
        )
        r_data = self._client.get(path)
        self.__mime_type = r_data.headers.get("Content-Type")
        self.__thumbnail_bytes = r_data.content


class DocumentThumbnail(APIObject):
    """Thumbnail of document from the project's dataset.

    If ``Project.stage`` is ``datarobot.enums.PROJECT_STAGE.EDA2``
    and it is a supervised project then the ``target_*`` attributes
    of this class will have values, otherwise the values will all be None.

    Attributes
    ----------
    document: Document
        Document object.
    project_id : str
        ID of the project record belongs to.
    target_value: str
        Target value used for filtering thumbnails.
    """

    _list_eda_sample_path = "projects/{project_id}/documentThumbnailSamples/"
    _list_project_sample_path = "projects/{project_id}/documentThumbnails/"

    _converter = t.Dict(
        {
            t.Key("project_id", optional=True): t.String(),
            t.Key("document_page_id", optional=True): t.String(),
            t.Key("height", optional=True): t.Int(),
            t.Key("width", optional=True): t.Int(),
            t.Key("target_value", optional=True): t.Or(
                t.String(), t.Int(), t.Float(), t.List(t.String())
            ),
        }
    ).ignore_extra("*")

    def __init__(
        self,
        project_id: str,
        document_page_id: str,
        height: int = 0,
        width: int = 0,
        target_value: Optional[Union[str, int, float, List[str]]] = None,
    ):
        self.document = DocumentThumbnailFile(
            project_id=project_id, document_page_id=document_page_id, height=height, width=width
        )
        self.project_id = project_id
        self.target_value = target_value

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}(project_id={self.project_id}, "
            f"document_page_id={self.document.document_page_id}, target_value={self.target_value})"
        )

    @classmethod
    def list(
        cls,
        project_id: str,
        feature_name: str,
        target_value: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
    ) -> List["DocumentThumbnail"]:
        """Get document thumbnails from a project.

        Parameters
        ----------
        project_id : str
            ID of the project record belongs to.
        feature_name : str
            Name of feature column that contains document type.
        target_value : Optional[str], default ``None``
            Target value to filter thumbnails.
        offset : Optional[int], default ``None``
            Number of documents to be skipped.
        limit : Optional[int], default ``None``
            Number of document thumbnails to return.

        Returns
        -------
        documents : List[DocumentThumbnail]
            List of ``DocumentThumbnail`` objects each representing a single document.

        Notes
        -----
        Actual document thumbnails are not fetched from the server by this method
        but just ``DocumentThumbnailFile`` object constructs that when accessed later on will fetch
        the thumbnail on demand (lazy loading).

        Examples
        --------

        Fetch document thumbnails for the given ``project_id`` and ``feature_name``.

        .. code-block:: python

            from datarobot._experimental.models.documentai.document import DocumentThumbnail

            # fetch 5 documents from EDA SAMPLE for specified project and specific feature
            document_thumbs = DocumentThumbnail.list(project_id, feature_name, limit=5)

            # fetch 5 documents for specified project with target value filtering
            # this option is only available after project target was selected and modeling started
            target1_thumbs = DocumentThumbnail.list(project_id, feature_name, target_value='target1', limit=5)


        Preview the document thumbnail.

        .. code-block:: python

            from datarobot._experimental.models.documentai.document import DocumentThumbnail
            from datarobot.helpers.image_utils import get_image_from_bytes

            # fetch 3 documents
            document_thumbs = DocumentThumbnail.list(project_id, feature_name, limit=3)

            for doc_thumb in document_thumbs:
                thumbnail = get_image_from_bytes(doc_thumb.document.thumbnail_bytes)
                thumbnail.show()
        """
        project = Project.get(project_id=project_id)

        if project.stage in [PROJECT_STAGE.EDA2, PROJECT_STAGE.MODELING]:
            path = cls._list_project_sample_path.format(project_id=project_id)
        else:
            path = cls._list_eda_sample_path.format(project_id=project_id)

        list_params = dict(featureName=feature_name)
        if target_value:
            list_params["targetValue"] = target_value
        if offset:
            list_params["offset"] = str(offset)
        if limit:
            list_params["limit"] = str(limit)

        r_data = cls._client.get(path, params=list_params).json()
        documents = []

        # construct document objects for each document sample
        for doc_data in r_data["data"]:
            doc_data["project_id"] = project_id
            document: "DocumentThumbnail" = cls.from_server_data(doc_data)
            documents.append(document)
        return documents
