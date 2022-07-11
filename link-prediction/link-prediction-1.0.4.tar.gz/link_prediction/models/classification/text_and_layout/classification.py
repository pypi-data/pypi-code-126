"""Link prediction models based on combined text and layout embeddings."""

from sklearn.ensemble import RandomForestClassifier
from imblearn.under_sampling import RandomUnderSampler
from imblearn.pipeline import make_pipeline
from link_prediction.models.classification.base import (
    Classifier as BaseClassifier,
)


class TextAndLayoutClassifier(BaseClassifier):
    """Link prediction model based on a combined text
    and layout embedding."""

    def __init__(
        self,
        steps=[
            ("randomundersampler", RandomUnderSampler(random_state=42)),
            (
                "randomforestclassifier",
                RandomForestClassifier(
                    n_jobs=2, random_state=42, max_features=1.0, n_estimators=10
                ),
            ),
        ],
        *,
        memory=None,
        verbose=False
    ):
        super().__init__(steps=steps, memory=memory, verbose=verbose)


def main() -> None:
    """Create model instance and test its properties."""
    model = TextAndLayoutClassifier()


if __name__ == "__main__":
    main()
