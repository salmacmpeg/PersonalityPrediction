from src.components.data_loading import load_data
import pandas as pd
from loguru import logger

data = load_data()


def preprocess_data() -> pd.DataFrame:

    data_filled = _fillna(data)

    mapped_data = _mapping(data_filled)

    logger.info("Done preprocessing data")

    return mapped_data


def _fillna(data: pd.DataFrame) -> pd.DataFrame:

    numerical_features = data.select_dtypes(include='number').columns
    data[numerical_features] = data[numerical_features].fillna(
        data[numerical_features].mean())

    non_numerical_features = data.select_dtypes(exclude='number').columns
    for feature in non_numerical_features:
        data[feature] = data[feature].fillna(data[feature].mode()[0])

    return data


def _mapping(data: pd.DataFrame) -> pd.DataFrame:

    features = ['Stage_fear', 'Drained_after_socializing', 'Personality']
    category_mappings = [
        {'No': 0, 'Yes': 1},
        {'No': 0, 'Yes': 1},
        {'Extrovert': 0, 'Introvert': 1},
    ]
    for feature, mappings in zip(features, category_mappings):
        data[feature] = data[feature].map(mappings)

    Featrures_to_be_ints = ['Time_spent_Alone',
                            'Social_event_attendance',
                            'Going_outside',
                            'Friends_circle_size',
                            'Post_frequency']
    for feat in Featrures_to_be_ints:
        data[feat] = data[feat].astype(int)
        data[feat] = data[feat].clip(0, 11)

    data = data.drop('id', axis=1)

    return data
