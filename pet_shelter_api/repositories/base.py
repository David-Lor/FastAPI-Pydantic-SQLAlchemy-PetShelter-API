from typing import Optional

from sqlalchemy.orm import Session

from ..models.base import BaseModel, ORMBase
from ..services.database import database

__all__ = ("BaseRepository",)


class BaseRepository:
    orm_model = ORMBase
    orm_id_field_name = ""
    read_model = BaseModel
    create_model = BaseModel
    database = database

    # @classmethod
    # @abc.abstractmethod
    # def get_orm_model(cls) -> ORMBase:
    #     """Returns the ORM class model for this repository"""
    #     pass
    #
    # @classmethod
    # @abc.abstractmethod
    # def get_orm_object_id(cls, orm_object: ORMBase):
    #     """Given an ORM object, return its id"""
    #     pass

    @classmethod
    def create(cls, create: create_model) -> read_model:
        with database.session_scope() as session:
            create_orm = create.to_orm()

            session.add(create_orm)
            session.flush()

            return cls.read_model.from_orm(create_orm)

    @classmethod
    def get(cls, _id, session: Optional[Session] = None) -> read_model:
        with database.session_scope(session=session) as session:
            filter_by = {cls.orm_id_field_name: _id}
            read_orm = session.query(cls.orm_model).filter_by(**filter_by).one()
            return cls.read_model.from_orm(read_orm)

    @classmethod
    def delete_all(cls):
        with database.session_scope() as session:
            session.query(cls.orm_model).delete()
