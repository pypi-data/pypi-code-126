from datetime import datetime
import random
import string

from sqlalchemy.orm import Session

from . import models, schemas
from .settings import settings


def randomword(length, among=string.ascii_letters + string.digits):
    return "".join(random.choice(among) for _ in range(length))


def delete(db: Session, item: models.Base):
    db.delete(item)
    db.commit()


def update(db: Session, item: models.Base):
    db.add(item)
    db.commit()
    db.refresh(item)


def get_thread(db: Session, thread_id: int) -> models.Thread:
    return db.query(models.Thread).filter(models.Thread.id == thread_id).first()


def get_threads(db: Session, skip: int = 0, limit: int = 100) -> list[models.Thread]:
    return db.query(models.Thread).offset(skip).limit(limit).all()


def get_thread_by_path(db: Session, path: str) -> models.Thread:
    return db.query(models.Thread).filter(models.Thread.path == path).first()


def get_comment(db: Session, comment_id: int) -> models.Comment:
    return db.query(models.Comment).filter(models.Comment.id == comment_id).first()


def create_thread(db: Session, thread_path: str):
    db_thread = models.Thread(path=thread_path)
    db_thread.auto_approve = settings.AUTO_APPROVE_NEW_THREADS
    db_thread.date_created = datetime.now()
    db_thread.locked = False
    update(db, db_thread)
    return db_thread


def create_comment(db: Session, comment: schemas.CommentCreateRequest):
    db_comment = models.Comment(**comment.dict())
    db_comment.date_created = datetime.now()
    db_comment.date_updated = None
    db_comment.update_key = randomword(50)
    db_comment.approved = get_thread(db, comment.thread_id).auto_approve
    db_comment.deleted = False
    update(db, db_comment)
    return db_comment


def update_comment(
    db: Session, comment: models.Comment, comment_patch: schemas.CommentPatch
):
    comment.date_updated = datetime.now()
    comment.text = comment_patch.text
    comment.author_name = comment_patch.author_name
    update(db, comment)
