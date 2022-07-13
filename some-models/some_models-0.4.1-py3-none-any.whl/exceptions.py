from sqlalchemy.exc import SQLAlchemyError


class ObjectNotFoundInDBError(SQLAlchemyError):
    pass
