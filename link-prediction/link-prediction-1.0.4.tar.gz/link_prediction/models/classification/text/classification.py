"""Link prediction models based on text embeddings."""

from sklearn.ensemble import RandomForestClassifier
from imblearn.under_sampling import RandomUnderSampler
from link_prediction.models.classification.base import Classifier as BaseClassifier


class TextClassifier(BaseClassifier):
    """Link prediction model based on text embeddings."""

    def __init__(
        self,
        steps=[
            ("randomundersampler", RandomUnderSampler(random_state=42)),
            (
                "randomforestclassifier",
                RandomForestClassifier(
                    n_jobs=2,
                    random_state=42,
                    max_features=0.11115488482277079,
                    n_estimators=10,
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
    model = TextClassifier()


if __name__ == "__main__":
    main()
