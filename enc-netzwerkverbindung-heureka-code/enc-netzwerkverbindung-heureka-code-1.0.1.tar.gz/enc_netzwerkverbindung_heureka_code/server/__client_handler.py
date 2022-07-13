import socketserver
from abc import ABC, abstractmethod
from typing import final

from enc_netzwerkverbindung_heureka_code._generell.verbindung import \
    ServerVerbindungsVerwalter
from enc_netzwerkverbindung_heureka_code.server.__kontext import ServerKontext

from .verwaltung.crypto_verwalter import CryptoVerwalter


class BasisClientHandler(socketserver.StreamRequestHandler, ABC):
    """ Handler fuer die Verbindung zu einem Client """

    def __init__(self, server_kontext: ServerKontext, *args, **kwargs):
        """
        Handler fuer die Verbindung zu einem Client

        :param server_kontext: Der Kontext des Servers
        """
        self.server_kontext: ServerKontext = server_kontext

        super(BasisClientHandler, self).__init__(*args, **kwargs)

    def __setup(self):
        """ Initialisiert die Verbindung """
        self._logger = self.server_kontext.get_client_logger(self.client_address[0])
        self.verbindung = CryptoVerwalter(
            ServerVerbindungsVerwalter(self.wfile, self.rfile),
            rsa=self.server_kontext.get_rsa()
        )

        self._logger.debug(f" Neuer Client will sich verbinden: {self.client_address[0]} ".center(100, "="))

        self._logger.debug("Verbindungsaufbau begonnen")
        self.verbindung._setup()
        if self.verbindung.aes_key is None:
            return False
        self._logger.debug("Verbindungsaufbau abgeschlossen")
        return True

    @abstractmethod
    def verbindung_verwalten(self):
        """ Abstrakte Methode zur eigentlichen Verbindungsverwaltung """
        pass

    @final
    def handle(self) -> None:
        """
        Startet die Verbindung, falls moeglich

        Wenn es aufgrund von z.B. einem Verschluesselungsfehler nicht moeglich ist, eine Verbindung aufzubauen,
        wird die Verbindung abgebrochen.
        """
        if not self.__setup():
            return
        self.verbindung_verwalten()
    pass
