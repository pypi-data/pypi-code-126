"""Transformers for link prediction models based
on the 'page contains label' heuristic."""

from link_prediction.datasets.rico import RicoDataPoint
from link_prediction.datasets.figma import FigmaDataPoint
from link_prediction.models.classification.base import (
    DataPointTransformer as BaseDataPointTransformer,
)


class DataPointTransformer(BaseDataPointTransformer):
    def __init__(
        self,
    ):
        """Transformer to process RicoDataPoint into required format
        for PageContainsLabelClassifier."""
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
        return (data_point.source_element.characters, data_point.target_page.texts)
