from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import DirectoryPath, FilePath
from sqlalchemy import create_engine

class DbSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='config/.env', 
        env_file_encoding='utf-8',
        extra='ignore'
        )
    db_conn_str: str
    table_name: str


db_settings = DbSettings()

engine = create_engine(db_settings.db_conn_str)