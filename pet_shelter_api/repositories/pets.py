from .base import BaseRepository
from ..models.pets.pet_create import PetCreate
from ..models.pets.pet_orm import PetORM
from ..models.pets.pet_read import PetRead

__all__ = ("PetRepository",)


class PetRepository(BaseRepository):
    orm_model = PetORM
    orm_id_field_name = PetORM.pet_id.name
    read_model = PetRead
    create_model = PetCreate
