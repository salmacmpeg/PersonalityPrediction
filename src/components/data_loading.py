from configs import db_settings_obj
import pandas as pd
from loguru import logger


def load_data() -> pd.DataFrame:
    logger.info("Loading data ...")
    data = pd.read_csv(db_settings_obj.DATA_FILE_PATH)
    logger.info(f"Loaded data with dimentions: {data.shape}")
    return data
