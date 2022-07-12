"""Transformers for link prediction models based on combined text and layout embeddings."""

from __future__ import annotations
from sentence_transformers import SentenceTransformer
from link_prediction.models.classification.layout.layout_encoder import LayoutEncoder
from .types import (
    TextAndLayoutEncoding,
)
from link_prediction.datasets.figma import FigmaDataPoint
from link_prediction.datasets.rico import RicoDataPoint
from link_prediction.models.classification.text.preprocessing import (
    DataPointTransformer as TextDataPointTransformer,
)
from link_prediction.models.classification.layout.preprocessing import (
    DataPointTransformer as LayoutDataPointTransformer,
)
from link_prediction.models.classification.base import (
    DataPointTransformer as BaseDataPointTransformer,
)


class DataPointTransformer(BaseDataPointTransformer):
    def __init__(
        self,
        language_model=SentenceTransformer("models/all-MiniLM-L6-v2"),
        layout_model=LayoutEncoder(),
        number_of_neighbors=1,
    ):
        """Transformer to process RicoDataPoint into required format
        for TextAndLayoutClassifier."""
        self.text_transformer = TextDataPointTransformer(
            language_model=language_model,
            number_of_neighbors=number_of_neighbors,
        )
        self.layout_transformer = LayoutDataPointTransformer(
            layout_model=layout_model,
        )
        self.language_model = language_model
        self.layout_model = layout_model
        self.number_of_neighbors = number_of_neighbors
        super().__init__()

    def _encode_data_point(
        self, data_point: RicoDataPoint | FigmaDataPoint, *args, **kwargs
    ) -> TextAndLayoutEncoding:
        """Returns a vector encoding of the given data point
        using the text and layout embedding model.

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
        [0.01, 0.1, 0.5, ...]
        """
        text_encoding = self._encode_data_point_text(data_point)
        layout_encoding = self._encode_data_point_layout(data_point)
        return text_encoding + layout_encoding

    def _encode_data_point_text(
        self, data_point: RicoDataPoint | FigmaDataPoint, *args, **kwargs
    ) -> list:
        """Returns a vector encoding of the given data point's
        source element and target screen text using the language model

        Examples
        --------
        Embedding a data point's text.

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
        >>> transformer._encode_data_point_text(rico_data_point)
        [0.01, 0.1, 0.5, ...]
        """
        text_encoding = self.text_transformer.transform([data_point])[0]
        return text_encoding

    def _encode_data_point_layout(
        self, data_point: RicoDataPoint | FigmaDataPoint, *args, **kwargs
    ) -> list:
        """Returns a vector encoding of the given data point's
        source screen and target screen layout using the layout model

        Examples
        --------
        Embedding a data point's layout.

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
        >>> transformer._encode_data_point_layout(rico_data_point)
        [0.01, 0.1, 0.5, ...]
        """
        layout_encoding = self.layout_transformer.transform([data_point])[0]
        return layout_encoding


def main() -> None:
    """Test transformers."""
    transformer = DataPointTransformer()
    rico_data_point: RicoDataPoint = RicoDataPoint(
        source=RicoDataPoint.RawSourceData(id=795, element_id="2e18ce7"),
        target=RicoDataPoint.RicoScreen(
            id=887,
        ),
        application_name="com.vzw.indycar",
        trace_id=0,
        data_type="link",
    )
    embedding = transformer.transform([rico_data_point])[0]
    assert isinstance(embedding, list)
    assert isinstance(embedding[0], float)


if __name__ == "__main__":
    main()
