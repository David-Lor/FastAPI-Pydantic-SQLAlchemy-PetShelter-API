from pydantic import Field

from .pet_create import PetCreate

__all__ = ("PetRead",)


class PetRead(PetCreate):
    pet_id: str = Field(..., description="Unique identifier of this pet in the system")
