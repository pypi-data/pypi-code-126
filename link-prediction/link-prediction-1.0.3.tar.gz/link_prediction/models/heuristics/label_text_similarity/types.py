"""Type definitions for LabelTextSimilarityClassifier."""

from typing import Optional


TextEncoding = list[float]
SourceElementLabelEncoding = Optional[TextEncoding]
TargetPageTextsEncoding = TextEncoding
