from configs import db_settings_obj
import pandas as pd


def load_data() -> pd.DataFrame:
    print(db_settings_obj.DATA_FILE_PATH)
    data = pd.read_csv(db_settings_obj.DATA_FILE_PATH)
    print(f"Loaded data with dimentions: {data.shape}")
    return data
