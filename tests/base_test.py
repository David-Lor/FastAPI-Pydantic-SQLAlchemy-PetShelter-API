from fastapi.testclient import TestClient
from requests import Session

from pet_shelter_api import app

from .helpers import clear_database

__all__ = ("BaseAPITest",)


class BaseAPITest:
    """Base API test class that starts a fastapi TestClient (https://fastapi.tiangolo.com/tutorial/testing/)"""
    client: Session

    @classmethod
    def setup_class(cls):
        with TestClient(app) as client:
            # Usage of context-manager to trigger app events when using TestClient:
            # https://fastapi.tiangolo.com/advanced/testing-events/
            cls.client = client

    @classmethod
    def teardown_class(cls):
        clear_database()
