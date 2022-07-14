from fiopy.enums import BaseEnum

__all__ = ["AccountRole"]


class AccountRole(BaseEnum):
    OWNER = "owner"
    ADMIN = "admin"
    ACCOUNT_MANAGER = "account_manager"
    BILLING_MANAGER = "billing_manager"
