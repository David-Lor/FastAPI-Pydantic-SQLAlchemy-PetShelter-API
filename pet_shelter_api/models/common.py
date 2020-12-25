from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base

__all__ = ("ORMBase", "STRING_MAX_LENGTH", "STRING", "UUID")

ORMBase = declarative_base()
"""Declarative Base is used as base class for all the ORM models"""

STRING_MAX_LENGTH = 255
"""Generic limit of string columns"""
UUID_LENGTH = 36
"""Fixed length of an UUID for id columns"""

STRING = String(STRING_MAX_LENGTH)
"""String column type"""
UUID = String(UUID_LENGTH)
"""UUID column type"""
