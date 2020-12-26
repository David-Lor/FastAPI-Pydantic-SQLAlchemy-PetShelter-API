from fastapi import FastAPI

from .api import router as api_router
from .pets import router as pets_router

__all__ = ("set_routes",)


def set_routes(app: FastAPI):
    app.include_router(api_router, prefix="", tags=["api"])
    app.include_router(pets_router, prefix="/pets", tags=["pets"])
