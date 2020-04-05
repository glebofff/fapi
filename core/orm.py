import sqlalchemy as sql
from sqlalchemy import MetaData
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.pool import QueuePool
from sqlalchemy.ext.declarative import declarative_base, as_declarative
from .settings import SETTINGS

engine = sql.create_engine(
    SETTINGS.db_url, poolclass=QueuePool,
    pool_size=SETTINGS.db_pool_size,
    pool_timeout=SETTINGS.db_pool_timeout
)

metadata = MetaData(engine)
registry = {}


@as_declarative(bind=engine, class_registry=registry)
class Base(object):
    pass


def create_session(scopefunc=None):
    return scoped_session(sessionmaker(bind=engine), scopefunc=scopefunc)


class new_session(object):
    def __init__(self):
        self.session = create_session(self.__enter__)

    def __enter__(self):
        return self.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.remove()
