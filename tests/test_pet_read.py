from pet_shelter_api.models.pets.pet_read import PetRead

from .base_test import BaseAPITest
from .helpers import get_existing_pet


class TestGetPet(BaseAPITest):
    pet: PetRead

    @classmethod
    def setup_class(cls):
        super().setup_class()
        cls.pet = get_existing_pet()

    def request(self, pet_id: str):
        return self.client.get("/pets/" + pet_id)

    def test_get_pet(self):
        """Get an existing pet by its id.
        Should return 200 and the PetRead object as response body.
        """
        r = self.request(self.pet.pet_id)
        assert r.status_code == 200
        assert r.json() == self.pet.dict()

    # TODO test get non existing pet
    # def test_get_nonexisting_pet(self):
    #     ...
