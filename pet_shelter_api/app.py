import uvicorn
from fastapi import FastAPI

from .routes.router import set_routes
from .settings import api_settings as settings


app = FastAPI(title=settings.title)
set_routes(app)


def run():
    """Run the API using Uvicorn"""
    uvicorn.run(
        app,
        host=settings.host,
        port=settings.port
    )
