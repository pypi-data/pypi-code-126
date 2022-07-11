"""Transformers for link prediction models based on layout."""

from typing import Optional
from sklearn.base import BaseEstimator, TransformerMixin
import torch
from link_prediction.datasets.rico import RicoDataPoint
from link_prediction.datasets.figma import FigmaDataPoint
from link_prediction.models.classification.layout.layout_encoder import LayoutEncoder
from link_prediction.models.classification.layout.screen_layout import ScreenLayout
from link_prediction.utils.classes import Bounds
from .types import LayoutEncoding, ElementBoundsEncoding
from link_prediction.models.classification.base import (
    DataPointTransformer as BaseDataPointTransformer,
)


class ElementBoundsTransformer(BaseEstimator, TransformerMixin):
    def __init__(self):
        """Transformer to process an element's bounds into required format
        for LayoutClassifier."""
        super().__init__()

    def _encode_element_bounds(
        self, layout: ScreenLayout, element_bounds: Bounds, *args, **kwargs
    ) -> ElementBoundsEncoding:
        """Returns the scaled bounds (i.e., position, height and width)
        of the source element on the source screen.

        Examples
        --------
        Embedding a data point's source element position.

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
        >>> transformer._encode_element_bounds(rico_data_point)
        [0.3, 0.5, 0.2, 0.25]
        """
        x_top_scaled = element_bounds.x * layout.horiz_scale
        y_top_scaled = element_bounds.y * layout.vert_scale
        width_scaled = element_bounds.width * layout.horiz_scale
        height_scaled = element_bounds.height * layout.vert_scale
        return [x_top_scaled, y_top_scaled, width_scaled, height_scaled]

    def fit(
        self,
        X: Optional[list[tuple[ScreenLayout, Bounds]]] = None,
        y: Optional[list[int]] = None,
    ) -> None:
        """Fit to data (no-op)."""
        return self

    def transform(
        self, X: list[tuple[ScreenLayout, Bounds]]
    ) -> list[ElementBoundsEncoding]:
        """
        Returns the processed samples for use with the LayoutClassifier.

        Examples
        --------
        Transform an element's position.

        >>> ui_element: UIElement = UIElement(
        ...    id="1",
        ...    name="TextElement",
        ...    type="Text",
        ...    bounds=Bounds(x=0, y=0, width=256, height=256),
        ...    characters="some text",
        ... )
        >>> page_content: list[UIElement] = [ui_element]
        >>> page: Page = Page(
        ...     id="123", name="Test Page", height=2560, width=1440, children=page_content
        ... )
        >>> screen_layout: ScreenLayout = ScreenLayout(page)
        >>> transformer = LayoutTransformer()
        >>> transformer.transform([(screen_layout, ui_element)])[0]
        [0.01, 0.1, 0.5, ...]
        """
        X_transformed = [
            self._encode_element_bounds(layout, element_bounds)
            for (layout, element_bounds) in X
        ]
        return X_transformed


class LayoutTransformer(BaseEstimator, TransformerMixin):
    def __init__(
        self,
        layout_model=LayoutEncoder(),
    ):
        """Transformer to process screen layouts into required format
        for LayoutClassifier."""
        self.layout_model = layout_model
        super().__init__()

    def _encode_layout(self, layout: ScreenLayout, *args, **kwargs) -> LayoutEncoding:
        """Returns a vector encoding of the given layout
        using the layout embedding model.

        Examples
        --------
        Embedding a layout.

        >>> page_content: list[UIElement] = [
        ...     UIElement(
        ...         id="1",
        ...         name="TextElement",
        ...         type="Text",
        ...         bounds=Bounds(x=0, y=0, width=256, height=256),
        ...         characters="some text",
        ...     )
        ... ]
        >>> page: Page = Page(
        ...     id="123", name="Test Page", height=2560, width=1440, children=page_content
        ... )
        >>> screen_layout: ScreenLayout = ScreenLayout(page)
        >>> transformer = LayoutTransformer()
        >>> transformer._encode_layout(screen_layout)
        [0.01, 0.1, 0.5, ...]
        """
        pixels = layout.pixels.flatten()
        layout_embedding: list[float] = self.layout_model(
            torch.FloatTensor(pixels)
        ).tolist()
        return layout_embedding

    def fit(
        self, X: Optional[list[ScreenLayout]] = None, y: Optional[list[int]] = None
    ) -> None:
        """Fit to data (no-op)."""
        return self

    def transform(self, X: list[ScreenLayout]) -> list[LayoutEncoding]:
        """
        Returns the processed samples for use with the TextAndLayoutClassifier.

        Examples
        --------
        Transform a layout.

        >>> page_content: list[UIElement] = [
        ...     UIElement(
        ...         id="1",
        ...         name="TextElement",
        ...         type="Text",
        ...         bounds=Bounds(x=0, y=0, width=256, height=256),
        ...         characters="some text",
        ...     )
        ... ]
        >>> page: Page = Page(
        ...     id="123", name="Test Page", height=2560, width=1440, children=page_content
        ... )
        >>> screen_layout: ScreenLayout = ScreenLayout(page)
        >>> transformer = LayoutTransformer()
        >>> transformer.transform([screen_layout])[0]
        [0.01, 0.1, 0.5, ...]
        """
        X_transformed = [self._encode_layout(layout) for layout in X]
        return X_transformed


class DataPointTransformer(BaseDataPointTransformer):
    def __init__(
        self,
        layout_model=LayoutEncoder(),
    ):
        """Transformer to process RicoDataPoint into required format
        for LayoutClassifier."""
        self.layout_transformer = LayoutTransformer(
            layout_model=layout_model,
        )
        self.element_bounds_transformer = ElementBoundsTransformer()
        self.layout_model = layout_model
        super().__init__()

    def _encode_data_point_layout(
        self, data_point: RicoDataPoint | FigmaDataPoint, *args, **kwargs
    ) -> tuple[LayoutEncoding, LayoutEncoding, ElementBoundsEncoding]:
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
        ([0.01, 0.1, 0.5, ...], [0.01, 0.1, 0.5, ...], [0.1, 0.2, 0.35, 0.4])
        """
        source_screen_layout = ScreenLayout(data_point.source_page)
        source_screen_layout_embedding = self.layout_transformer.transform(
            [source_screen_layout]
        )[0]
        target_screen_layout = ScreenLayout(data_point.target_page)
        target_screen_layout_embedding = self.layout_transformer.transform(
            [target_screen_layout]
        )[0]
        source_element_bounds = self.element_bounds_transformer.transform(
            [(source_screen_layout, data_point.source_element.bounds)]
        )[0]
        return (
            source_screen_layout_embedding,
            target_screen_layout_embedding,
            source_element_bounds,
        )

    def _encode_data_point(
        self, data_point: RicoDataPoint | FigmaDataPoint, *args, **kwargs
    ) -> tuple[LayoutEncoding, LayoutEncoding, ElementBoundsEncoding]:
        """Returns a vector encoding of the given data point
        using the layout embedding model.

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
            source_screen_layout_embedding,
            target_screen_layout_embedding,
            source_element_mask,
        ) = self._encode_data_point_layout(data_point)
        return (
            source_screen_layout_embedding
            + target_screen_layout_embedding
            + source_element_mask
        )
