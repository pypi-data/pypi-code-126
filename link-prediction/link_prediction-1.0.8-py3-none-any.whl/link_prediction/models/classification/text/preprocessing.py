"""Transformers for link prediction models based on text."""

from typing import Optional
from sklearn.base import BaseEstimator, TransformerMixin
from sentence_transformers import SentenceTransformer
from link_prediction.datasets.rico import RicoDataPoint
from link_prediction.datasets.figma import FigmaDataPoint
from .types import TextEncoding
from link_prediction.models.classification.base import (
    DataPointTransformer as BaseDataPointTransformer,
)


class TextTransformer(BaseEstimator, TransformerMixin):
    def __init__(
        self,
        language_model=SentenceTransformer("all-MiniLM-L6-v2"),
    ):
        """Transformer to process text into required format
        for text classification."""
        self.language_model = language_model
        super().__init__()

    def _encode_text(self, text: str, *args, **kwargs) -> TextEncoding:
        """Returns a vector encoding of the given text
        using the language model.

        Examples
        --------
        Embedding a text.

        >>> transformer = TextTransformer()
        >>> transformer._encode_text("some text")
        [0.01, 0.1, 0.5, ...]
        """
        return self.language_model.encode(text, *args, **kwargs).tolist()

    def fit(self, X: Optional[list[str]] = None, y: Optional[list[int]] = None) -> None:
        """Fit to data (no-op)."""
        return self

    def transform(self, X: list[str]) -> list[TextEncoding]:
        """
        Returns the processed samples for use with text classification.

        Examples
        --------
        Transform a text.

        >>> transformer = TextTransformer()
        >>> transformer.transform(["some text"])
        [0.01, 0.1, 0.5, ...]
        """
        X_transformed = [self._encode_text(text) for text in X]
        return X_transformed


class DataPointTransformer(BaseDataPointTransformer):
    def __init__(
        self,
        language_model=SentenceTransformer("all-MiniLM-L6-v2"),
        number_of_neighbors=7,
    ):
        """Transformer to process RicoDataPoint into required format
        for TextClassifier."""
        self.text_transformer = TextTransformer(
            language_model=language_model,
        )
        self.language_model = language_model
        self.number_of_neighbors = number_of_neighbors
        super().__init__()

    def _encode_data_point(
        self, data_point: RicoDataPoint | FigmaDataPoint, *args, **kwargs
    ) -> TextEncoding:
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
        [0.01, 0.1, 0.5, ...]
        """
        (
            source_element_text_embedding,
            target_screen_text_embedding,
        ) = self._encode_data_point_text(data_point)
        return source_element_text_embedding + target_screen_text_embedding

    def _encode_data_point_text(
        self, data_point: RicoDataPoint | FigmaDataPoint, *args, **kwargs
    ) -> tuple[TextEncoding, TextEncoding]:
        """Returns a vector encoding of the given data point's
        source element and target screen text using the language model.

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
        ([0.01, 0.1, 0.5, ...], [0.01, 0.1, 0.5, ...])
        """
        closest_neighbors = data_point.source_page.get_closest_neighbors(
            element_id=data_point.source_element.id,
            number_of_neighbors=self.number_of_neighbors,
            include_non_text=False,
        )
        neighbor_texts = [
            neighbor.characters for neighbor in closest_neighbors if neighbor.characters
        ]
        source_element_texts = (
            data_point.source_element.texts if data_point.source_element.texts else []
        )
        source_element_text_embedding = self.text_transformer.transform(
            [" ".join(source_element_texts + neighbor_texts)]
        )[0]
        target_screen_text_embedding = self.text_transformer.transform(
            [" ".join(data_point.target_page.texts)]
        )[0]
        return source_element_text_embedding, target_screen_text_embedding
