"""Test link prediction models based on text embeddings."""

import pytest
from typing import Optional
from sklearn import clone
from sklearn.model_selection import train_test_split

from sklearn.pipeline import make_pipeline
from link_prediction.datasets.rico import load_rico_links
from link_prediction.models.classification.text import (
    TextClassifier,
    DataPointTransformer,
)
from link_prediction.models.classification.text.preprocessing import TextTransformer
from link_prediction.models.classification.text.types import TextEncoding
from .data import rico_data_point


class TestTextClassifier:
    """Contains tests for the TextClassifier model."""

    def test_text_embedding(
        self,
        transformer: TextTransformer = TextTransformer(),
    ) -> None:
        """Test text embedding methods of model."""
        text_embedding = transformer._encode_text("some text")
        text_embedding_vector_length = 384
        assert len(text_embedding) == text_embedding_vector_length
        assert isinstance(text_embedding, list)

    @pytest.mark.skip(reason="dependent on other input")
    def test_data_point_embedding_format(
        self, data_point_embedding: Optional[TextEncoding] = None
    ):
        """Test format of the text embedding for the source and target."""
        if data_point_embedding is None:
            transformer = DataPointTransformer()
            data_point_embedding = transformer._encode_data_point(rico_data_point)
        text_vector_length = 384
        data_point_embedding_vector_length = text_vector_length * 2
        assert len(data_point_embedding) == data_point_embedding_vector_length
        assert isinstance(data_point_embedding, list)
        assert isinstance(data_point_embedding[0], float)

    def test_data_point_embedding(
        self,
        transformer: DataPointTransformer = DataPointTransformer(),
    ) -> None:
        """Test data point embedding methods of model."""
        data_point_embedding = transformer._encode_data_point(rico_data_point)
        self.test_data_point_embedding_format(data_point_embedding)

    def test_rico_data_point_transformer(self):
        """Test the preprocessing transformer."""
        transformer = DataPointTransformer()
        data_point_embedding = transformer.transform([rico_data_point])[0]
        self.test_data_point_embedding_format(data_point_embedding)

    def test_model_params(
        self,
        model: TextClassifier = TextClassifier(),
        transformer: DataPointTransformer = DataPointTransformer(),
    ) -> None:
        """Test parameter-related methods of model."""
        expected_params = {
            "datapointtransformer__number_of_neighbors": 6,
            "textclassifier__complementnb__alpha": 1,
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
            "textclassifier__complementnb__alpha": 0.1,
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


def main() -> None:
    """Create model instance and test its methods."""
    model = TextClassifier()
    transformer = DataPointTransformer()
    test_model = TestTextClassifier()
    test_model.test_model_params(model, transformer)


if __name__ == "__main__":
    main()
