import datetime
import json
import logging
import socketserver
import time
from base64 import b64decode, b64encode
from logging import getLogger

from VTeacher.backend._logging_adapter import neuer_client_logger

from ._benutzer import User
from ._logging_kontext import LoggingKontext
from enc_netzwerkverbindung_heureka_code.__generell import AESKodierung, AESSchluessel, RSAKodierung, RSASchluessel
from .__verwalter.ablauf_verbindung import AblaufVerbindung
from .__verwalter.ablauf_benutzer import AblaufBenutzer
from .__verwalter.ablauf_test import AblaufTest


class ClientHandler(socketserver.StreamRequestHandler):
    """ Handler fuer die Verbindung zu einem Client """
    def __init__(self, public_key, secret_key, server_kontext, *args, **kwargs):
        """
        Handler fuer die Verbindung zu einem Client
        :param public_key: Der oeffentliche Schluessel des Servers
        :param secret_key: Der private Schluessel des Servers
        :param server_kontext: Der Kontext des Servers
        """
        self._logger = getLogger(__name__)

        self.callback = server_kontext.callback
        self.server_kontext = server_kontext

        self.aes_kodierung = AESKodierung(AESSchluessel.generiere_aes_schluessel())
        self.verbindung = AblaufVerbindung(
            self, self.aes_kodierung, public_key=public_key, secret_key=secret_key
        )
        super(ClientHandler, self).__init__(*args, **kwargs)

    def handle(self) -> None:
        """ Verwaltet die Verbindung zu einem Benutzer """

        self._logger.debug(f" Neuer Client will sich verbinden: {self.client_address[0]} ".center(100, "="))

        self._logger.debug("Verbindungsaufbau begonnen")
        self.verbindung.warten_auf_startnachricht()
        self.verbindung.send_public_key()

        self.aes_key = self.verbindung.receive_aes_key()
        if self.aes_key is None:
            return

        self._logger.debug("Verbindungsaufbau abgeschlossen")

        user_ablauf = AblaufBenutzer(self)
        user = user_ablauf.receive_user()

        test_ablauf = AblaufTest(self, lambda *args: self.server_kontext.test_aktiv)

        if user_ablauf.user_akzeptieren(user):
            test = test_ablauf.get_erwarteten_test()
            test_ablauf.test_starten()

            self._logger.info("Test wird begonnen")
            self.verbindung.send_encrypted(test.as_json_bytes())
            antworten = self.verbindung.receive_encrypted()
            antworten = json.loads(antworten)

            test_ablauf.test_beenden(test)

            if test_ablauf.abgabe_zulaessig:
                self._logger.info(f"Antworten abgegeben {antworten}")
                self.callback({"test": test, "user": user, "antworten": antworten})
            else:
                self._logger.warning(
                    f"Antworten nach der Zeit abgegeben,   {wirkliche_zeit} statt {erlaubtes_ende} "
                    f"{'(Test wurde vorzeitig beendet)' if test_ablauf.vorzeitig_beendet else ''}  "
                    f"{antworten}")

            self.verbindung.send_encrypted("RECEIVED".encode("utf-8"))

    pass
