import logging
import sqlite3 as sl

from simplefancontroller.settings import SFCAPIConfig
from simplefancontroller.api.schemas import User

logger = logging.getLogger(__name__)

USER_TABLE = SFCAPIConfig.db_user_table
FANS_TABLE = SFCAPIConfig.db_fan_table
PERSISTENCE_TABLE = SFCAPIConfig.db_persistence_table


# todo: implement
def hash_password(pwd: str) -> str:
    return pwd


def check_password(pwd: str, pwd_hash: str) -> bool:
    return hash_password(pwd) == pwd_hash


class SFCUserManager:
    def __init__(self):
        self.con = sl.connect(SFCAPIConfig.db_user_file)
        if not self._check_tables_exist(USER_TABLE):
            self._create_user_table()

    def shutdown(self):
        self.con.close()

    def _create_user_table(self):
        with self.con:
            self.con.execute(
                f"""
                CREATE TABLE {USER_TABLE} (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    email TEXT,
                    password TEXT
                );
            """
            )

    def update_user(self, prev_mail: str, user: User):
        self.delete_user(prev_mail)
        self.add_user(user)

    def get_user_by_mail(self, email: str):
        with self.con:
            user = self.con.execute(
                f"SELECT * FROM {USER_TABLE} where email = ?", (email,)
            ).fetchone()
        if user:
            return User(name=user[1], email=user[2], password=user[3])
        raise ValueError(f"No user with email {email} found.")

    def add_user(self, user: User):
        try:
            found = self.get_user_by_mail(user.email)
        except:
            found = None
        if found:
            raise ValueError(f"A user with the email {user.email} already exists.")
        with self.con:
            self.con.execute(
                f"INSERT INTO {USER_TABLE} (name, email, password)" "VALUES (?, ?, ?)",
                (user.name, user.email, hash_password(user.password)),
            )

    def delete_user(self, email: str):
        self.get_user_by_mail(email)
        with self.con:
            self.con.execute(f"DELETE FROM {USER_TABLE} where email=?", (email,))

    def get_users(self):
        with self.con:
            users = self.con.execute(f"SELECT * FROM {USER_TABLE}").fetchall()
        for user in users:
            yield User(name=user[1], email=user[2], password=user[3])

    def check_user_password(self, email: str, password: str) -> bool:
        user_entry = self.get_user_by_mail(email)
        return check_password(password, user_entry.password)

    def _check_tables_exist(self, table_name: str) -> bool:
        with self.con:
            data = self.con.execute(
                "SELECT name FROM sqlite_master WHERE type='table' AND name=?",
                (table_name,),
            )
        return bool(data.fetchone())


if __name__ == "__main__":
    email = "bla@mail.com"
    manager = SFCUserManager()
    user = User(name="tester", email=email, password="blabla")
    manager.add_user(user)
    print(list(manager.get_users()))
    print(manager.get_user_by_mail(email))
    manager.delete_user(email)
    print(list(manager.get_users()))
