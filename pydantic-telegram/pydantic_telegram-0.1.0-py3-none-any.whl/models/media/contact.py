from pydantic import BaseModel


class Contact(BaseModel):
    phone_number: str
    first_name: str
    last_name: str = None
    user_id: int = None
    vcard: str = None
