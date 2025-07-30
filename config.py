#data_file_name
#model path
#model name

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import DirectoryPath, FilePath

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')
    data_file_name: str
    model_path: str
    model_name: str

settings = Settings()