from pydantic_settings import BaseSettings
from logs import logger_instance
import os
class Settings(BaseSettings):
    app_name: str = "Geral"
    debug: bool

    class Config:
        env_file = os.path.join(os.path.dirname(__file__), 'config.env')
        env_file_encoding = 'utf-8'
