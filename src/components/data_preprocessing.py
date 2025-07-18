from src.components.data_loading import load_data
import pandas as pd
from loguru import logger


class DataPreprocessing():
    def __init__(self):
        self.data = load_data()

    def preprocess_data(self) -> pd.DataFrame:
        self._fillna()
        self._mapping()
        logger.info("Done preprocessing data")
        return self.data

    def _fillna(self) -> pd.DataFrame:

        numerical_features = self.data.select_dtypes(include='number').columns
        self.data[numerical_features] = self.data[numerical_features].fillna(
            self.data[numerical_features].mean())

        non_numerical_features = self.data.select_dtypes(exclude='number'
                                                         ).columns
        for feature in non_numerical_features:
            self.data[feature] = self.data[feature].fillna(
                self.data[feature].mode()[0])

    def _mapping(self) -> pd.DataFrame:

        features = ['Stage_fear', 'Drained_after_socializing', 'Personality']
        category_mappings = [
            {'No': 0, 'Yes': 1},
            {'No': 0, 'Yes': 1},
            {'Extrovert': 0, 'Introvert': 1},
        ]
        for feature, mappings in zip(features, category_mappings):
            self.data[feature] = self.data[feature].map(mappings)

        Featrures_to_be_ints = ['Time_spent_Alone',
                                'Social_event_attendance',
                                'Going_outside',
                                'Friends_circle_size',
                                'Post_frequency']
        for feat in Featrures_to_be_ints:
            self.data[feat] = self.data[feat].astype(int)
            self.data[feat] = self.data[feat].clip(0, 11)

        self.data = self.data.drop('id', axis=1)
