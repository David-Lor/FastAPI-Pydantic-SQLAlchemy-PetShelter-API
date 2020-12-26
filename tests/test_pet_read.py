from pet_shelter_api.models.pets.pet_read import PetRead

from .base_test import BaseAPITest
from .helpers import *


class TestGetPet(BaseAPITest):
    pet: PetRead

    @classmethod
    def setup_class(cls):
        cls.pet = get_existing_pet()

    def request(self, pet_id: str):
        r = self.client.get("/pets/" + pet_id)
        r.raise_for_status()
        return r

    def test_get_pet(self):
        r = self.request(self.pet.pet_id)
        assert r.status_code == 200
        assert r.json() == self.pet.dict()
