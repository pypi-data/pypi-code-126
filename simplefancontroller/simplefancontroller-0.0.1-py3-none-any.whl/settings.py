from secrets import token_urlsafe

from dataclasses import dataclass

from decouple import config


def _generate_secret(n: int = 32) -> str:
    return token_urlsafe(n)


@dataclass
class SFCAPIConfig:
    secret: str = _generate_secret()
    algorithm: str = config("SFC_API_ALGORITHM", default="HS256")
    ttl: int = config("SFC_API_TOKEN_TTL", default=600, cast=int)
    db_user_file: str = config("SFC_API_DB", default="sfc_users.db")
    db_data_file: str = config("SFC_API_DB", default="sfc_data.db")
    db_user_table: str = config("SFC_API_DB_USER_TABLE", default="USERS")
    db_fan_table: str = config("SFC_API_DB_FAN_TABLE", default="FANS")
    db_persistence_table: str = config("SFC_API_DB_PERSISTENCE_TABLE", default="PERSISTENCE")
    db_settings_table: str = config("SFC_API_DB_PERSISTENCE_TABLE", default="SETTINGS")
