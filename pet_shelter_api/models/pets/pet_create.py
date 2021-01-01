from pydantic import Field

from .pet_orm import PetORM
from ..base import BaseModel

__all__ = ("PetCreate",)


class PetCreate(BaseModel):
    name: str = Field(..., description="Name of the pet", example="Max")
    animal_type: str = Field(..., description="Type of animal this pet is", example="dog")

    class Config(BaseModel.Config):
        orm_model = PetORM
