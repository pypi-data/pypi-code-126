"""Test link prediction models based on supervised classification."""

from typing import Optional
import pytest
import numpy as np
from sklearn.base import BaseEstimator
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from skopt import BayesSearchCV
from skopt.space import Integer, Real, Dimension
from link_prediction.datasets.figma import FigmaDataPoint, load_figma_links
from link_prediction.models.classification.base import (
    DataPointTransformer as BaseDataPointTransformer,
)
from link_prediction.datasets import load_rico_links
from link_prediction.models.classification.text_and_layout import (
    TextAndLayoutClassifier,
    DataPointTransformer as TextAndLayoutDataPointTransformer,
)
from link_prediction.models.classification.text import (
    TextClassifier,
    DataPointTransformer as TextDataPointTransformer,
)
from link_prediction.models.classification.layout import (
    LayoutClassifier,
    DataPointTransformer as LayoutDataPointTransformer,
)
from link_prediction.models.heuristics.largest_text_elements_contain_label import (
    LargestTextElementsContainLabelClassifier,
    DataPointTransformer as LargestTextElementsContainLabelDataPointTransformer,
)
from link_prediction.models.heuristics.page_contains_label import (
    PageContainsLabelClassifier,
    DataPointTransformer as PageContainsLabelDataPointTransformer,
)
from link_prediction.models.heuristics.label_text_similarity import (
    LabelTextSimilarityClassifier,
    DataPointTransformer as LabelTextSimilarityDataPointTransformer,
)
from link_prediction.models.heuristics.text_similarity import (
    TextSimilarityClassifier,
    DataPointTransformer as TextSimilarityDataPointTransformer,
)
from link_prediction.models.heuristics.text_similarity_neighbors import (
    TextSimilarityNeighborsClassifier,
    DataPointTransformer as TextSimilarityNeighborsDataPointTransformer,
)


SearchSpaces = dict[str, Dimension]

CLASSIFIERS_AND_TRANSFORMERS: list[
    tuple[BaseEstimator, BaseDataPointTransformer, Optional[SearchSpaces]]
] = [
    (
        TextSimilarityNeighborsClassifier,
        TextSimilarityNeighborsDataPointTransformer,
        {
            "datapointtransformer__number_of_neighbors": Integer(1, 20),
            "textsimilarityneighborsclassifier__similarity_threshold": Real(
                0.001, 10, prior="log-uniform"
            ),
        },
    ),
    (
        TextSimilarityClassifier,
        TextSimilarityDataPointTransformer,
        {
            "textsimilarityclassifier__similarity_threshold": Real(
                0.001, 10, prior="log-uniform"
            ),
        },
    ),
    (
        LabelTextSimilarityClassifier,
        LabelTextSimilarityDataPointTransformer,
        {
            "labeltextsimilarityclassifier__similarity_threshold": Real(
                0.001, 10, prior="log-uniform"
            ),
        },
    ),
    (
        LargestTextElementsContainLabelClassifier,
        LargestTextElementsContainLabelDataPointTransformer,
        {
            "datapointtransformer__large_text_elements_count": Integer(1, 20),
        },
    ),
    (PageContainsLabelClassifier, PageContainsLabelDataPointTransformer, None),
    (
        TextAndLayoutClassifier,
        TextAndLayoutDataPointTransformer,
        {
            "datapointtransformer__number_of_neighbors": Integer(1, 20),
            "textandlayoutclassifier__randomforestclassifier__n_estimators": Integer(
                10, 200
            ),
            "textandlayoutclassifier__randomforestclassifier__max_features": Real(
                0.001, 1.0, prior="log-uniform"
            ),
        },
    ),
    (
        TextClassifier,
        TextDataPointTransformer,
        {
            "datapointtransformer__number_of_neighbors": Integer(1, 20),
            "textclassifier__randomforestclassifier__n_estimators": Integer(10, 200),
            "textclassifier__randomforestclassifier__max_features": Real(
                0.001, 1.0, prior="log-uniform"
            ),
        },
    ),
    (
        LayoutClassifier,
        LayoutDataPointTransformer,
        {
            "layoutclassifier__balancedrandomforestclassifier__n_estimators": Integer(
                10, 200
            ),
            "layoutclassifier__balancedrandomforestclassifier__max_features": Real(
                0.001, 1.0, prior="log-uniform"
            ),
        },
    ),
]
PARAMETRIC_MODELS_AND_TRANSFORMERS = [
    (classifier, transformer, search_spaces)
    for (classifier, transformer, search_spaces) in CLASSIFIERS_AND_TRANSFORMERS
    if search_spaces is not None
]


@pytest.mark.parametrize(
    "model_class,transformer_class",
    [
        (model_class, transformer)
        for model_class, transformer, _ in CLASSIFIERS_AND_TRANSFORMERS
    ],
)
def test_classifier(
    model_class: BaseEstimator,
    transformer_class: BaseDataPointTransformer,
) -> None:
    """Test classification methods of model."""
    X, y = load_rico_links(return_X_y=True)
    X_train, X_test, y_train = train_test_split(X, y, test_size=0.33, random_state=42)[
        :3
    ]
    pipeline = make_pipeline(
        transformer_class(),
        model_class(),
    )
    pipeline.fit(X=X_train, y=y_train)
    y_pred = pipeline.predict(X_test)
    assert isinstance(y_pred, np.ndarray)
    assert isinstance(y_pred[0].item(), int)
    try:
        y_score = pipeline.predict_proba(X_test)
    except AttributeError:
        y_score = pipeline.decision_function(X_test)
    assert isinstance(y_score, np.ndarray)
    if y_score.ndim == 1:
        assert isinstance(y_score[0].item(), float)
    elif y_score.ndim == 1:  # May also be np.ndarray with both probabilities
        assert isinstance(y_score[0], np.ndarray) and isinstance(
            y_score[0][1].flatten().item(), float
        )


@pytest.mark.parametrize(
    "model_class,transformer_class,search_spaces",
    [
        (model_class, transformer, search_spaces)
        for model_class, transformer, search_spaces in PARAMETRIC_MODELS_AND_TRANSFORMERS
    ],
)
@pytest.mark.slow
@pytest.mark.filterwarnings("ignore:::.*skopt*")  # Raised by skopt
def test_tuning_hyperparameters(
    model_class: BaseEstimator,
    transformer_class: BaseDataPointTransformer,
    search_spaces: SearchSpaces,
    number_of_data_points=1000,
    n_iter=2,
    cv=2,
) -> None:
    """Test tuning the model's hyperparameters."""
    X, y = load_rico_links(return_X_y=True, number_of_data_points=number_of_data_points)
    pipeline = make_pipeline(
        transformer_class(),
        model_class(),
    )
    score = "f1"
    opt = BayesSearchCV(
        pipeline,
        search_spaces,
        scoring="%s_macro" % score,
        n_jobs=1,
        cv=cv,
        n_iter=n_iter,
        verbose=4,
        random_state=42,
    )
    opt.fit(X, y)
    assert hasattr(opt, "best_params_")
    assert hasattr(opt, "cv_results_")
    for key in search_spaces:
        assert key in opt.best_params_
    assert "mean_test_score" in opt.cv_results_
    assert "std_test_score" in opt.cv_results_
    assert "params" in opt.cv_results_


@pytest.mark.parametrize(
    "model_class,transformer_class",
    [
        (model_class, transformer)
        for model_class, transformer, _ in CLASSIFIERS_AND_TRANSFORMERS
    ],
)
def test_design_predictions(
    model_class: BaseEstimator,
    transformer_class: BaseDataPointTransformer,
):
    """Test link prediction using design structures as data."""
    model = model_class()
    transformer = transformer_class()
    X, y = load_figma_links(return_X_y=True)
    assert isinstance(X, list)
    assert isinstance(X[0], FigmaDataPoint)
    assert isinstance(y, list)
    assert isinstance(y[0], int)
    X_transformed = transformer.transform(X)
    assert isinstance(X_transformed, list)
    if model_class in [
        PageContainsLabelClassifier,
        LargestTextElementsContainLabelClassifier,
        LabelTextSimilarityClassifier,
        TextSimilarityClassifier,
        TextSimilarityNeighborsClassifier,
    ]:
        assert isinstance(X_transformed[0], tuple)
        if model_class in [
            LabelTextSimilarityClassifier,
            TextSimilarityClassifier,
            TextSimilarityNeighborsClassifier,
        ]:
            assert (
                isinstance(X_transformed[0][0], np.ndarray)
                or X_transformed[0][0] is None
            )
            assert isinstance(X_transformed[0][1], np.ndarray)
        else:
            assert isinstance(X_transformed[0][0], str) or X_transformed[0][0] is None
            assert isinstance(X_transformed[0][1], list)
            assert isinstance(X_transformed[0][1][0], str)
    else:
        assert isinstance(X_transformed[0], list)
        assert isinstance(X_transformed[0][0], float)
    pipeline = make_pipeline(
        transformer,
        model,
    )
    X_train, X_test, y_train = train_test_split(X, y, test_size=0.33, random_state=42)[
        :3
    ]
    pipeline.fit(X=X_train, y=y_train)
    y_pred = pipeline.predict(X)
    assert isinstance(y_pred, np.ndarray)
    assert isinstance(y_pred[0].item(), int)
    try:
        y_score = pipeline.predict_proba(X_test)
    except AttributeError:
        y_score = pipeline.decision_function(X_test)
    assert isinstance(y_score, np.ndarray)
    assert isinstance(y_score[0].item(), float)
