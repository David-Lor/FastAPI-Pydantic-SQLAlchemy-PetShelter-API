from pet_shelter_api.models.pets.pet_read import PetRead
from pet_shelter_api.models.pets.pet_create import PetCreate

from .base_test import BaseAPITest
from .helpers import get_pet_create


class TestGetPet(BaseAPITest):
    def request(self, body: dict):
        return self.client.post("/pets", json=body)

    def test_create_pet(self):
        pet_create = get_pet_create()
        r = self.request(pet_create.dict_alias())
        assert r.status_code == 201
