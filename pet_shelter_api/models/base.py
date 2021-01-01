import pydantic
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base

from ..services.database import database
from ..helpers import snakecase_to_camelcase

__all__ = ("ORMBase", "STRING_MAX_LENGTH", "STRING", "UUID", "BaseModel")

# TODO remove bind (not required when using alembic)
ORMBase = declarative_base(bind=database)
"""Declarative Base is used as base class for all the ORM models"""

STRING_MAX_LENGTH = 255
"""Generic limit of string columns"""
UUID_LENGTH = 36
"""Fixed length of an UUID for id columns"""

STRING = String(STRING_MAX_LENGTH)
"""String column type"""
UUID = String(UUID_LENGTH)
"""UUID column type"""


class BaseModel(pydantic.BaseModel):
    """Custom pydantic BaseModel used widely on all the API models. Features:

    - all model fields, defined as camel_case (standard Python notation), are automatically aliased with their
      camelCase representation. Request and response models will use the camelCase (more canonical for JSON)
    - "dict" method outputs aliased (camelCase) variable names
    - strip whitespaces on any string
    - orm_mode enabled
    - new "to_orm" method to convert a BaseModel instance into its associated ORM class model
    """

    class Config:
        orm_mode = True
        orm_model = None
        anystr_strip_whitespace = True
        allow_population_by_field_name = True
        alias_generator = snakecase_to_camelcase

    def dict(self, *args, **kwargs):
        # TODO force exclude_none=True on dict() method, if required
        kwargs.setdefault("by_alias", True)
        return super().dict(*args, **kwargs)

    def to_orm(self) -> ORMBase:
        """Return an instance of the ORM class defined in Config.orm_model, with the current data of the object"""
        if not self.Config.orm_model:
            raise AttributeError("Config.orm_model is undefined")
        return self.Config.orm_model(**self.dict(by_alias=False))
