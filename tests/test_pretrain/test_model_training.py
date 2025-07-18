from pathlib import Path
from src.components.data_preprocessing import DataPreprocessing
from src.components.model_all import (
    build_model,
    _get_x_y,
    _split_data,
    _train_model,
    _evaluate_model,
    _save_highest_model_score)
from src.configs import model_settings_obj
import pandas as pd
import pytest

pytestmark = pytest.mark.training


@pytest.fixture(scope="module")
def loaded_data():
    db_preprocessor = DataPreprocessing()
    data = db_preprocessor.preprocess_data()
    return data


@pytest.fixture(scope="module")
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
    x_train_copy = x_train.copy()
    x_test_copy = x_test.copy()
    x_train_copy['Personality'] = y_train
    x_test_copy['Personality'] = y_test
    concat_df = pd.concat([x_train_copy, x_test_copy], axis=0)
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


def test_save_highest_model_score_0(tmp_path):
    from src.configs import model_settings_obj
    old_file_name = model_settings_obj.HIGH_SCORE_FILE_NAME
    old_folder_name = model_settings_obj.MODELS_FOLDER

    model_settings_obj.HIGH_SCORE_FILE_NAME = "test_score.txt"
    model_settings_obj.MODELS_FOLDER = str(tmp_path)

    # Import the function
    _save_highest_model_score(0.9)
    # Test when the file does not exist

    with open(f'{tmp_path}/test_score.txt', 'r') as file:
        assert float(file.readline()) == 0.9

    model_settings_obj.HIGH_SCORE_FILE_NAME = old_file_name
    model_settings_obj.MODELS_FOLDER = old_folder_name


def test_save_highest_model_score_1(tmp_path):
    from src.configs import model_settings_obj
    old_file_name = model_settings_obj.HIGH_SCORE_FILE_NAME
    old_folder_name = model_settings_obj.MODELS_FOLDER

    model_settings_obj.HIGH_SCORE_FILE_NAME = "test_score.txt"
    model_settings_obj.MODELS_FOLDER = str(tmp_path)

    # Test when the file exists and the new score is lower
    _save_highest_model_score(0.9)
    _save_highest_model_score(0.8)
    with open(f'{tmp_path}/test_score.txt', 'r') as file:
        assert float(file.readline()) == 0.9

    model_settings_obj.HIGH_SCORE_FILE_NAME = old_file_name
    model_settings_obj.MODELS_FOLDER = old_folder_name


def test_save_highest_model_score_2(tmp_path):
    from src.configs import model_settings_obj
    old_file_name = model_settings_obj.HIGH_SCORE_FILE_NAME
    old_folder_name = model_settings_obj.MODELS_FOLDER

    model_settings_obj.HIGH_SCORE_FILE_NAME = "test_score.txt"
    model_settings_obj.MODELS_FOLDER = str(tmp_path)

    # Test when the file exists and the new score is higher
    _save_highest_model_score(0.7)
    _save_highest_model_score(1.0)
    with open(f'{tmp_path}/test_score.txt', 'r') as file:
        assert float(file.readline()) == 1.0

    model_settings_obj.HIGH_SCORE_FILE_NAME = old_file_name
    model_settings_obj.MODELS_FOLDER = old_folder_name
