"""Test link prediction models based on combined text and layout embeddings."""

from __future__ import annotations
from typing import Optional
import pytest
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from link_prediction.models.classification.text_and_layout import (
    TextAndLayoutClassifier,
)
from link_prediction.datasets.rico import load_rico_links
from link_prediction.models.classification.text_and_layout.types import (
    TextAndLayoutEncoding,
)
from link_prediction.models.classification.text_and_layout.preprocessing import (
    DataPointTransformer,
)
from sklearn.base import clone
from .data import rico_data_point


class TestTextAndLayoutClassifier:
    """Contains tests for the TextAndLayoutClassifier model."""

    @pytest.mark.skip(reason="dependent on other input")
    def test_data_point_embedding_format(
        self, data_point_embedding: Optional[TextAndLayoutEncoding] = None
    ):
        if data_point_embedding is None:
            transformer = DataPointTransformer()
            data_point_embedding = transformer._encode_data_point(rico_data_point)
        layout_vector_length = 64
        text_vector_length = 384
        source_element_bounds_vector_length = 4
        data_point_embedding_vector_length = (
            text_vector_length * 2
            + layout_vector_length * 2
            + source_element_bounds_vector_length
        )
        assert len(data_point_embedding) == data_point_embedding_vector_length
        assert isinstance(data_point_embedding, list)

    def test_data_point_embedding(
        self,
        transformer: DataPointTransformer = DataPointTransformer(),
    ) -> None:
        """Test data point embedding methods of model."""
        data_point_embedding = transformer._encode_data_point(rico_data_point)
        self.test_data_point_embedding_format(data_point_embedding)

    def test_model_params(
        self,
        model: TextAndLayoutClassifier = TextAndLayoutClassifier(),
        transformer: DataPointTransformer = DataPointTransformer(),
    ) -> None:
        """Test parameter-related methods of model."""
        expected_params = {
            "datapointtransformer__number_of_neighbors": 6,
            "textandlayoutclassifier__complementnb__alpha": 1,
        }
        pipeline = make_pipeline(
            transformer,
            model,
        )
        pipeline_params = pipeline.get_params()
        for param, value in expected_params.items():
            assert param in pipeline_params
            assert pipeline_params[param] == value
        updated_params = {
            "datapointtransformer__number_of_neighbors": 1,
            "textandlayoutclassifier__complementnb__alpha": 0.1,
        }
        updated_pipeline = clone(pipeline).set_params(**updated_params)
        updated_pipeline_params = updated_pipeline.get_params()
        for param, value in updated_params.items():
            assert param in updated_pipeline_params
            assert updated_pipeline_params[param] == value
        X, y = load_rico_links(return_X_y=True)
        y_scores = []
        for current_pipeline in [pipeline, updated_pipeline]:
            X_train, X_test, y_train = train_test_split(
                X, y, test_size=0.33, random_state=42
            )[:3]
            current_pipeline.fit(X=X_train, y=y_train)
            try:
                y_score = current_pipeline.predict_proba(X_test)
            except AttributeError:
                y_score = current_pipeline.decision_function(X_test)
            y_scores.append(y_score)
        y_scores_different = [
            y_s != y_s_2 for y_s, y_s_2 in zip(y_scores[0], y_scores[1])
        ]
        assert any(y_scores_different)

    def test_rico_data_point_transformer(self):
        """Test the preprocessing transformer."""
        transformer = DataPointTransformer()
        data_point_embedding = transformer.transform([rico_data_point])[0]
        self.test_data_point_embedding_format(data_point_embedding)


def main() -> None:
    """Create model instance and test its methods."""
    model = TextAndLayoutClassifier()
    transformer = DataPointTransformer()
    test_model = TestTextAndLayoutClassifier()
    test_model.test_model_params(model, transformer)


if __name__ == "__main__":
    main()
