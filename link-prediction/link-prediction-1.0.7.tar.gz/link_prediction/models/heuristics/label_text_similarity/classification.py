"""Heuristic link prediction models based on semantic similarity
between source element's label and target screen's text content."""

from link_prediction.models.heuristics.text_similarity.classification import (
    TextSimilarityClassifier,
)


class LabelTextSimilarityClassifier(TextSimilarityClassifier):
    def __init__(
        self, similarity_threshold=0.122
    ):  # value from optimization: similarity_threshold=0.12176566857218385
        """Link elements to pages if the element label and the text on
        the page meet a predefined similarity threshold."""
        super().__init__(similarity_threshold)


def main() -> None:
    """Create model instance and test its properties."""
    model = LabelTextSimilarityClassifier()


if __name__ == "__main__":
    main()
