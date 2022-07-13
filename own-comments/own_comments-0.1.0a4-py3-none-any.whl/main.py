import asyncio
import urllib.parse
from pathlib import Path
from typing import Optional

from fastapi import Depends, FastAPI, HTTPException, Form, Request
from fastapi.security import HTTPBasicCredentials
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from starlette import status

from . import crud, schemas, notification
from .helpers import (
    get_db,
    require_admin,
    is_admin,
    get_basic_auth,
    get_comment_if_authorized,
)
from .settings import settings


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=settings.ALLOW_ORIGIN_REGEX,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

try:
    app.mount(
        "/static",
        StaticFiles(directory=Path(__file__).parent.parent / "dist"),
        name="static",
    )
except RuntimeError:
    pass


@app.get("/thread_by_path", response_model=schemas.Thread)
def get_thread_by_path(
    path: str, db: Session = Depends(get_db), credentials=Depends(get_basic_auth)
) -> schemas.Thread:
    """
    Gogogo

    :param path:
    :param db:
    :param credentials:
    """
    t = crud.get_thread_by_path(db, path)
    if t is None:
        t = crud.create_thread(db, path)
    if not is_admin(credentials):
        t.make_public()
    return t


@app.get("/thread_by_referer", response_class=RedirectResponse)
def get_thread_by_referer(request: Request):
    referer = request.headers.get("referer")
    if referer is None:
        raise HTTPException(422, detail="Referer header not found, cannot proceed")
    thread_path = urllib.parse.urlparse(referer).path
    return f"{settings.URL_PREFIX}/thread_by_path?path={thread_path}"


@app.get(
    "/threads/",
    response_model=list[schemas.Thread],
    dependencies=[Depends(require_admin)],
)
def get_threads(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
):
    return crud.get_threads(db, skip=skip, limit=limit)


@app.get("/threads/{thread_id}", response_model=schemas.Thread)
def get_thread(
    thread_id: int, db: Session = Depends(get_db), credentials=Depends(get_basic_auth)
):
    t = crud.get_thread(db, thread_id)
    if t is None:
        raise HTTPException(404, detail="Thread not found")
    if credentials is None or not is_admin(credentials):
        t.make_public()
    return t


@app.delete(
    "/threads/{thread_id}",
    response_model=schemas.Thread,
    dependencies=[Depends(require_admin)],
)
def delete_thread(
    thread_id: int,
    db: Session = Depends(get_db),
):
    thread = crud.get_thread(db, thread_id)
    crud.delete(db, thread)


@app.patch("/threads/{thread_id}/lock", dependencies=[Depends(require_admin)])
def lock_thread(
    thread_id: int,
    lock: bool = True,
    db: Session = Depends(get_db),
):
    t = crud.get_thread(db, thread_id)
    t.locked = lock
    crud.update(db, t)


@app.post(
    "/comments/",
    response_model=schemas.CommentCreateResponse,
    responses={403: {"model": schemas.HTTPError}, 404: {"model": schemas.HTTPError}},
)
async def create_comment(
    comment_create: schemas.CommentCreateRequest, db: Session = Depends(get_db)
):
    thread = crud.get_thread(db, thread_id=comment_create.thread_id)
    if thread is None:
        raise HTTPException(404, detail="Thread ID not found")
    if thread.locked:
        raise HTTPException(403, detail="This thread is locked")

    comment = crud.create_comment(db, comment_create)
    asyncio.create_task(notification.comment_added(comment))
    return comment


@app.post(
    "/comments/form",
    responses={403: {"model": schemas.HTTPError}, 404: {"model": schemas.HTTPError}},
)
async def create_comment_form(
    request: Request,
    author_name: str = Form(),
    text: str = Form(),
    db: Session = Depends(get_db),
):
    referer = request.headers.get("referer")
    if referer is None:
        raise HTTPException(422, detail="Referer header not found, cannot proceed")
    thread_path = urllib.parse.urlparse(referer).path
    thread = crud.get_thread_by_path(db, thread_path)

    if thread is None:
        thread = crud.create_thread(db, thread_path)
    if thread.locked:
        raise HTTPException(403, detail="This thread is locked")

    comment = crud.create_comment(
        db,
        schemas.CommentCreateRequest(
            thread_id=thread.id, author_name=author_name, text=text
        ),
    )
    asyncio.create_task(notification.comment_added(comment))
    return RedirectResponse(referer, status_code=status.HTTP_302_FOUND)


@app.get("/comments/{comment_id}")
async def get_comment(
    comment_id: int,
    db: Session = Depends(get_db),
    credentials: Optional[HTTPBasicCredentials] = Depends(get_basic_auth),
):
    c = crud.get_comment(db, comment_id)
    if c is None:
        raise HTTPException(404, "Comment not found")
    if credentials is None or not is_admin(credentials):
        c.make_public()
    return c


@app.delete("/comments/{comment_id}")
async def delete_comment(
    comment_id: int,
    purge: bool = False,
    comment_delete: Optional[schemas.CommentDelete] = None,
    db: Session = Depends(get_db),
    credentials: Optional[HTTPBasicCredentials] = Depends(get_basic_auth),
):
    comment = get_comment_if_authorized(db, comment_id, credentials, comment_delete)
    thread = crud.get_thread(db, comment.thread_id)
    if thread.locked and not is_admin(credentials):
        raise HTTPException(403, "This thread is locked")
    if purge:
        if is_admin(credentials) and purge:
            crud.delete(db, comment)
        else:
            raise HTTPException(403, "Only the admin can purge")
    else:
        comment.deleted = True
        crud.update(db, comment)
    asyncio.create_task(notification.comment_deleted(comment))


@app.patch("/comments/{comment_id}/undelete")
async def undelete_comment(
    comment_id: int,
    comment_delete: Optional[schemas.CommentDelete] = None,
    db: Session = Depends(get_db),
    credentials: Optional[HTTPBasicCredentials] = Depends(get_basic_auth),
):
    comment = get_comment_if_authorized(db, comment_id, credentials, comment_delete)
    thread = crud.get_thread(db, comment.thread_id)
    if thread.locked and not is_admin(credentials):
        raise HTTPException(403, "This thread is locked")
    comment.deleted = False
    crud.update(db, comment)


@app.patch("/comments/{comment_id}")
async def patch_comment(
    comment_id: int,
    comment_patch: schemas.CommentPatch,
    db: Session = Depends(get_db),
    credentials: Optional[HTTPBasicCredentials] = Depends(get_basic_auth),
):
    comment = get_comment_if_authorized(db, comment_id, credentials, comment_patch)
    thread = crud.get_thread(db, comment.thread_id)
    if thread.locked and not is_admin(credentials):
        raise HTTPException(403, "This thread is locked")
    crud.update_comment(db, comment, comment_patch)
    asyncio.create_task(notification.comment_updated(comment))


@app.patch("/comments/{comment_id}/approve", dependencies=[Depends(require_admin)])
async def approve_comment(comment_id: int, db: Session = Depends(get_db)):
    comment = crud.get_comment(db, comment_id)
    comment.approved = True
    crud.update(db, comment)


@app.patch("/comments/{comment_id}/unapprove", dependencies=[Depends(require_admin)])
async def unapprove_comment(comment_id: int, db: Session = Depends(get_db)):
    comment = crud.get_comment(db, comment_id)
    comment.approved = False
    crud.update(db, comment)


@app.get(
    "/auth",
    dependencies=[Depends(require_admin)],
    responses={403: {"model": schemas.HTTPError}},
)
def check_auth():
    """
    Verify that admin HTTP basic credentials are valid
    """
    pass
