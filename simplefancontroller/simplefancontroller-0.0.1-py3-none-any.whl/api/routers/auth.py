import logging

from fastapi import APIRouter, Body, HTTPException, Request, Depends

from ..jwt_bearer import JWTBearer
from ..schemas import User, UserLoginSchema, UserPassUpdateSchema
from .controller import USER_MANAGER

auth_router = APIRouter(tags=["user"], prefix="/api/v1/users")

logger = logging.getLogger(__name__)


def user_login_check(user: UserPassUpdateSchema, request: Request):
    if USER_MANAGER.check_user_password(request.user.email, user.password):
        return True
    else:
        raise HTTPException(status_code=401)


@auth_router.post("/signup")
async def create_user(user: User = Body(...)):
    """Creates a new SFC User."""
    try:
        USER_MANAGER.add_user(user)
        return JWTBearer.sign_jwt(user.email)
    except ValueError as e:
        logger.debug(e)
        return HTTPException(
            status_code=500,
            detail=f"User with email address {user.email} already exists.",
        )


@auth_router.post("/login")
async def user_login(user: UserLoginSchema = Body(...)):
    """Login a SFC User."""
    if USER_MANAGER.check_user_password(user.email, user.password):
        return JWTBearer.sign_jwt(user.email)
    return HTTPException(status_code=401)


@auth_router.post("/change_password", dependencies=[Depends(JWTBearer())])
async def user_change_password(user: UserPassUpdateSchema, request: Request):
    """Change a SFC User's password"""
    USER_MANAGER.delete_user(email=request.user.email)
    USER_MANAGER.add_user(
        User(
            name=request.user.name, email=request.user.email, password=user.new_password
        )
    )


@auth_router.delete("/{email}", dependencies=[Depends(JWTBearer())])
async def delete_user(email: str):
    """Delete a SFC User."""
    if not USER_MANAGER.get_user_by_mail(email):
        raise HTTPException(
            status_code=500, detail=f"No user with email address {email} found."
        )
    USER_MANAGER.delete_user(email)


@auth_router.get("", response_model=list[User], dependencies=[Depends(JWTBearer())])
async def get_users():
    """Get a list of all stored SFC Users"""
    return USER_MANAGER.get_users()


@auth_router.get("/{email}", response_model=User, dependencies=[Depends(JWTBearer())])
async def get_user(email: str):
    """Get a single SFC User by email."""
    user = USER_MANAGER.get_user_by_mail(email)
    if not user:
        raise HTTPException(
            status_code=500, detail=f"No user with email address {email} found."
        )
    return user


# todo: add route for updating a user
