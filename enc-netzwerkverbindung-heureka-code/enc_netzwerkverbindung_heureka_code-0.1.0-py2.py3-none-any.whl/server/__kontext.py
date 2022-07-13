from logging import Logger
from abc import ABC, abstractmethod


class ServerKontext(ABC):
    @abstractmethod
    def callback(self):
        pass

    @abstractmethod
    def get_server_logger(self) -> Logger:
        pass

    @abstractmethod
    def user_akzeptieren(self, user):
        pass

    @abstractmethod
    def get_test(self) -> dict:
        pass

    @property
    @abstractmethod
    def test_aktiv(self) -> bool:
        pass
    pass
