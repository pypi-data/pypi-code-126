from abc import ABC, abstractmethod


class BasisCOM(ABC):
    """ Basisklasse fuer eine Netzwerkverbindung """
    @abstractmethod
    def send(self, data: bytes):
        """
        Sendet eine Nachricht

        :param data: Die zu sendende Nachricht
        """
        pass

    @abstractmethod
    def receive(self) -> bytes:
        """ Empfaengt eine Nachricht und liefert diese zurueck """
        pass
