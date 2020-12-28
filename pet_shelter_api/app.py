import uvicorn
from fastapi import FastAPI

from .routes.router import set_routes
from .services.database import database
from .settings import api_settings as settings


app = FastAPI(title=settings.title)
set_routes(app)


@app.on_event("startup")
def app_setup():
    database.prepare()


def run():
    """Run the API using Uvicorn"""
    uvicorn.run(
        app,
        host=settings.host,
        port=settings.port
    )
