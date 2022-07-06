# This file was generated by mettle.genes.db.GenPy3 [ver 2.1] on Wed Jul  6 10:16:56 2022
#  Target Database = postgresql
#
import datetime
import uuid
import time
import mettle.lib
import mettle.io
import mettle.db

from bs_audit.db.tables.cfg import tCfg

class dCfgInsert:

    def __init__(self, dbcon: mettle.db.IConnect):
        """
        Constructor.

        :param dbcon: Mettle database connection object.
        """
        self._dbcon   = dbcon
        self._dbstmnt = None
        self.irec     = tCfg()
    def __enter__(self):
        """
        With statement enter.
        """
        return self

    def __exit__(self, type, value, traceback):
        """
        With statement exit.
        """
        self._destroy()

    def _destroy(self):
        self._dbstmnt = None

    def exec_deft(self,
                  id: str,
                  col_pk: str,
                  col_ignr: str,
                  par_id: str,
                  par_col: str,
                  last_chg: datetime.datetime,
                  audby_col: str,
                  mode: str) -> "dCfgInsert":
        """
        Execute the query by setting all the inputs.

        :param id: str
        :param col_pk: str
        :param col_ignr: str
        :param par_id: str
        :param par_col: str
        :param last_chg: datetime.datetime
        :param audby_col: str
        :param mode: str
        :return: Self for convenience.
        """
        self.irec.id = id
        self.irec.col_pk = col_pk
        self.irec.col_ignr = col_ignr
        self.irec.par_id = par_id
        self.irec.par_col = par_col
        self.irec.last_chg = last_chg
        self.irec.audby_col = audby_col
        self.irec.mode = mode

        return self.exec()

    def exec(self, irec: tCfg = None) -> "dCfgInsert":
        """
        Execute the query, optionally passing in the input rec.

        :param irec:
        :return: Self for convenience.
        """
        if irec:
            self.irec._copy_from(irec)

        self._destroy()

        self._dbstmnt = self._dbcon.statement("CfgInsert", self._dbcon.STMNT_TYPE_CUD)

        self._dbstmnt.sql("""insert into audit.Cfg (
  id,
  col_pk,
  col_ignr,
  par_id,
  par_col,
  last_chg,
  audby_col,
  mode
) values (
  :id,
  :col_pk,
  :col_ignr,
  :par_id,
  :par_col,
  :last_chg,
  :audby_col,
  :mode
)""")

        self._dbstmnt.bind_in("id", self.irec.id, str)
        self._dbstmnt.bind_in("col_pk", self.irec.col_pk, str)
        self._dbstmnt.bind_in("col_ignr", self.irec.col_ignr, str)
        self._dbstmnt.bind_in("par_id", self.irec.par_id, str)
        self._dbstmnt.bind_in("par_col", self.irec.par_col, str)
        self._dbstmnt.bind_in("last_chg", self.irec.last_chg, datetime.datetime)
        self._dbstmnt.bind_in("audby_col", self.irec.audby_col, str)
        self._dbstmnt.bind_in("mode", self.irec.mode, str, 1)

        self._dbcon.execute(self._dbstmnt)

        if irec:
            irec._copy_from(self.irec)

        return self

