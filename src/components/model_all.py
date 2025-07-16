from .data_preprocessing import preprocess_data
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import pickle as pk
from configs import model_settings_obj
from loguru import logger


data = preprocess_data()


def build_model():
    X, y = _get_x_y(data)
    X_train, X_test, y_train, y_test = _split_data(X, y)
    model = _train_model(X_train, y_train)
    accuracy = _evaluate_model(model, X_test, y_test)
    logger.info(f"Built model with evaluation accuracy: {accuracy}")
    _save_model(model)


def _get_x_y(data: pd.DataFrame):
    X = data.drop('Personality', axis=1)
    y = data['Personality']
    return X, y


def _split_data(X: pd.DataFrame, y: pd.Series):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,
                                                        random_state=42)
    return X_train, X_test, y_train, y_test


def _train_model(X_train: pd.DataFrame, y_train: pd.Series):
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)
    return model


def _evaluate_model(model: DecisionTreeClassifier, X_test: pd.DataFrame,
                    y_test: pd.Series):
    accuracy = model.score(X_test, y_test)
    return accuracy


def _save_model(model):
    model_path = f'{model_settings_obj.MODELS_FOLDER}/' \
                 f'{model_settings_obj.MODEL_NAME}'
    with open(model_path, 'wb') as model_file:
        pk.dump(model, model_file)
        logger.info("Saved model successfully")
