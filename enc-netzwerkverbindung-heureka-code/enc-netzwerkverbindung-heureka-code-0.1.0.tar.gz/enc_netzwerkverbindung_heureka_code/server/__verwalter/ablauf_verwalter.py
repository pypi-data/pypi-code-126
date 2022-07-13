from abc import ABC, abstractmethod


class Verbindungsablauf(ABC):
    def __init__(self, handler):
        self.handler = handler
        self.logger = handler._logger
    pass
