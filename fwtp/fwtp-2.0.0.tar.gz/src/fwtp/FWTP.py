from __future__ import annotations
from psycopg2 import connect
from StringIteratorIO import StringIteratorIO
from typing import TypedDict, Optional, Iterator, List, Any
from logging import warning


class ConnDict(TypedDict):
    host: str
    database: str
    username: str
    password: str
    port: Optional[str]


class FWTP:

    def __init__(self, connection_dict: ConnDict, show_speed: Optional[bool]) -> None:
        self._conn_dict = connection_dict
        self._show_speed = show_speed

    def __enter__(self):
        self._connection = connect(**self._conn_dict)
        self._connection.autocommit = True
        self._cursor = self._connection.cursor
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self._connection.close()
        self._cursor.close()

    def _clean_csv_value(self, value: Any) -> str:
        if value is None or value == '':
            warning('A value was found to be None or empty. This can cause issue in writing to the database.')
            return r'\N'
        return str(value).replace('\n', '\\n')

    def write_to_db(self, rows: Iterator | List, columns: List[str], schema: str, table: str) -> None:
        csv_file_like_object_iterator = StringIteratorIO((
            ';'.join(
                [self._clean_csv_value(v) for v in row.values()]
            ) + '\n'
            for row in rows
        ))

        self._cursor.copy_expert(f"""COPY {schema}.{table} ({','.join(columns)})FROM STDIN DELIMITER ';' """,
                                 csv_file_like_object_iterator)
