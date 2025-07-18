from src.components.data_loading import load_data
import pandas as pd
import pytest


@pytest.fixture(scope="module")
def loaded_data():
    return load_data()


def test_data_loading_shape(loaded_data):
    assert loaded_data.shape[0] > 0 and loaded_data.shape[1] > 0
    assert True


def test_data_loading_type(loaded_data):
    assert isinstance(loaded_data, pd.DataFrame)
    assert True
