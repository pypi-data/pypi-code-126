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

from bs_audit.db.tables.tran import tTran
from bs_audit.db.tables.tran_key import tTranKey

from .tran_select_one import dTranSelectOne
from .tran_insert import dTranInsert

class dTran:

    def __init__(self, dbcon: mettle.db.IConnect):
        """
        Constructor.

        :param dbcon: Mettle database connection object.
        """
        self.rec    = tTran()
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
        _key = tTranKey()

        self.rec._write_key(_key)

        return self.try_select_one_by_key(_key)

    def try_select_one_with(self, _rec: tTran) -> bool:
        """
        Attempt to select the record using a table rec.

        :param _rec: The table rec to select with and into.
        :return: True if the row as selectd.
        """
        _key = tTranKey()
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
        _key = tTranKey()

        _key.id = id

        return self.try_select_one_by_key(_key)

    def try_select_one_by_key(self, _key: tTranKey) -> bool:
        """
        Attempt to select the record with it's primary key.

        :param _key: Primary key of the table record.
        :returns: True if row was selected.
        """
        with dTranSelectOne(self._dbcon) as _qry:
            _qry.exec(_key)
            if not _qry.fetch():
                return False

            self.rec = _qry.orec

        return True

    def select_one(self) -> "dTran":
        """
        Selects the record, raises and error if it does not exist.

        :return: Self for convenience.
        """
        if not self.try_select_one():
            raise mettle.lib.xMettle("SelectOne failed to return a record (dTran)")

        return self

    def select_one_with(self, _rec: tTran) -> "dTran":
        """
        Attempt to select the record with the table record.

        :param _rec: Table record.
        :returns: Self for convenience.
        """
        if not self.try_select_one_with(_rec):
            raise mettle.lib.xMettle("SelectOne failed to return a record (dTran)")

        return self

    def select_one_deft(self,
                        id: int) -> "dTran":
        """
        Selects the record by its primary key columns, raises and error if it does not exist.

        :param id: int
        """
        _key = tTranKey()

        _key.id = id

        if not self.try_select_one_by_key(_key):
            raise mettle.lib.xMettle("SelectOne failed to return a record (dTran)")

        return self

    def select_one_by_key(self, _key: tTranKey) -> "dTran":
        """
        Attempt to select the record with it's primary key.

        :param _key: Primary key of the table record.
        :return: Self for convenience.
        """
        if not self.try_select_one_by_key(_key):
            raise mettle.lib.xMettle("SelectOne failed to return a record (dTran)")

        return self

    def insert_deft(self,
                    site_id: int,
                    who: str,
                    src: str):
        """
        Insert the record setting all column values.

        :param id: int
        :param site_id: int
        :param who: str
        :param src: str
        :param tm_stamp: datetime.datetime
        """
        self.rec.site_id = site_id
        self.rec.who = who
        self.rec.src = src

        self.insert()

    def insert(self, irec: tTran = None):
        """
        Insert the record in the database with the record or irec if it is not None.

        :param irec: If not None use this record to insert into the database.
        """
        if irec:
            self.rec._copy_from(irec)

        with dTranInsert(self._dbcon) as _qry:
            _qry.exec(self.rec)

        if irec:
            irec._copy_from(self.rec)

