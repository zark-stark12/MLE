from loguru import logger
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import DirectoryPath, FilePath
from sqlalchemy import create_engine


class LoggerSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='config/.env', 
        env_file_encoding='utf-8', 
        extra='ignore',
        )
    log_level: str

def configure_logging(log_level: str) -> None:
    logger.remove()
    logger.add(
        'logs/app.log', 
        level=log_level, 
        rotation="1 day", 
        retention="2 days", 
        compression="zip",
        )

configure_logging(LoggerSettings().log_level)