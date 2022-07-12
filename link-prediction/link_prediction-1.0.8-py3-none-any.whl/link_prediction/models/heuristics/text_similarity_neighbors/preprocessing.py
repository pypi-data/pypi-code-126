"""Transformers for link prediction models based
on the 'text similarity neighbors' heuristic."""

from link_prediction.datasets.rico import RicoDataPoint
from link_prediction.datasets.figma import FigmaDataPoint
from link_prediction.models.classification.base import (
    DataPointTransformer as BaseDataPointTransformer,
)
from sentence_transformers import SentenceTransformer
from .types import TextEncoding, SourceElementAreaTextEncoding


class DataPointTransformer(BaseDataPointTransformer):
    def __init__(
        self,
        number_of_neighbors=2,
        language_model=SentenceTransformer("all-MiniLM-L6-v2"),
    ):
        """Transformer to process RicoDataPoint into required format
        for TextSimilarityNeighborsClassifier."""
        self.language_model = language_model
        self.number_of_neighbors = number_of_neighbors
        super().__init__()

    def _encode_data_point(
        self, data_point: RicoDataPoint | FigmaDataPoint, *args, **kwargs
    ) -> tuple[SourceElementAreaTextEncoding, TextEncoding]:
        """Returns a vector encoding of the given data point
        using the text embedding model.

        Examples
        --------
        Embedding a data point.

        >>> rico_data_point: RicoDataPoint = RicoDataPoint(
        ...      source=RicoDataPoint.RawSourceData(
        ...          id=795, element_id="2e18ce7"
        ...      ),
        ...      target=RicoDataPoint.RicoScreen(
        ...         id=887,
        ...      ),
        ...      application_name="com.vzw.indycar",
        ...      trace_id=0,
        ...      data_type="link",
        ... )
        >>> transformer = DataPointTransformer()
        >>> transformer._encode_data_point(rico_data_point)
        [[0.01, 0.1, 0.23, ...], [0.01, 0.1, 0.23, ...]]
        """
        target_page_embedding = self.language_model.encode(
            " ".join(data_point.target_page.texts)
        )
        if data_point.source_element.texts is None:
            return (None, target_page_embedding)
        closest_neighbors = data_point.source_page.get_closest_neighbors(
            element_id=data_point.source_element.id,
            number_of_neighbors=self.number_of_neighbors,
            include_non_text=False,
        )
        neighbor_texts = [
            neighbor.characters for neighbor in closest_neighbors if neighbor.characters
        ]
        source_element_text_embedding = self.language_model.encode(
            " ".join(data_point.source_element.texts + neighbor_texts)
        )
        source_element_text_embedding = (
            self.language_model.encode(" ".join(data_point.source_element.texts))
            if data_point.source_element.texts is not None
            else None
        )
        return (
            source_element_text_embedding,
            target_page_embedding,
        )
