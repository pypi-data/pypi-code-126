import enum


class PackageManager(str, enum.Enum):
    PIP = "PIP"
    POETRY = "POETRY"
