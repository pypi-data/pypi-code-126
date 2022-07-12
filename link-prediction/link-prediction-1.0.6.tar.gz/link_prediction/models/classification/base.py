"""Base classes for use across models."""

import abc
from typing import Optional
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.naive_bayes import ComplementNB
from sklearn.preprocessing import MinMaxScaler
from link_prediction.datasets.rico import RicoDataPoint
from link_prediction.datasets.figma import FigmaDataPoint
from imblearn.pipeline import Pipeline


class DataPointTransformer(BaseEstimator, TransformerMixin):
    """Base classes for all data point (i.e., RICO or Figma-based)
    transformers."""

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def _encode_data_point(
        self, data_point: RicoDataPoint | FigmaDataPoint, *args, **kwargs
    ) -> list[float | int]:
        """Returns a vector encoding of the given data point.

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
        return data_point

    def fit(
        self,
        X: Optional[list[RicoDataPoint | FigmaDataPoint]] = None,
        y: Optional[list[int]] = None,
    ) -> None:
        """Fit to data (no-op)."""
        return self

    def transform(self, X: list[RicoDataPoint | FigmaDataPoint]) -> list:
        """
        Returns the processed samples for use with the TextAndLayoutClassifier.

        Examples
        --------
        Transform a data point.

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
        >>> transformer.transform([rico_data_point])[0]
        [0.01, 0.1, 0.5, ...]
        """
        X_transformed = [self._encode_data_point(x) for x in X]
        return X_transformed


def get_linkability_score(y_score: np.ndarray):
    """Return positive linkability score from an array of scores."""
    return y_score[:, 1:2].flatten() if isinstance(y_score[0], np.ndarray) else y_score


class Classifier(Pipeline):
    """Represents a link prediction model pipeline."""

    def __init__(
        self,
        steps=[("scaler", MinMaxScaler()), ("complementnb", ComplementNB())],
        *,
        memory=None,
        verbose=False
    ):
        super().__init__(steps=steps, memory=memory, verbose=verbose)

    def predict_proba(self, X, **predict_proba_params):
        y_probs = super().predict_proba(X, **predict_proba_params)
        link_probabilities = get_linkability_score(y_probs)
        return link_probabilities

    def decision_function(self, X):
        y_score = super().decision_function(X)
        linkability_scores = get_linkability_score(y_score)
        return linkability_scores
