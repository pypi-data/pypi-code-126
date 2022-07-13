from fiopy.enums import BaseEnum

__all__ = ["UserRole"]


class UserRole(BaseEnum):
    OWNER = "owner"
    ADMIN = "admin"
    MANAGER = "manager"
    MEMBER = "member"
    COLLABORATOR = "collaborator"
