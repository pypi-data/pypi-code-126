from typing import List

from pydantic import BaseModel
from telegram_pydantic.models.passport.encrypted_credentials import EncryptedCredentials
from telegram_pydantic.models.passport.encypted_passport_element import EncryptedPassportElement


class PassportData(BaseModel):
    data: List[EncryptedPassportElement]
    credentials: EncryptedCredentials
