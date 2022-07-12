import io
import html
import logging
import os
import os.path
import subprocess
import traceback
import threading
from lxcommon import LxParagraph, CintilFormatSpec, normalize_unicode, normalize_text


LOG = logging.getLogger(__name__)

CHUNKER_COPYRIGHT_NOTICE = {
    "LX-Chunker: part of the LX-Suite of tools",
    "(c) 2002 A. Branco and J. Silva",
}


class Feeder(threading.Thread):
    "thread to feed the chunker process"

    def __init__(self, lines, proc_stdin):
        super().__init__()
        self.lines = lines
        self.proc_stdin = proc_stdin

    def run(self):
        for line in self.lines:
            line = line.strip()
            line = normalize_unicode(line)
            line = normalize_text(line)
            line = html.escape(line)
            print(line, file=self.proc_stdin)
        self.proc_stdin.close()


class ErrorLogger(threading.Thread):
    "thread to log errors from the chunker process"

    def __init__(self, chunker_basename, proc_stderr):
        super().__init__()
        self.chunker_basename = chunker_basename
        self.proc_stderr = proc_stderr

    def run(self):
        for line in map(str.strip, self.proc_stderr):
            if line not in CHUNKER_COPYRIGHT_NOTICE:
                LOG.warning(f"{self.chunker_basename} STDERR >> {line}")


class LxSentenceSplitter:
    CHUNKER_ENCODING = "cp1252"
    CHUNKER_DIR = os.path.join(os.path.dirname(__file__), "chunker")
    CHUNKER_ONE_BIN = os.path.join(CHUNKER_DIR, "chunker-one")
    CHUNKER_TWO_BIN = os.path.join(CHUNKER_DIR, "chunker-two")

    def __init__(self, paragraphs_separated_by_empty_line=True):
        self.paragraphs_separated_by_empty_line = paragraphs_separated_by_empty_line
        if self.paragraphs_separated_by_empty_line:
            self.chunker = LxSentenceSplitter.CHUNKER_TWO_BIN
        else:
            self.chunker = LxSentenceSplitter.CHUNKER_ONE_BIN
        self.chunker_basename = os.path.basename(self.chunker)

    def __del__(self):
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass

    def isplit(self, lines):
        proc = None
        try:
            proc = subprocess.Popen(
                [self.chunker],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            LOG.debug(f"{self.chunker_basename} << <iterable>")
            LOG.debug(f"{self.chunker_basename} >> <generator>")

            cintil_format = CintilFormatSpec(tokenized=False)
            proc_stdin = io.TextIOWrapper(
                proc.stdin,
                encoding=LxSentenceSplitter.CHUNKER_ENCODING,
                errors="replace",
            )
            proc_stdout = io.TextIOWrapper(
                proc.stdout,
                encoding=LxSentenceSplitter.CHUNKER_ENCODING,
                errors="replace",
            )
            proc_stderr = io.TextIOWrapper(
                proc.stderr,
                encoding=LxSentenceSplitter.CHUNKER_ENCODING,
                errors="replace",
            )
            with proc_stdin, proc_stdout, proc_stderr:
                feeder = Feeder(lines, proc_stdin)
                feeder.start()
                errorlogger = ErrorLogger(self.chunker_basename, proc_stderr)
                errorlogger.start()
                yield from LxParagraph.read_cintil_paragraphs(
                    map(html.unescape, proc_stdout), cintil_format
                )
                feeder.join()
                errorlogger.join()
            proc.wait()
        except Exception:  # pragma: no cover
            traceback.print_exc()
            if proc is not None:
                proc.kill()
            raise

    def split(self, document):
        if not isinstance(document, str):
            raise TypeError("document must be a string")
        document = html.escape(normalize_unicode(document))
        if not document.strip():
            return []
        proc = None
        try:
            proc = subprocess.Popen(
                [self.chunker],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            # we split lines and join them again to normalize line endings
            input_lines = document.splitlines(keepends=False)
            if LOG.isEnabledFor(logging.DEBUG):  # pragma: no cover
                for line in input_lines:
                    LOG.debug(f"{self.chunker_basename} << {line}")
            stdin = "\n".join(input_lines).encode(
                LxSentenceSplitter.CHUNKER_ENCODING, errors="replace"
            )
            stdout, stderr = proc.communicate(input=stdin)
            stdout_text = stdout.decode(LxSentenceSplitter.CHUNKER_ENCODING)
            stderr_text = stderr.decode(LxSentenceSplitter.CHUNKER_ENCODING)
            output_lines = html.unescape(stdout_text).splitlines(keepends=False)
            error_lines = stderr_text.splitlines(keepends=False)
            if LOG.isEnabledFor(logging.DEBUG):  # pragma: no cover
                for line in output_lines:
                    LOG.debug(f"{self.chunker_basename} >> {line}")
            for line in error_lines:
                if line not in CHUNKER_COPYRIGHT_NOTICE:
                    LOG.warning(f"{self.chunker_basename} STDERR >> {line}")
            return LxParagraph.read_cintil_paragraphs(
                output_lines, CintilFormatSpec(tokenized=False)
            )
        except Exception:  # pragma: no cover
            traceback.print_exc()
            if proc is not None:
                proc.kill()
            raise


def _check_chunker_runs():
    chunkers = [LxSentenceSplitter.CHUNKER_ONE_BIN, LxSentenceSplitter.CHUNKER_TWO_BIN]
    for chunker in chunkers:
        try:
            subprocess.check_call(
                [chunker],
                stdin=subprocess.DEVNULL,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
        except Exception:
            message = (
                f"could not run {chunker}, which is a 32-bit "
                "executable; if this is a Debian-based system, ensure you have "
                "installed the libc6-i386 package"
            )
            LOG.exception(message)
            raise Exception(message)


_check_chunker_runs()
