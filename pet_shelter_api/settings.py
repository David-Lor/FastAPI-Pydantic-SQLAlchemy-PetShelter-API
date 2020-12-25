import os

import pydantic

__all__ = ("api_settings", "database_settings")

env_file = os.getenv("ENV_FILE", ".env")
"""Name/path of the .env file where settings can be read from"""


class BaseSettings(pydantic.BaseSettings):
    class Config:
        env_file = env_file


class APISettings(BaseSettings):
    host: str = "0.0.0.0"
    port: int = 5000
    title: str = "Pet Shelter API"

    class Config(BaseSettings.Config):
        env_prefix = "API_"


class DatabaseSettings(BaseSettings):
    host: str = "127.0.0.2"
    port: int = 3306
    user: str
    password: str
    database: str = "pet-shelter"

    @property
    def uri(self):
        return f"mysql+pymysql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"

    class Config(BaseSettings.Config):
        env_prefix = "DB_"


api_settings = APISettings()
database_settings = DatabaseSettings()
