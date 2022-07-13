from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class CommentBase(BaseModel):
    author_name: str
    text: str


class CommentCreateRequest(CommentBase):
    thread_id: int


class CommentUpdateMixin(BaseModel):
    update_key: Optional[str] = None


class CommentDelete(CommentUpdateMixin):
    pass


class CommentPatch(CommentBase, CommentUpdateMixin):
    pass


class CommentCreateResponse(CommentCreateRequest, CommentUpdateMixin):
    id: int
    update_key: str
    date_created: datetime

    class Config:
        orm_mode = True


class Comment(CommentCreateRequest, CommentUpdateMixin):
    id: int
    date_created: datetime
    date_updated: Optional[datetime] = None

    approved: bool
    deleted: bool

    class Config:
        orm_mode = True


class ThreadBase(BaseModel):
    path: str
    auto_approve: bool
    date_created: datetime
    locked: bool


class Thread(ThreadBase):
    id: int
    comments: list[Comment] = []

    class Config:
        orm_mode = True


class HTTPError(BaseModel):
    detail: str

    class Config:
        schema_extra = {
            "example": {"detail": "HTTPException raised."},
        }
