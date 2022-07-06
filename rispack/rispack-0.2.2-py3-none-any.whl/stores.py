from rispack.database import Database
from contextlib import contextmanager
from rispack.logger import logger
from functools import wraps


def atomic(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        session = BaseStore.database.session
        in_transaction = session.in_transaction()

        result = func(*args, **kwargs)

        if not in_transaction:
            logger.debug("Not in transaction, committing...")
            session.commit()

        return result

    return wrapper


class BaseStore:
    database = None

    def __init__(self):
        if not BaseStore.database:
            BaseStore.database = Database()

        self.session = BaseStore.database.session

    @atomic
    def add(self, entity):
        self.session.add(entity)

        return entity

    @atomic
    def add_all(self, entities):
        self.session.add_all(entities)

        return entities

    def get_mapper(self):
        raise NotImplementedError

    def filter_by(self, **kwargs):
        return self.session.query(self.get_mapper()).filter_by(**kwargs)

    def find(self, id: int):
        return self.filter_by(id=id).first()

    def find_by(self, **kwargs):
        return self.filter_by(**kwargs).first()

    def where(self, **kwargs):
        return self.filter_by(**kwargs).all()


@contextmanager
def begin_transaction():
    with BaseStore().database.session.begin():
        yield
