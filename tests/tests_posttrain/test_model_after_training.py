from src.pipeline.model_load_pipeline import model_loader_service
from src.pipeline.model_inference_pipeline import model_inference_service
from src.components.data_preprocessing import DataPreprocessing
from src.components.model_all import _evaluate_model, _get_x_y, _split_data
import pandas as pd
import pytest


pytestmark = [pytest.mark.posttrain]
test_introvert = {
    'Time_spent_Alone': [5],
    'Stage_fear': [0],
    'Social_event_attendance': [1],
    'Going_outside': [3],
    'Drained_after_socializing': [1],
    'Friends_circle_size': [2],
    'Post_frequency': [1]
}

test_extrovert = {
    'Time_spent_Alone': [2],
    'Stage_fear': [0],
    'Social_event_attendance': [8],
    'Going_outside': [7],
    'Drained_after_socializing': [0],
    'Friends_circle_size': [10],
    'Post_frequency': [3]
}


def test_loading_service():
    MS = model_loader_service()
    MS.load_model()
    assert MS.model is not None


def test_loading_highest_score():
    MS = model_loader_service()
    MS.load_highest_score()
    assert MS.highest_score > -1


def test_inference_service_introvert():
    MIS = model_inference_service()
    pred = MIS.predict(pd.DataFrame(test_introvert))
    assert MIS._classes[pred[0]] == 'Introvert'


def test_inference_service_extrovert():
    MIS = model_inference_service()
    pred = MIS.predict(pd.DataFrame(test_extrovert))
    assert MIS._classes[pred[0]] == 'Extrovert'


def test_inference_service_invariant_introvert():
    MIS = model_inference_service()
    test_introvert_v1 = test_introvert.copy()
    test_introvert_v1['Friends_circle_size'] = 1
    pred = MIS.predict(pd.DataFrame(test_introvert_v1))
    assert MIS._classes[pred[0]] == 'Introvert'


def test_inference_service_directional_introvert():
    MIS = model_inference_service()
    test_introvert_v2 = test_introvert.copy()
    test_introvert_v2['Drained_after_socializing'] = 0
    test_introvert_v2['Friends_circle_size'] = 7
    pred = MIS.predict(pd.DataFrame(test_introvert_v2))
    assert MIS._classes[pred[0]] == 'Extrovert'


def test_model_score_test_non_decreasing():
    db_preprocessor = DataPreprocessing()
    data = db_preprocessor.preprocess_data()
    x, y = _get_x_y(data)
    x_train, x_test, y_train, y_test = _split_data(x, y)
    MIS = model_inference_service()

    MS = model_loader_service()
    MS.load_highest_score()
    highest = MS.highest_score
    assert _evaluate_model(MIS.model, x_test, y_test) >= (highest - 0.05)
