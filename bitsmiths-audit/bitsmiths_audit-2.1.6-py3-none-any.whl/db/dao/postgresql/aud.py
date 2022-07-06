# This file was generated by mettle.genes.db.GenPy3 [ver 2.1] on Wed Jul  6 10:16:56 2022
#  Target Database = postgresql
#
import asyncio
import datetime
import uuid
import time
import mettle.lib
import mettle.io
import mettle.db

from bs_audit.db.tables.aud import tAud
from bs_audit.db.tables.aud_key import tAudKey

from .aud_select_one import dAudSelectOne
from .aud_insert import dAudInsert

class dAud:

    def __init__(self, dbcon: mettle.db.IConnect):
        """
        Constructor.

        :param dbcon: Mettle database connection object.
        """
        self.rec    = tAud()
        self._dbcon = dbcon

    def __enter__(self):
        """
        DAO enter.
        """
        return self

    def __exit__(self, type, value, traceback):
        """
        DAO exit.
        """
        pass

    def try_select_one(self) -> bool:
        """
        Attempt to select the record.

        :return: True if the record was found.
        """
        _key = tAudKey()

        self.rec._write_key(_key)

        return self.try_select_one_by_key(_key)

    def try_select_one_with(self, _rec: tAud) -> bool:
        """
        Attempt to select the record using a table rec.

        :param _rec: The table rec to select with and into.
        :return: True if the row as selectd.
        """
        _key = tAudKey()
        _rec._write_key(_key)

        if not self.try_select_one_by_key(_key):
            return False

        _rec._copy_from(self.rec)

        return True

    def try_select_one_deft(self,
                            id: int) -> bool:
        """
        Attempt to select the record by it's primary key columns.

        :param id: int
        :return: True if the row as selectd.
        """
        _key = tAudKey()

        _key.id = id

        return self.try_select_one_by_key(_key)

    def try_select_one_by_key(self, _key: tAudKey) -> bool:
        """
        Attempt to select the record with it's primary key.

        :param _key: Primary key of the table record.
        :returns: True if row was selected.
        """
        with dAudSelectOne(self._dbcon) as _qry:
            _qry.exec(_key)
            if not _qry.fetch():
                return False

            self.rec = _qry.orec

        return True

    def select_one(self) -> "dAud":
        """
        Selects the record, raises and error if it does not exist.

        :return: Self for convenience.
        """
        if not self.try_select_one():
            raise mettle.lib.xMettle("SelectOne failed to return a record (dAud)")

        return self

    def select_one_with(self, _rec: tAud) -> "dAud":
        """
        Attempt to select the record with the table record.

        :param _rec: Table record.
        :returns: Self for convenience.
        """
        if not self.try_select_one_with(_rec):
            raise mettle.lib.xMettle("SelectOne failed to return a record (dAud)")

        return self

    def select_one_deft(self,
                        id: int) -> "dAud":
        """
        Selects the record by its primary key columns, raises and error if it does not exist.

        :param id: int
        """
        _key = tAudKey()

        _key.id = id

        if not self.try_select_one_by_key(_key):
            raise mettle.lib.xMettle("SelectOne failed to return a record (dAud)")

        return self

    def select_one_by_key(self, _key: tAudKey) -> "dAud":
        """
        Attempt to select the record with it's primary key.

        :param _key: Primary key of the table record.
        :return: Self for convenience.
        """
        if not self.try_select_one_by_key(_key):
            raise mettle.lib.xMettle("SelectOne failed to return a record (dAud)")

        return self

    def insert_deft(self,
                    tran_id: int,
                    action: str,
                    tbl_id: str,
                    tbl_key: str):
        """
        Insert the record setting all column values.

        :param id: int
        :param tran_id: int
        :param action: str
        :param tbl_id: str
        :param tbl_key: str
        """
        self.rec.tran_id = tran_id
        self.rec.action = action
        self.rec.tbl_id = tbl_id
        self.rec.tbl_key = tbl_key

        self.insert()

    def insert(self, irec: tAud = None):
        """
        Insert the record in the database with the record or irec if it is not None.

        :param irec: If not None use this record to insert into the database.
        """
        if irec:
            self.rec._copy_from(irec)

        with dAudInsert(self._dbcon) as _qry:
            _qry.exec(self.rec)

        if irec:
            irec._copy_from(self.rec)

