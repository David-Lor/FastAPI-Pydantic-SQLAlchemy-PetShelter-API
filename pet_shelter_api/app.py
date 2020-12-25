import uvicorn
from fastapi import FastAPI

from .settings import api_settings as settings


app = FastAPI(title=settings.title)


def run():
    """Run the API using Uvicorn"""
    uvicorn.run(
        app,
        host=settings.host,
        port=settings.port
    )
