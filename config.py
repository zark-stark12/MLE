#data_file_name
#model path
#model name

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import DirectoryPath, FilePath
from loguru import logger
from sqlalchemy import create_engine


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')
    data_file_name: str
    model_path: str
    model_name: str
    log_level: str
    db_conn_str: str
    table_name: str


settings = Settings()

logger.remove() # prevents log displaying in the console
logger.add('app.log', level=settings.log_level, rotation="1 day", retention="2 days", compression="zip")

engine = create_engine(settings.db_conn_str)