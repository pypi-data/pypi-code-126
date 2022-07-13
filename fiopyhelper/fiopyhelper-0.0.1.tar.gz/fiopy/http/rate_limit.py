class RateLimit:
    def __init__(self, *, value=0, remaining=0, window=0):
        self._value = value
        self._remaining = remaining
        self._window = window

    @property
    def value(self):
        return self._value

    @property
    def remaining(self):
        return self._remaining

    @property
    def window(self):
        return self._window
