from fastapi import APIRouter

from ..models.pets.pet_create import PetCreate

__all__ = ("router",)

from ..models.pets.pet_read import PetRead
from ..repositories.pets import PetRepository

router = APIRouter()


@router.get("/{pet_id}", description="Get a single existing ped by its unique identifier", response_model=PetRead)
def get_pet(pet_id: str):
    return PetRepository.get(pet_id)


@router.post("", description="Create a new pet", response_model=PetRead)
def create_pet(pet_create: PetCreate):
    return PetRepository.create(pet_create)
