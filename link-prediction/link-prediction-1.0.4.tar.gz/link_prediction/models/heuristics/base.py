"""Base classes for use across heuristic models."""

import abc
from typing import Optional
from sklearn.base import BaseEstimator
import numpy as np


class HeuristicClassifier(BaseEstimator):
    """Base class for heuristic classification models."""

    def __init__(
        self,
    ):
        super().__init__()

    def fit(self, X: Optional[list] = None, y: Optional[list] = None):
        """Fit to data (no-op)."""
        pass

    @abc.abstractmethod
    def decision_function(self, X: list):
        """Returns a 'linkability' score for each given sample"""
        raise NotImplementedError()

    @abc.abstractmethod
    def predict(self, X: list):
        """Returns a label of link (1) or non-link (0)for each given sample"""
        y_score = self.decision_function(X)
        y_pred = np.array([int(y_s > 0) for y_s in y_score])
        return y_pred


def main() -> None:
    """Create model instance and test its properties."""
    model = HeuristicClassifier()


if __name__ == "__main__":
    main()
