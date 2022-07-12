"""Heuristic link prediction models based on semantic similarity
between source element area's and target screen's text content."""

from link_prediction.models.heuristics.text_similarity import (
    TextSimilarityClassifier,
)


class TextSimilarityNeighborsClassifier(TextSimilarityClassifier):
    def __init__(
        self, similarity_threshold=0.292
    ):  # value from optimization similarity_threshold=0.2921234440977471
        """Link elements to pages if the element text content and the text content of its
        n closest neighbors and the text on the page meet a predefined similarity threshold"""
        super().__init__(similarity_threshold)


def main() -> None:
    """Create model instance and test its properties."""
    model = TextSimilarityNeighborsClassifier()


if __name__ == "__main__":
    main()
