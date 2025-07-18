from pathlib import Path
from src.components.data_preprocessing import DataPreprocessing
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import pickle as pk
from src.configs import model_settings_obj
from loguru import logger


def build_model():
    db_preprocessor = DataPreprocessing()
    data = db_preprocessor.preprocess_data()
    X, y = _get_x_y(data)
    X_train, X_test, y_train, y_test = _split_data(X, y)
    model = _train_model(X_train, y_train)
    accuracy = _evaluate_model(model, X_test, y_test)
    logger.info(f"Built model with evaluation accuracy: {accuracy}")
    _save_model(model)


def _get_x_y(data: pd.DataFrame):
    logger.debug(f"loaded data  with shapes: {data.shape}")
    data.drop_duplicates(inplace=True)
    logger.debug(f"after removing duplicates it became: {data.shape}")
    X = data.drop('Personality', axis=1)
    y = data['Personality']
    return X, y


def _split_data(X: pd.DataFrame, y: pd.Series):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,
                                                        random_state=42)
    logger.debug(f"Split data  with shapes: {X_train.shape}, {X_test.shape}")
    return X_train, X_test, y_train, y_test


def _train_model(X_train: pd.DataFrame, y_train: pd.Series):
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train, y_train)
    logger.debug(f'Model {type(model).__name__} has been trained with train ' +
                 f'score: {model.score(X_train, y_train)}')
    return model


def _evaluate_model(model: DecisionTreeClassifier, X_test: pd.DataFrame,
                    y_test: pd.Series):
    accuracy = model.score(X_test, y_test)
    logger.debug(f'Model {type(model).__name__} has been evaluated with ' +
                 f'test score: {accuracy}')
    _save_highest_model_score(accuracy)
    return accuracy


def _save_model(model):
    model_path = f'{model_settings_obj.MODELS_FOLDER}/' \
                 f'{model_settings_obj.MODEL_NAME}'
    with open(model_path, 'wb') as model_file:
        pk.dump(model, model_file)
        logger.info("Saved model successfully")


def _save_highest_model_score(score: float):
    file_path = f'{model_settings_obj.MODELS_FOLDER}/' \
                 f'{model_settings_obj.HIGH_SCORE_FILE_NAME}'
    logger.debug(f'inside save highest score, and the path is: {file_path} ')
    if not Path(file_path).exists():
        with open(file_path, mode='w') as file:
            file.write(str(score))
    else:
        with open(file_path, mode='r+') as file:
            old_score_str = file.readline()
            old_score = float(old_score_str)
            if score > old_score:
                file.seek(0)
                file.write(str(score))
                file.truncate()
