from fastapi import FastAPI

from .api import router as api_router

__all__ = ("set_routes",)


def set_routes(app: FastAPI):
    app.include_router(api_router, prefix="", tags=["api"])
