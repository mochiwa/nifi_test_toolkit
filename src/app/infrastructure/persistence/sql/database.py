import logging
from contextlib import contextmanager, AbstractContextManager
from typing import Callable

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy.util.preloaded import orm

logger = logging.getLogger(__name__)

Base = declarative_base()


class Database:

    def __init__(self, url: str):
        self._engine = create_engine(url, echo=True)
        self._session_factory = orm.scoped_session(
            orm.sessionmaker(
                bind=self._engine,
                autoflush=True,
            )
        )
        self.create_database()

    def create_database(self) -> None:
        Base.metadata.create_all(self._engine)

    @contextmanager
    def session(self) -> Callable[..., AbstractContextManager[Session]]:
        session: Session = self._session_factory()
        try:
            yield session
        except Exception:
            logger.exception("Session rollback cause failure")
            session.rollback()
            raise
        finally:
            session.close()
