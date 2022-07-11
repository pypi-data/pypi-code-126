"""Heuristic link prediction models based on semantic similarity
between source element's and target screen's text content."""

from ..base import HeuristicClassifier
import numpy as np
from sentence_transformers import util
from .types import SourceElementTextEncoding, TextEncoding


class TextSimilarityClassifier(HeuristicClassifier):
    """Link elements to pages if the element text content and the text on
    the page meet a predefined similarity threshold"""

    def __init__(
        self, similarity_threshold=0.263
    ):  # value from optimization similarity_threshold=0.26307284305776457
        self.similarity_threshold = similarity_threshold
        super().__init__()

    def get_difference_to_similarity_threshold(
        self,
        source_element_text_encoding: SourceElementTextEncoding,
        target_page_texts_encoding: TextEncoding,
    ):
        """
        Returns the difference between the text similarity of the source element
        and the target page (as measured by cosine similarity) to the predefined
        similarity threshold.
        """
        if source_element_text_encoding is None:
            return 0.0
        text_similarity = util.cos_sim(
            source_element_text_encoding, target_page_texts_encoding
        ).item()
        return text_similarity - self.similarity_threshold

    def decision_function(
        self, X: list[tuple[SourceElementTextEncoding, TextEncoding]]
    ):
        y_score = np.array(
            [
                self.get_difference_to_similarity_threshold(
                    source_element_text_encoding=source_element_text_encoding,
                    target_page_texts_encoding=target_page_texts_encoding,
                )
                for (source_element_text_encoding, target_page_texts_encoding) in X
            ]
        )
        return y_score


def main() -> None:
    """Create model instance and test its properties."""
    model = TextSimilarityClassifier()


if __name__ == "__main__":
    main()
