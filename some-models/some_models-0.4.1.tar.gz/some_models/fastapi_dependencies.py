from collections.abc import Generator

from sqlalchemy.orm import sessionmaker, Session


class SessionDependency:
    def __init__(self, session_getter: sessionmaker):
        self.session_getter = session_getter

    def __call__(self) -> Generator[Session, None, None]:
        session = self.session_getter()
        try:
            yield session
        finally:
            session.close()
