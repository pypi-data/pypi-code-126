from queue import Queue


class SourceBase:
    __source_name = ''

    def __init__(self) -> None:
        pass

    def get_price(self, queue: Queue) -> None:
        raise NotImplementedError
