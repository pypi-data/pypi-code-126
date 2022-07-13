import base64
import secrets
from typing import Optional, Union

from fastapi import Depends, HTTPException
from fastapi.security import HTTPBasicCredentials, HTTPBasic
from sqlalchemy.orm import Session
from starlette.requests import Request

from . import models, schemas, crud
from .database import get_session_local, get_engine
from .settings import settings


security = HTTPBasic()


def get_db():
    db = get_session_local()()
    models.Base.metadata.create_all(bind=get_engine())
    try:
        yield db
    finally:
        db.close()


def require_admin(credentials: HTTPBasicCredentials = Depends(security)):
    if not is_admin(credentials):
        raise HTTPException(403)


def is_admin(credentials: Optional[HTTPBasicCredentials]):
    return (
        credentials is not None
        and credentials.username is not None
        and credentials.password is not None
        and secrets.compare_digest(
            credentials.username, settings.ADMIN_USERNAME
        )
        and secrets.compare_digest(
            credentials.password, settings.ADMIN_PASS
        )
    )


def get_basic_auth(request: Request):
    h: str = request.headers.get("Authorization")
    if h is not None and h.startswith("Basic "):
        creds = base64.b64decode(h[6:]).decode()
        u, p = creds.split(":")
        return HTTPBasicCredentials(username=u, password=p)


def check_update_key(
    comment: models.Comment, comment_update: schemas.CommentUpdateMixin
):
    return comment_update.update_key is not None and secrets.compare_digest(
        comment_update.update_key, comment.update_key
    )


def get_comment_if_authorized(
    db: Session,
    comment_id: int,
    credentials: Optional[HTTPBasicCredentials],
    comment_update: Optional[Union[schemas.CommentPatch, schemas.CommentDelete]],
):
    comment = crud.get_comment(db, comment_id)
    if comment is None:
        raise HTTPException(404, detail="Comment ID not found")
    if credentials is not None and is_admin(credentials):
        return comment
    if comment_update is not None and check_update_key(comment, comment_update):
        return comment
    raise HTTPException(403, detail="You are not allowed to delete this comment")
