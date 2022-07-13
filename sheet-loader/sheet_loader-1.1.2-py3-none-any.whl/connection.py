# -*- coding: utf-8 -*-
from __future__ import annotations

import os
from multiprocessing.connection import Connection


class NonBlockConnection(Connection):
    def _close(self, _close=os.close):
        _close(self._handle)

    _write = os.write
    _read = os.read

    def _send(self, buf, write=_write):
        remaining = len(buf)
        while True:
            try:
                n = write(self._handle, buf)
            except BlockingIOError:
                continue
            remaining -= n
            if remaining == 0:
                break
            buf = buf[n:]

    @classmethod
    def convert_connnection(cls, conn: Connection):
        conn.__class__ = cls
        os.set_blocking(conn.fileno(), False)
        return conn
