from typing import List

from pydantic import BaseModel
from telegram_pydantic.models.passport.passport_file import PassportFile


class EncryptedPassportElement(BaseModel):
    type: str
    data: str = None
    phone_number: str = None
    email: str = None
    files: List[PassportFile] = None
    front_side: PassportFile = None
    reverse_side: PassportFile = None
    selfie: PassportFile = None
    translation: List[PassportFile] = None
    hash: str
