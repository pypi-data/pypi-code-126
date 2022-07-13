# -*- coding: utf-8 -*-
from __future__ import annotations

import ctypes
import logging
import select
from collections import deque
from csv import Sniffer
from multiprocessing import Pipe
from threading import Thread
from typing import Optional

from .buffer_processor import MAGIC_BYTE_SEQUENCE, BufferProcessor
from .connection import NonBlockConnection
from .helpers import LazyOpener, catch_exceptions
from .types import FilePathType, Openable, Readable

CHUNK_SIZE = 32 * 1024
ENCODING_PREFIX_LENGTH = 16
CSV_SAMPLE_SIZE = 512 * 1024  # 512 kb sample size


class DetectingBuffer(Readable):
    # pylint: disable=too-many-instance-attributes
    def seek(self, __offset: int, __whence: int = ...) -> int:
        raise NotImplementedError

    def __init__(
        self,
        file: Readable | Openable | FilePathType,
        newline=None,
        **kwargs,
    ) -> None:
        super().__init__()

        self._newline = newline
        kwargs["mode"] = "rb"
        self._opener = LazyOpener(file, **kwargs)
        self._open_file = self._opener.open()
        self._in_read, self._in_write = Pipe(duplex=False)
        self._out_read, self._out_write = Pipe(duplex=False)
        self._reader = ReaderThread(
            self._open_file,
            NonBlockConnection.convert_connnection(self._in_write),
            kwargs.get("chunk_size", CHUNK_SIZE),
        )

        self._processor = BufferProcessor(
            in_reader=self._in_read,
            out_writer=NonBlockConnection.convert_connnection(self._out_write),
        )
        self._reader.start()
        self._processor.start()
        self._buffer: deque = deque()
        self._done = False
        self._leftovers = ""
        self._closed = False

        self._log = logging.getLogger(__name__).getChild(self.__class__.__name__)

    # noinspection PyMethodMayBeStatic
    def seekable(self) -> bool:
        return False

    def _fetch_chunk(self):
        if self._done:
            return ""
        try:
            chunk = self._out_read.recv()
            # self._log.debug("Received chunk: %s (%s bytes)", type(chunk), len(chunk))
        except EOFError:
            self._done_reading()
            return ""
        if chunk == MAGIC_BYTE_SEQUENCE:
            self._done_reading()
            return ""
        if self._newline is None:
            chunk = chunk.replace("\r\n", "\n")
            chunk = chunk.replace("\r", "\n")
        return chunk

    def _done_reading(self):
        if self._closed:
            return
        self._reader.stop()
        self._processor.stop()
        catch_exceptions(self._out_read.close, [OSError])()
        catch_exceptions(self._out_write.close, [OSError])()
        catch_exceptions(self._in_read.close, [OSError])()
        catch_exceptions(self._in_write.close, [OSError])()
        self._reader.join()
        self._processor.join()
        self._log.debug("Joined all thread/processes")
        self._done = True
        self._opener.close()
        self._closed = True

    def __del__(self):
        self._done_reading()

    def peek(self, size: int | None = None) -> str:
        out = self.read(size)
        self._leftovers = out + self._leftovers
        return out

    def read(self, size: int | None = None) -> str:
        self._log.debug(
            "Trying to read %s bytes (already have %s bytes)", size, len(self._leftovers)
        )
        output = ""
        size = size or -1
        if size < 0:
            if self._leftovers:
                output += self._leftovers
                self._leftovers = ""
            while chunk := self._fetch_chunk():
                output += chunk
            return output
        while size > 0:
            if self._leftovers:
                # self._log.debug("%s: Using leftovers: %s", threading.currentThread(), len(self._leftovers))
                nc = self._leftovers[:size]
                self._leftovers = self._leftovers[size:]
                # self._log.debug("%s: Leftovers: %s", threading.currentThread(), len(self._leftovers))
                output += nc
                size -= len(nc)
                continue
            chunk = self._fetch_chunk()
            if chunk == "":
                break
            if len(chunk) > size:
                self._leftovers = chunk[size:]
                output += chunk[:size]
                break

            output += chunk
            size -= len(chunk)
        # self._log.debug("Read %s bytes", len(output))
        return output

    def readline(self):
        str_buf = self.read(1024)
        if self._newline is None:
            nl = "\n"
        else:
            nl = self._newline
        while nl not in str_buf:
            r = self.read(1024)
            str_buf += r
            if r == "":
                break
        if nl in str_buf:
            ret = str_buf[: str_buf.index(nl) + 1]
            self._leftovers = str_buf[len(ret) :] + self._leftovers
        else:
            ret = str_buf
        return ret

    def __next__(self):
        r = self.readline()
        if r == "":
            raise StopIteration
        return r

    def __iter__(self):
        return self

    def get_csv_dialect(
        self,
        sniffer: Optional[Sniffer] = None,
        delimiters: Optional[str] = None,
        sample_size=CSV_SAMPLE_SIZE,
    ):
        sniffer = sniffer or Sniffer()
        buffer = self.read(sample_size)
        dialect = sniffer.sniff(buffer, delimiters=delimiters)
        self._leftovers = buffer + self._leftovers
        return dialect


class StopThread(BaseException):
    pass


def pipe_full(conn, timeout=0.0):
    _, w, _ = select.select([], [conn], [], timeout)
    return 0 == len(w)


class ReaderThread(Thread):
    def __init__(self, file: Readable, in_writer: NonBlockConnection, chunk_size=CHUNK_SIZE):
        super().__init__()
        self._file = file
        self._in_writer = in_writer
        self._chunk_size = chunk_size
        self._log = (
            logging.getLogger(__name__).getChild(self.__class__.__name__).getChild(self.name)
        )

        # self._log.debug(os.get_blocking(self._in_writer.fileno()))
        # os.set_blocking(self._in_writer.fileno(), False)
        # self._log.debug(os.get_blocking(self._in_writer.fileno()))

    def _reader(self):
        while chunk := self._file.read(self._chunk_size):
            self._log.info(pipe_full(self._in_writer))
            self._in_writer.send_bytes(chunk)
            # self._log.debug("Sent %s bytes", len(chunk))
        # self._in_write_wrap.send_bytes_polled(MAGIC_BYTE_SEQUENCE)
        self._in_writer.send_bytes(chunk)
        self._log.debug("Sent magic byte sequence")
        self._in_writer.close()
        self._log.debug("Closed input")

    def run(self):
        try:
            self._reader()
        except StopThread:
            self._log.debug("stopped")
        except Exception as e:  # pylint: disable=broad-except
            self._log.exception(e)

        finally:
            self._log.debug("exiting")

    def stop(self):
        thread_id = self.ident
        self._log.debug("Raising exception for thread %s", thread_id)
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(
            ctypes.c_long(thread_id), ctypes.py_object(SystemExit)
        )
        self._log.debug("Raised exception for thread %s: %s", thread_id, res)
        if res > 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(thread_id), 0)
            raise SystemError("PyThreadState_SetAsyncExc failed")
