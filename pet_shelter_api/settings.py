import os

import pydantic

__all__ = ("api_settings",)

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


api_settings = APISettings()
