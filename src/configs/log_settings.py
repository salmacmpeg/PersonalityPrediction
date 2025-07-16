from pydantic_settings import BaseSettings, SettingsConfigDict
from loguru import logger


class LoggerSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file='src/configs/.env',
                                      env_file_encoding='utf-8',
                                      extra='ignore')
    LOG_LEVEL: str


def configure_logging(log_level: str) -> None:
    """
    Configure the logging for the application.

    Args:
        log_level (str): The log level to be set for the logger.
    """
    logger.remove()
    logger.add('src/logs/personality.log',
               format='{time} {level} {message}',
               rotation='10 MB',
               retention='2 days',
               level=log_level)


configure_logging(log_level=LoggerSettings().LOG_LEVEL)
