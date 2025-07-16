"""Configuration file for pydantic settings for the data base"""

from pydantic import FilePath
from pydantic_settings import BaseSettings, SettingsConfigDict


class DBSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file='src/configs/.env',
                                      env_file_encoding='utf-8',
                                      extra='ignore')

    DATA_FILE_PATH: FilePath


db_settings_obj = DBSettings()
# print(db_settings_obj.DATA_FILE_PATH)
