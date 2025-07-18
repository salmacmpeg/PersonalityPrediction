from src.components.data_preprocessing import DataPreprocessing
import pandas as pd
import pytest

pytestmark = pytest.mark.pretrain


def test_DataPreprocessing_loaddata():
    db_preprocessor = DataPreprocessing()
    data = db_preprocessor.data
    assert data is not None


def test_DataPreprocessing_fillna():
    db_preprocessor = DataPreprocessing()
    db_preprocessor._fillna()
    data = db_preprocessor.data
    assert not data.isna().any().any()


def test_DataPreprocessing_mapping():
    db_preprocessor = DataPreprocessing()
    db_preprocessor._fillna()
    db_preprocessor._mapping()
    data = db_preprocessor.data
    assert all(pd.api.types.is_integer_dtype(data[col])
               for col in data.columns), "Not all columns are integer types"


def test_DataPreprocessing_final():
    db_preprocessor = DataPreprocessing()
    data = db_preprocessor.preprocess_data()
    assert all(pd.api.types.is_integer_dtype(data[col])
               for col in data.columns) and not data.isna().any().any()
