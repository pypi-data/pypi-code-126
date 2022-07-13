import socketserver
from logging import getLogger
from weakref import finalize

import enc_netzwerkverbindung_heureka_code.server.__kontext as s_kontext
from enc_netzwerkverbindung_heureka_code._generell import RSASchluessel, get_ip

from .__client_handler import BasisClientHandler
from .__uebergabe_sk_pk import uebergebe_sk_pk
from .verwaltung.rsa_verwalter import RSAVerwalter


class SocketServer:
    """ Verwaltet den Server """

    def __init__(self, host: str = "0.0.0.0", port: int = 3901):
        """
        Verwaltet den Server

        :param host: Der Host, auf den der Server geoeffnet werden soll
        :param port: Der zu verwendende Port
        """
        self._logger = getLogger(__name__)

        self._server_kontext: s_kontext.ServerKontext
        self.__abschluss = finalize(self, self.close)
        self.__geschlossen = False

        self.HOST, self.PORT = host, port
        self.secret_key, self.public_key = None, None

    def start(self, server_kontext: "s_kontext.ServerKontext"):
        """ Verwaltet den Serverprozess """
        self._server_kontext = server_kontext
        self._logger = self._server_kontext.get_server_logger(__name__)

        self._logger.debug("Server startet")
        self._logger.info(f"Server offen: {get_ip()}:{self.PORT}      ({self.HOST})")

        self.__server_starten()

    def close(self):
        """ Schliesst die Serververbindung """
        if not self.__geschlossen:
            if hasattr(self, "server"):
                self.server.server_close()
            self.__geschlossen = True
            self._logger.info("Server wurde geschlossen")

    def __server_starten(self):
        """ Startet die Serververbindung """
        with socketserver.TCPServer(
                (self.HOST, self.PORT),
                uebergebe_sk_pk(stream_klasse=self._server_kontext.client_handler, server_kontext=self._server_kontext)
        ) as self.server:
            self._logger.debug("Server wurde fertig gestartet")
            self.__geschlossen = False
            try:
                self.server.serve_forever()
            except KeyboardInterrupt:
                pass
