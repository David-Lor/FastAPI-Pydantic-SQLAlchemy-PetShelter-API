from fastapi import APIRouter
from fastapi import status as statuscode

from ..models.pets.pet_create import PetCreate

__all__ = ("router",)

from ..models.pets.pet_read import PetRead
from ..repositories.pets import PetRepository

router = APIRouter()


@router.get("/{pet_id}", response_model=PetRead, description="Get a single existing ped by its unique identifier")
def get_pet(pet_id: str):
    return PetRepository.get(pet_id)


@router.post("", response_model=PetRead, status_code=statuscode.HTTP_201_CREATED, description="Create a new pet",)
def create_pet(pet_create: PetCreate):
    return PetRepository.create(pet_create)
