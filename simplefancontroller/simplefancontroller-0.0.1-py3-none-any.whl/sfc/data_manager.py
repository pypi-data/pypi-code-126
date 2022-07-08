import logging
import sqlite3 as sl
import sys

from simplefancontroller.settings import SFCAPIConfig
from simplefancontroller.sfc.settings import (
    SFCFanSettings,
    SFCDBSettings,
    SFControllerSettings,
)

logger = logging.getLogger(__name__)

USER_TABLE = SFCAPIConfig.db_user_table
FANS_TABLE = SFCAPIConfig.db_fan_table
PERSISTENCE_TABLE = SFCAPIConfig.db_persistence_table
SETTINGS_TABLE = SFCAPIConfig.db_settings_table


class SFCDataManager:
    def __init__(self):
        self.con = sl.connect(SFCAPIConfig.db_data_file)
        if not self._check_tables_exist(FANS_TABLE):
            self._create_fan_table()
        if not self._check_tables_exist(PERSISTENCE_TABLE):
            self._create_persistence_table()
        if not self._check_tables_exist(SETTINGS_TABLE):
            self._create_settings_table()

    def shutdown(self):
        self.con.close()

    def _create_fan_table(self):
        with self.con:
            self.con.execute(
                f"""
                CREATE TABLE {FANS_TABLE} (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    type TEXT,
                    settings TEXT
                );
            """
            )

    def _create_persistence_table(self):
        with self.con:
            self.con.execute(
                f"""
                CREATE TABLE {PERSISTENCE_TABLE} (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    type TEXT,
                    settings TEXT
                );
            """
            )

    def _create_settings_table(self):
        with self.con:
            self.con.execute(
                f"""
                CREATE TABLE {SETTINGS_TABLE} (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    settings TEXT
                );
            """
            )

    def save_fan(self, settings: SFCFanSettings):
        data = settings.json()
        with self.con:
            if self.con.execute(
                f"SELECT * FROM {FANS_TABLE} where name = ?", (settings.name,)
            ).fetchone():
                self.con.execute(
                    f"""
                    UPDATE {FANS_TABLE}
                    SET settings = ?
                    WHERE name = ?
                """,
                    (data, settings.name),
                )
            else:
                self.con.execute(
                    f"""
                    INSERT INTO {FANS_TABLE} (name, type, settings)
                    VALUES (?, ?, ?)
                """,
                    (settings.name, settings.__class__.__name__, data),
                )

    def get_fan(self, fan_name: str) -> SFCFanSettings:
        with self.con:
            data = self.con.execute(
                f"SELECT * FROM {FANS_TABLE} where name = ?", (fan_name,)
            ).fetchone()
        if data:
            cls_name = data[2].split(".")[-1].replace("'>", "")
            cls = getattr(sys.modules["simplefancontroller"], cls_name)
            return cls.parse_raw(data[3])
        raise ValueError(f"Not fan with name {fan_name} found.")

    def delete_fan(self, fan_name: str):
        self.get_fan(fan_name)
        with self.con:
            self.con.execute(f"DELETE FROM {FANS_TABLE} where name=?", (fan_name,))

    def get_fan_names(self) -> list[str]:
        with self.con:
            data = self.con.execute(f"SELECT name FROM {FANS_TABLE}").fetchall()
        yield from map(lambda x: x[0], data)

    def get_fans(self) -> list[SFCFanSettings]:
        names = self.get_fan_names()
        with self.con:
            for name in names:
                yield self.get_fan(name)

    def save_persistence(self, settings: SFCDBSettings):
        data = settings.json()
        with self.con:
            if self.con.execute(
                f"SELECT * FROM {PERSISTENCE_TABLE} where name = ?", (settings.name,)
            ).fetchone():
                self.con.execute(
                    f"""
                    UPDATE {PERSISTENCE_TABLE}
                    SET settings = ?
                    WHERE name = ?
                """,
                    (data, settings.name),
                )
            else:
                self.con.execute(
                    f"""
                    INSERT INTO {PERSISTENCE_TABLE} (name, type, settings)
                    VALUES (?, ?, ?)
                """,
                    (settings.name, settings.__class__.__name__, data),
                )

    def get_persistence(self, db_name: str) -> SFCDBSettings:
        with self.con:
            data = self.con.execute(
                f"SELECT * FROM {PERSISTENCE_TABLE} where name = ?", (db_name,)
            ).fetchone()
        if data:
            cls_name = data[2].split(".")[-1].replace("'>", "")
            cls = getattr(sys.modules["simplefancontroller"], cls_name)
            return cls.parse_raw(data[3])
        raise ValueError(f"Not database client with name {db_name} found.")

    def delete_persistence(self, db_name: str):
        self.get_persistence(db_name)
        with self.con:
            self.con.execute(
                f"DELETE FROM {PERSISTENCE_TABLE} where name=?", (db_name,)
            )

    def get_persistence_names(self) -> list[str]:
        with self.con:
            data = self.con.execute(f"SELECT name FROM {PERSISTENCE_TABLE}").fetchall()
        yield from map(lambda x: x[0], data)

    def save_settings(self, settings: SFControllerSettings):
        data = settings.json()
        with self.con:
            if self.con.execute(f"SELECT * FROM {SETTINGS_TABLE}").fetchone():
                self.con.execute(
                    f"""
                    UPDATE {SETTINGS_TABLE}
                    SET settings = ?
                """,
                    (data,),
                )
            else:
                self.con.execute(
                    f"""
                    INSERT INTO {SETTINGS_TABLE} 
                    (settings)
                    VALUES (?)
                """,
                    (data,),
                )

    def get_settings(self) -> SFControllerSettings:
        with self.con:
            data = self.con.execute(f"SELECT * FROM {SETTINGS_TABLE}").fetchone()
        if data:
            return SFControllerSettings.parse_raw(data[1])
        raise ValueError("No settings found.")

    def delete_settings(self):
        self.get_settings()
        with self.con:
            self.con.execute(f"DELETE FROM {SETTINGS_TABLE}")

    def _check_tables_exist(self, table_name: str) -> bool:
        with self.con:
            data = self.con.execute(
                "SELECT name FROM sqlite_master WHERE type='table' AND name=?",
                (table_name,),
            )
        return bool(data.fetchone())
