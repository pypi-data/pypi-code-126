from fiopy.http.rate_limit import RateLimit


class RateLimitedException(Exception):
    def __init__(self, message: str = None, rate_limit: RateLimit = None):
        super().__init__(message)
        self._rate_limit = rate_limit

    def __str__(self):
        return f"Rate-limited. {self.remaining} requests (out of {self.value} requests) remaining against {self.window} ms."

    @property
    def value(self):
        return self._rate_limit.value

    @property
    def remaining(self):
        return self._rate_limit.remaining

    def window(self):
        return self._rate_limit.window
