from typing import Iterator, Optional
import io


class StringIteratorIO(io.TextIOBase):
    def __init__(self, iter: Iterator[str]):
        self._iter = iter
        self._buff = ''

    def readable(self) -> bool:
        return True

    def _private_read(self, limit: Optional[int] = None) -> str:

        while not self._buff:
            try:
                self._buff = next(self._iter)
            except Exception as e:
                break

        line = self._buff[:limit]
        self._buff = self._buff[len(line):]

        return line

    def read(self, size: Optional[int] = None) -> str:
        lines = []

        if size is None or size < 0:
            while True:
                line = self._private_read()
                if not line:
                    break
                lines.append(line)
        else:
            while size > 0:
                line = self._private_read(size)
                if not line:
                    break
                size -= len(line)

                lines.append(line)

        return ''.join(lines)
