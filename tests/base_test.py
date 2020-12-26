from fastapi.testclient import TestClient

from pet_shelter_api import app
from pet_shelter_api.services.database import database

__all__ = ("BaseAPITest",)


class BaseAPITest:
    """Base API test class that starts a fastapi TestClient (https://fastapi.tiangolo.com/tutorial/testing/)"""
    client: TestClient

    @classmethod
    def setup_class(cls):
        cls.client = TestClient(app)
        database.wait_for()
