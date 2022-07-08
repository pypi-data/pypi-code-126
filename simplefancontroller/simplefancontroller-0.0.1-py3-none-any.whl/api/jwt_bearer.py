import time
import logging

import jwt
from fastapi import HTTPException, Request
from fastapi.responses import RedirectResponse
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from simplefancontroller.settings import SFCAPIConfig

logger = logging.getLogger(__name__)


def token_response(token: str):
    return {"access_token": token}


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(
            JWTBearer, self
        ).__call__(request)
        if not credentials:
            raise HTTPException(status_code=403, detail="Invalid authorization code.")
        if credentials.scheme != "Bearer":
            raise HTTPException(
                status_code=403, detail="Invalid authentication scheme."
            )
        token_data, token_valid = self.verify_jwt(credentials.credentials)
        if not token_valid and token_data:
            return RedirectResponse(token_data['redirect_uri'])
        elif not token_valid:
            raise HTTPException(
                status_code=403, detail="Invalid authentication."
            )
        request.username = credentials.credentials
        return credentials.credentials

    def verify_jwt(self, jwtoken: str) -> tuple[dict, bool]:
        isTokenValid: bool = False

        try:
            payload = self.decode_jwt(jwtoken)
        except:
            payload = None
        if payload:
            isTokenValid = True
        logger.info(payload)
        logger.info(isTokenValid)
        return payload, isTokenValid

    @staticmethod
    def sign_jwt(user_id: str) -> dict[str, str]:
        payload = {"user_id": user_id, "expires": time.time() + SFCAPIConfig.ttl, "redirect_uri": "/api/v1/users/login"}
        token = jwt.encode(
            payload, key=SFCAPIConfig.secret, algorithm=SFCAPIConfig.algorithm
        )
        return token_response(token)

    @staticmethod
    def decode_jwt(token: str) -> dict:
        try:
            decoded_token = jwt.decode(
                token, key=SFCAPIConfig.secret, algorithms=[SFCAPIConfig.algorithm]
            )
            return decoded_token if decoded_token["expires"] >= time.time() else None
        except jwt.DecodeError as e:
            logger.exception(e)
            raise
