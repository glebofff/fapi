import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    db_url: str = 'postgresql:///fapi'
    db_pool_size: int = 20
    db_pool_timeout: int = 50


SETTINGS = Settings()
DEBUG = False
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

