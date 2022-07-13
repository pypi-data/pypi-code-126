from logging import getLogger
from enc_netzwerkverbindung_heureka_code.__generell import get_ip
from .__client_handler import ClientHandler
from .__uebergabe_sk_pk import uebergebe_sk_pk


class StdSocketServer:
    """ Verwaltet den Server """

    def __init__(self, host: str = "0.0.0.0", port: int = 3901):
        """
        Verwaltet den Server

        :param host: Der Host, auf den der Server geoeffnet werden soll
        :param port: Der zu verwendende Port
        :param logger: Der zu verwendende Logger
        """
        self._logger = getLogger(__name__)

        self._server_kontext: ServerKontext
        self.__abschluss = finalize(self, self.close)
        self.__geschlossen = False

        self.HOST, self.PORT = host, port
        self.secret_key, self.public_key = None, None

    def start(self, server_kontext: "ServerKontext"):
        """ Verwaltet den Serverprozess """
        self._server_kontext = server_kontext
        self._logger = self._server_kontext.get_server_logger()

        self._logger.debug("Server startet")
        self._logger.info(f"Server offen: {self.get_ip()}:{self.PORT}      ({self.HOST})")

        self.__schluessel_generieren()
        self.__server_starten()

    def __server_starten(self):
        with socketserver.TCPServer(
                (self.HOST, self.PORT),
                uebergebe_sk_pk(pk=self.public_key, sk=self.secret_key,
                                stream_klasse=ClientHandler, server_kontext=self._server_kontext)
        ) as self.server:
            self._logger.debug("Server wurde fertig gestartet")
            self.server.serve_forever()

    def __schluessel_generieren(self):
        with LoggingKontext(self._logger, "Schluesselgenerierung", level_enter=logging.DEBUG, level_exit=logging.DEBUG):
            self.secret_key = ServerRSA.generate_sk()
            self.public_key = ServerRSA.calc_pk(self.secret_key)
            self._logger.info(f"Schluesselfussabdruck ist {ServerRSA.calc_footprint(self.public_key)}")

    def close(self):
        """ Schliesst die Serververbindung """
        if not self.__geschlossen:
            if hasattr(self, "server"):
                self.server.server_close()
            self.__geschlossen = True
            self._logger.info("Server wurde geschlossen")

    @property
    def fingerabdruck(self) -> str:
        """ Berechnet den Fingerabdruck des Servers """
        while not self.schluessel_erstellt:
            pass
        return ServerRSA.calc_footprint(self.public_key)

    @property
    def schluessel_erstellt(self) -> bool:
        """ Prueft, ob die Schluesselgenerierung abgeschlossen ist """
        return self.public_key is not None
    pass
