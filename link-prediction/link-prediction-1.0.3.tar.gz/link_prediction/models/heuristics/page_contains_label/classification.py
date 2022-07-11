"""Heuristic link prediction models based on source element's
label and target screen text content."""

from typing import Optional
from ..base import HeuristicClassifier
import numpy as np

SourceElementLabel = Optional[str]
TargetPageTexts = list[str]


class PageContainsLabelClassifier(HeuristicClassifier):
    """Links elements to pages if the element label contains a token
    present on the page"""

    def get_share_of_label_words_on_target_page(
        self,
        source_element_label: SourceElementLabel,
        target_page_texts: TargetPageTexts,
    ):
        """
        Returns the number of label words also appearing on the target page
        divided by the total number of words on the target page
        """
        if not source_element_label:
            return 0.0
        if len(target_page_texts) == 0:
            return 0.0
        label_words_on_target_page = [
            label_word
            for label_word in source_element_label.split(" ")
            if label_word in target_page_texts
        ]
        return len(label_words_on_target_page) / len(target_page_texts)

    def decision_function(self, X: list[tuple[SourceElementLabel, TargetPageTexts]]):
        y_score = np.array(
            [
                self.get_share_of_label_words_on_target_page(
                    source_element_label=source_element_label,
                    target_page_texts=target_page_texts,
                )
                for (source_element_label, target_page_texts) in X
            ]
        )
        return y_score


def main() -> None:
    """Create model instance and test its properties."""
    model = PageContainsLabelClassifier()


if __name__ == "__main__":
    main()
