# -*- coding: utf-8 -*-
from __future__ import annotations

import logging
import signal
from abc import ABC, abstractmethod
from collections import deque
from multiprocessing import Process
from multiprocessing.connection import Connection
from timeit import default_timer as timer

from chardet import UniversalDetector

from .helpers import catch_exceptions


class KillableProcess(ABC, Process):
    def __init__(self, *args, **kwargs):
        super().__init__(name=self.__class__.__name__, daemon=True, *args, **kwargs)
        self._log = (
            logging.getLogger(__name__).getChild(self.__class__.__name__).getChild(self.name)
        )

    def stop(self):
        try:
            self._popen._send_signal(signal.SIGINT)  # pylint: disable=protected-access
        except AttributeError:
            self.terminate()

    def terminate(self):
        try:
            super().terminate()
        except AttributeError:
            pass

    @abstractmethod
    def _stop(self):
        pass

    def _handle_sigint(self, signum, frame):  # pylint: disable=unused-argument
        self._log.debug("SIGINT received")
        self._stop()
        self.terminate()

    def run(self):
        signal.signal(signal.SIGINT, self._handle_sigint)


class BufferProcessor(KillableProcess):
    def __init__(self, in_reader: Connection, out_writer: Connection):
        super().__init__()
        self._in_reader = in_reader
        self._out_writer = out_writer
        self._total_bytes = 0
        self._detector = UniversalDetector()
        self.current_enc = DEFAULT_START_ENCODING
        self.last_encodings: deque = deque(maxlen=3)
        self.result = None
        self._stop_feeding = False

    def feed_detector(self, chunk):
        self._detector.feed(chunk)

        self.result = self.get_best_encoding()
        if self.result["encoding"] is not None:
            self.last_encodings.append(self.current_enc)
            self.current_enc = self.result["encoding"]
            if set(self.last_encodings) == {self.current_enc}:
                self._stop_feeding = True
        return self._send(chunk.decode(self.current_enc))

    def get_best_encoding(self):
        dd = self._detector.done
        result = self._detector.close()
        self._detector.done = dd
        return result

    def feed_and_process(self, chunk):
        try:
            return self._feed_and_process(chunk)
        except TypeError as e:
            self._log.exception(e)
        return False

    def _feed_and_process(self, chunk):
        # self._log.debug("%s %s %s", pipe_full(self._out_writer), self._out_writer.closed, self._in_reader.closed)
        if self._stop_feeding or self._detector.done or self._total_bytes > MAX_DETECTION_SIZE:
            # no more detection needed (at least for now)
            self._log.debug("Not feeding")
            try:
                return self._send(chunk.decode(self.current_enc))
            except UnicodeError:
                self._log.debug(
                    'Could not decode chunk with encoding "%s", re-feeding', self.current_enc
                )
                return self.feed_detector(chunk)
        else:
            self._log.debug("Feeding")
            return self.feed_detector(chunk)

    def _stop(self):
        self._close_in()
        start = timer()
        while timer() - start < 1:
            if self.is_alive():
                continue
            break
        self._close_out()

    def run(self):
        super().run()
        chunk = b""
        while True:
            try:
                nc = self._in_reader.recv_bytes()
                # self._log.debug("Received %s bytes", len(nc))
            except (EOFError, OSError):
                nc = b""
            if nc == MAGIC_BYTE_SEQUENCE:
                nc = b""
            chunk += nc

            if chunk == b"":
                # empty chunk means we're done
                break
            if nc and (nc[-1] > 0x7F or nc[-1] in (ord("\n"), ord("\r"))):
                # last byte is not ascii, or last byte is some type of line ending,
                # let's get some more, so we don't split a character
                continue
            if not self.feed_and_process(chunk):
                break
            self._total_bytes += len(chunk)
            chunk = b""
            if nc == b"":
                # empty next chunk means done
                break
        self._send(MAGIC_BYTE_SEQUENCE)
        self._close()

    def _send(self, chunk):
        try:
            self._out_writer.send(chunk)
            return True
        except OSError:
            return False

    def _close_in(self):
        catch_exceptions(self._in_reader.close, [OSError])()

    def _close_out(self):
        catch_exceptions(self._out_writer.close, [OSError])()

    def _close(self):
        self._close_in()
        self._close_out()


MAGIC_BYTE_SEQUENCE = b"\xde\xca\xf0\xde\xad\xbe\xef"
MAX_DETECTION_SIZE = 1 * 1024 * 1024  # 1MB max detection size
DEFAULT_START_ENCODING = "utf-8"
