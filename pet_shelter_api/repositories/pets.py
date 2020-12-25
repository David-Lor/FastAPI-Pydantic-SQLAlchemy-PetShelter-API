from typing import Optional

from sqlalchemy.orm import Session

from ..models.pets.pet_orm import PetORM
from ..services.database import database

__all__ = ("PetRepository",)


class PetRepository:
    @classmethod
    def create(cls, pet: PetORM):
        with database.session_scope() as session:
            session.add(pet)
            session.flush()
            # TODO Verify if the "get" is required, or the current "pet" object was already updated with the ORM-generated values
            return cls.get(pet.pet_id, session=session)

    @classmethod
    def get(cls, pet_id: str, session: Optional[Session]):
        with database.session_scope(session=session) as session:
            return session.query(PetORM).filter_by(pet_id=pet_id).one()
