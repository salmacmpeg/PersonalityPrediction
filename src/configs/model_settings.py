from pydantic import DirectoryPath
from pydantic_settings import BaseSettings, SettingsConfigDict


class ModelSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file='src/configs/.env',
                                      env_file_encoding='utf-8',
                                      extra='ignore')
    MODELS_FOLDER: DirectoryPath
    MODEL_NAME: str
    HIGH_SCORE_FILE_NAME: str


model_settings_obj = ModelSettings()
