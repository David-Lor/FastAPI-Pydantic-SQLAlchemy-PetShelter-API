import contextlib
from typing import Optional

import wait4it
import sqlalchemy
from sqlalchemy.orm import Session, sessionmaker

from ..settings import database_settings as settings

__all__ = ("database",)


class Database:
    def __init__(self):
        self._uri = settings.uri
        self._engine = self._create_engine()
        self._sessionmaker = sessionmaker(bind=self._engine)

    def _create_engine(self) -> sqlalchemy.engine.Engine:
        return sqlalchemy.create_engine(self._uri)

    def close(self):
        self._engine.dispose()

    def get_session(self) -> Session:
        return self._sessionmaker()

    @contextlib.contextmanager
    def session_scope(self, session: Optional[Session] = None):
        if not session:
            session = self.get_session()

        try:
            yield session
            session.commit()

        except Exception as ex:
            session.rollback()
            raise ex

        finally:
            session.close()

    @staticmethod
    def wait_for(timeout: float = 5):
        wait4it.wait_for(host=settings.host, port=settings.port, timeout=timeout)


database = Database()
