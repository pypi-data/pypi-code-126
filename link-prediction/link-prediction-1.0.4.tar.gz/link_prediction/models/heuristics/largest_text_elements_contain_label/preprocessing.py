"""Transformers for link prediction models based
on the 'largest text elements contain label' heuristic."""

from link_prediction.datasets.rico import RicoDataPoint
from link_prediction.datasets.figma import FigmaDataPoint
from link_prediction.models.classification.base import (
    DataPointTransformer as BaseDataPointTransformer,
)


class DataPointTransformer(BaseDataPointTransformer):
    def __init__(self, large_text_elements_count=20):
        """Transformer to process RicoDataPoint into required format
        for LargestTextElementsContainLabelClassifier."""
        self.large_text_elements_count = large_text_elements_count
        super().__init__()

    def _encode_data_point(
        self, data_point: RicoDataPoint | FigmaDataPoint, *args, **kwargs
    ) -> tuple[str | None, list[str]]:
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
        ["Driver", ["Times", "Circuits", ...]]
        """
        elements_with_text = data_point.target_page.elements_with_text
        elements_with_text_sorted_by_size = sorted(
            elements_with_text,
            key=lambda element: element.bounds.width * element.bounds.height,
            reverse=True,
        )
        largest_elements_with_text = elements_with_text_sorted_by_size[
            : self.large_text_elements_count
        ]
        target_page_largest_text_elements_texts = [
            element.characters for element in largest_elements_with_text
        ]
        return (
            data_point.source_element.characters,
            target_page_largest_text_elements_texts,
        )
