from pet_shelter_api.models.pets.pet_create import PetCreate
from pet_shelter_api.repositories.pets import PetRepository

__all__ = ("get_pet_create", "get_existing_pet")


def get_pet_create(**kwargs) -> PetCreate:
    return PetCreate(**{
        "name": "Ciri",
        "animal_type": "cat",
        **kwargs
    })


def get_existing_pet(**kwargs):
    pet_create = get_pet_create(**kwargs)
    return PetRepository.create(pet_create)
