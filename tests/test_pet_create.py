import pytest

from pet_shelter_api.models.pets.pet_read import PetRead
from pet_shelter_api.models.pets.pet_create import PetCreate
from pet_shelter_api.repositories.pets import PetRepository

from .base_test import BaseAPITest
from .helpers import get_pet_create
from .const import TestCases


class TestGetPet(BaseAPITest):
    def request(self, body: dict):
        return self.client.post("/pets", json=body)

    def test_create_pet(self):
        """Create a new pet providing a valid body.
        Should return 201 and the PetRead object as response body.
        The created pet should exist.
        """
        pet_create = get_pet_create()
        r = self.request(pet_create.dict())
        assert r.status_code == 201

        response_pet = PetRead(**r.json())
        pet_read = PetRepository.get(response_pet.pet_id)
        assert r.json() == pet_read.dict()

    @pytest.mark.parametrize("body", [
        pytest.param({"name": "foo"}, id="incomplete object"),
        *TestCases.Common.invalid_body_create
    ])
    def test_create_invalid_body(self, body):
        """Create a new pet providing invalid bodies.
        Should return 422.
        """
        r = self.request(body)
        assert r.status_code == 422
