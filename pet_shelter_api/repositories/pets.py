from typing import Optional

from sqlalchemy.orm import Session

from ..models.pets.pet_create import PetCreate
from ..models.pets.pet_orm import PetORM
from ..models.pets.pet_read import PetRead
from ..services.database import database

__all__ = ("PetRepository",)


class PetRepository:
    @classmethod
    def create(cls, pet_create: PetCreate):
        with database.session_scope() as session:
            pet_orm: PetORM = pet_create.to_orm()
            session.add(pet_orm)
            session.flush()
            # TODO Verify if the "get" is required, or the current "pet" object was already updated with the ORM-generated values
            return cls.get(pet_orm.pet_id, session=session)

    @classmethod
    def get(cls, pet_id: str, session: Optional[Session] = None) -> PetRead:
        with database.session_scope(session=session) as session:
            pet_orm: PetORM = session.query(PetORM).filter_by(pet_id=pet_id).one()
            return PetRead.from_orm(pet_orm)
