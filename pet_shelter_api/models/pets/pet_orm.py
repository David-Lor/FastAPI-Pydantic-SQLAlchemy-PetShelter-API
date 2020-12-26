from sqlalchemy import Column

from ..common import ORMBase, UUID, STRING
from ...helpers import get_uuid


class PetORM(ORMBase):
    __tablename__ = "pets"

    pet_id = Column(UUID, primary_key=True, default=get_uuid)
    name = Column(STRING, nullable=False)
    animal_type = Column(STRING, nullable=False)
