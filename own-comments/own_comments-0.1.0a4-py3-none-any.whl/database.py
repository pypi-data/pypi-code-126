from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .settings import settings


def get_session_local():
    global instance
    global engine
    if instance is None:
        engine = get_engine()
        instance = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return instance


def get_engine():
    global engine
    if engine is None:
        engine = create_engine(
            settings.SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
        )
    return engine


Base = declarative_base()

instance = None
engine = None
