"""Link prediction models based on layout embeddings."""

from imblearn.ensemble import BalancedRandomForestClassifier
from link_prediction.models.classification.base import Classifier as BaseClassifier


class LayoutClassifier(BaseClassifier):
    """Link prediction model based on layout embeddings."""

    def __init__(
        self,
        steps=[
            (
                "balancedrandomforestclassifier",
                BalancedRandomForestClassifier(
                    n_jobs=2,
                    random_state=42,
                    max_features=0.39235390082196925,
                    n_estimators=24,
                ),
            )
        ],
        *,
        memory=None,
        verbose=False
    ):
        super().__init__(steps=steps, memory=memory, verbose=verbose)


def main() -> None:
    """Create model instance and test its properties."""
    model = LayoutClassifier()


if __name__ == "__main__":
    main()
