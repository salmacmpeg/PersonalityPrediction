from pathlib import Path
from src.components.data_preprocessing import DataPreprocessing
from src.components.model_all import (
    build_model, _get_x_y, _split_data, _train_model, _evaluate_model)
from src.configs import model_settings_obj
import pandas as pd
import pytest

pytestmark = pytest.mark.training


@pytest.fixture(scope="module")
def loaded_data():
    db_preprocessor = DataPreprocessing()
    data = db_preprocessor.preprocess_data()
    return data


@pytest.fixture(scope="function")
def splitted_data():
    db_preprocessor = DataPreprocessing()
    data = db_preprocessor.preprocess_data()
    x, y = _get_x_y(data)
    x_train, x_test, y_train, y_test = _split_data(x, y)
    return x_train, x_test, y_train, y_test


def test_model_get_x_y_0(loaded_data: pd.DataFrame):
    x, y = _get_x_y(loaded_data)
    assert isinstance(x, pd.DataFrame) and isinstance(y, pd.Series)
    assert True


def test_model_get_x_y_1(loaded_data: pd.DataFrame):
    x, y = _get_x_y(loaded_data)
    assert x.shape[0] == y.shape[0]
    assert True


def test_model_split_data_0(splitted_data):
    x_train, x_test, y_train, y_test = splitted_data
    assert [isinstance(obj, pd.DataFrame)
            for obj in [x_train, x_test]].count(True) == 2


def test_model_split_data_1(splitted_data):
    x_train, x_test, y_train, y_test = splitted_data
    assert [isinstance(obj, pd.Series)
            for obj in [y_train, y_test]].count(True) == 2


def test_model_split_data_2(splitted_data):
    x_train, x_test, y_train, y_test = splitted_data
    assert (x_train.shape[0] == y_train.shape[0] and
            x_test.shape[0] == y_test.shape[0])


def test_model_split_data_3(splitted_data):
    x_train, x_test, y_train, y_test = splitted_data
    assert list(x_train.columns) == list(x_test.columns)


def test_model_split_data_leakage(splitted_data):
    x_train, x_test, y_train, y_test = splitted_data
    x_train['Personality'] = y_train
    x_test['Personality'] = y_test
    concat_df = pd.concat([x_train, x_test], axis=0)
    concat_df.drop_duplicates(inplace=True)
    assert concat_df.shape[0] == x_train.shape[0] + x_test.shape[0]


def test_model_training(splitted_data):
    x_train, x_test, y_train, y_test = splitted_data
    model = _train_model(x_train, y_train)
    assert model.score(x_train, y_train) > 0.5


def test_model_evaluation(splitted_data):
    x_train, x_test, y_train, y_test = splitted_data
    model = _train_model(x_train, y_train)
    evaluation = _evaluate_model(model, x_test, y_test)
    assert model.score(x_test, y_test) == evaluation


def test_model_saving():
    build_model()
    model_path = f'{model_settings_obj.MODELS_FOLDER}/' \
                 f'{model_settings_obj.MODEL_NAME}'
    assert Path(model_path).exists()
