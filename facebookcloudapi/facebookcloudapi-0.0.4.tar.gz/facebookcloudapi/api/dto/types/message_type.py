from enum import Enum


class MessageType(Enum):
    TEXT = "text"
    IMAGE = "image"
    AUDIO = "audio"
    DOCUMENT = "document"
    TEMPLATE = "template"
    HSM = "hsm"
    CONTACTS = "contacts"
    INTERACTIVE = "interactive"
    LOCATION = "location"

