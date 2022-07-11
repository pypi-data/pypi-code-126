"""Heuristic link prediction models based on source element's
label and target screen's largest text elements' content."""

from typing import Optional
from ..base import HeuristicClassifier
import numpy as np

SourceElementLabel = Optional[str]
TargetPageTexts = list[str]


class LargestTextElementsContainLabelClassifier(HeuristicClassifier):
    """Link elements to pages if the element label contains a token
    present among the words of the largest n text elements on the page"""

    def get_share_of_label_words_among_target_page_largest_texts(
        self,
        source_element_label: SourceElementLabel,
        target_page_largest_text_elements_texts: TargetPageTexts,
    ):
        """
        Returns the number of words in both the source element's label
        and on the target page divided by the number of all words on
        the target page.
        """
        if not source_element_label:
            return 0.0
        target_page_words = [
            word
            for text in target_page_largest_text_elements_texts
            for word in text.split(" ")
        ]
        if len(target_page_words) == 0:
            return 0.0
        label_words_among_target_page_largest_texts = [
            label_word
            for label_word in source_element_label.split(" ")
            if label_word in target_page_words
        ]
        return len(label_words_among_target_page_largest_texts) / len(target_page_words)

    def decision_function(self, X: list[tuple[SourceElementLabel, TargetPageTexts]]):
        y_score = np.array(
            [
                self.get_share_of_label_words_among_target_page_largest_texts(
                    source_element_label=source_element_label,
                    target_page_largest_text_elements_texts=target_page_largest_text_elements_texts,
                )
                for (source_element_label, target_page_largest_text_elements_texts) in X
            ]
        )
        return y_score


def main() -> None:
    """Create model instance and test its properties."""
    model = LargestTextElementsContainLabelClassifier()


if __name__ == "__main__":
    main()
