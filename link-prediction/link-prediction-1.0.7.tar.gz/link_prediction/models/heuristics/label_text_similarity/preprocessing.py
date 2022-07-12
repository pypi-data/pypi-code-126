"""Transformers for link prediction models based
on the 'label text similarity' heuristic."""

from link_prediction.datasets.rico import RicoDataPoint
from link_prediction.datasets.figma import FigmaDataPoint
from link_prediction.models.classification.base import (
    DataPointTransformer as BaseDataPointTransformer,
)
from sentence_transformers import SentenceTransformer
from .types import SourceElementLabelEncoding, TargetPageTextsEncoding


class DataPointTransformer(BaseDataPointTransformer):
    def __init__(
        self,
        language_model=SentenceTransformer("all-MiniLM-L6-v2"),
    ):
        """Transformer to process RicoDataPoint into required format
        for LabelTextSimilarityClassifier."""
        self.language_model = language_model
        super().__init__()

    def _encode_data_point(
        self, data_point: RicoDataPoint | FigmaDataPoint, *args, **kwargs
    ) -> tuple[SourceElementLabelEncoding, TargetPageTextsEncoding]:
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
        label_embedding = (
            self.language_model.encode(data_point.source_element.characters)
            if data_point.source_element.characters is not None
            else None
        )
        target_page_embedding = self.language_model.encode(
            " ".join(data_point.target_page.texts)
        )
        return (
            label_embedding,
            target_page_embedding,
        )
