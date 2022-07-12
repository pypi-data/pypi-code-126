"""Test the models' ability to predict Figma links."""

from dataclasses import asdict
from sklearn.pipeline import make_pipeline
from sklearn.metrics import precision_score, recall_score, f1_score
from link_prediction.datasets import load_rico_links
from link_prediction.datasets.figma import FigmaDataPoint, load_figma_links
from link_prediction.models import (
    PageContainsLabelClassifier,
    PageContainsLabelDataPointTransformer,
    LargestTextElementsContainLabelClassifier,
    LargestTextElementsContainLabelDataPointTransformer,
    LabelTextSimilarityClassifier,
    LabelTextSimilarityDataPointTransformer,
    TextSimilarityClassifier,
    TextSimilarityDataPointTransformer,
    TextSimilarityNeighborsClassifier,
    TextSimilarityNeighborsDataPointTransformer,
    TextClassifier,
    TextDataPointTransformer,
    LayoutClassifier,
    LayoutDataPointTransformer,
    TextAndLayoutClassifier,
    TextAndLayoutDataPointTransformer,
)
from sentence_transformers import SentenceTransformer
import json
from tqdm import tqdm


def prediction_to_dict(x: FigmaDataPoint, y_p: int, y_s: float):
    """Returns a dictionary representation of a prediction."""
    prediction_dict = x.to_dict()
    prediction_dict.update(is_predicted_link=bool(y_p), prediction_score=y_s)
    return prediction_dict


def test_predict_links(save_predictions_to_file=False):
    """Tests whether the link prediction models can be trained
    on RICO data and then create a file with link predictions
    for the Figma designs."""
    # Load data
    X_rico, y_rico = load_rico_links(return_X_y=True)
    X_figma, y_figma = load_figma_links(return_X_y=True, number_of_data_points=99999)

    # For each pipeline
    transformers_and_classifiers = [
        (
            PageContainsLabelDataPointTransformer(),
            PageContainsLabelClassifier(),
        ),
        (
            LargestTextElementsContainLabelDataPointTransformer(),
            LargestTextElementsContainLabelClassifier(),
        ),
        (
            LabelTextSimilarityDataPointTransformer(
                language_model=SentenceTransformer("../all-MiniLM-L6-v2")
            ),
            LabelTextSimilarityClassifier(),
        ),
        (
            TextSimilarityDataPointTransformer(
                language_model=SentenceTransformer("../all-MiniLM-L6-v2")
            ),
            TextSimilarityClassifier(),
        ),
        (
            TextSimilarityNeighborsDataPointTransformer(
                language_model=SentenceTransformer("../all-MiniLM-L6-v2")
            ),
            TextSimilarityNeighborsClassifier(),
        ),
        (
            LayoutDataPointTransformer(),
            LayoutClassifier(),
        ),
        (
            TextDataPointTransformer(
                language_model=SentenceTransformer("../all-MiniLM-L6-v2")
            ),
            TextClassifier(),
        ),
        (
            TextAndLayoutDataPointTransformer(
                language_model=SentenceTransformer("../all-MiniLM-L6-v2")
            ),
            TextAndLayoutClassifier(),
        ),
    ]
    for (transformer, classifier) in tqdm(transformers_and_classifiers):
        pipeline = make_pipeline(
            transformer,
            classifier,
        )

        # Fit to RICO data
        pipeline.fit(X_rico, y_rico)

        # Generate predictions (and scores) for Figma data
        y_pred_figma = pipeline.predict(X_figma)
        if hasattr(pipeline, "predict_proba"):
            y_score_figma = pipeline.predict_proba(X_figma)
        else:
            y_score_figma = pipeline.decision_function(X_figma)

        # Construct one data object holding all predicted links
        predictions = [
            prediction_to_dict(x, y_p, y_s)
            for x, y_p, y_s in zip(X_figma, y_pred_figma, y_score_figma)
        ]

        assert isinstance(predictions, list)
        assert isinstance(predictions[0], dict)
        for attribute in ["application_id", "target_id", "id", "is_link"]:
            assert attribute in predictions[0]
            assert predictions[0][attribute] == getattr(X_figma[0], attribute)
        assert "source" in predictions[0]
        assert predictions[0]["source"] == asdict(X_figma[0].source)
        assert "is_predicted_link" in predictions[0]
        assert isinstance(predictions[0]["is_predicted_link"], bool)
        assert "prediction_score" in predictions[0]
        assert isinstance(predictions[0]["prediction_score"], float)

        link_ids = [prediction["id"] for prediction in predictions]
        assert 1 in link_ids

        precision = precision_score(y_figma, y_pred_figma)
        recall = recall_score(y_figma, y_pred_figma)
        f1 = f1_score(y_figma, y_pred_figma)

        print(
            f"{classifier.__class__.__name__}: pre={round(precision, 3)}, rec={round(recall, 3)}, f1={round(f1, 3)},"
        )

        if save_predictions_to_file:
            # Save to file
            with open(
                f"data/links/models/{classifier.__class__.__name__}.json", "w"
            ) as f:
                json.dump({"predictions": predictions}, f, indent=4)
