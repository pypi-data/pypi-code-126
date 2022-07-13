from logging import getLogger

from enc_netzwerkverbindung_heureka_code._generell import (AESKodierung,
                                                           RSAKodierung)
from enc_netzwerkverbindung_heureka_code._generell.cipher import EncVerbindung
from enc_netzwerkverbindung_heureka_code._generell.verbindung import (
    BasisCOM, ServerVerbindungsVerwalter)


class CryptoVerwalter(BasisCOM):
    """ Verwaltet den verschluesselten Verbindungsaufbau des Servers """
    def __init__(self, verbindung: ServerVerbindungsVerwalter, rsa):
        """
        Verwaltet den verschluesselten Verbindungsaufbau des Servers

        :param verbindung: Die zu verwendende Verbindung
        :param rsa: Das RSA-Schluesselpaar
        """
        self.verbindung = verbindung

        self.logger = getLogger(__name__)

        self.__rsa = rsa

        self.__aes_key = None
        self.__enc = None

    @property
    def secret_key(self):
        """ Der private Schluessel """
        return self.__rsa.secret_key

    @property
    def public_key(self):
        """ Der oeffentliche Schluessel """
        return self.__rsa.public_key

    def send(self, data: [bytes, str]):
        """
        Sendet verschluesselte Daten an den Client

        Funktioniert nur, falls die verschluesselte Verbindung aufgebaut wurde (Aufruf von _setup() sichern)
        """
        return self.__enc.send(data)

    def receive(self) -> bytes:
        """
        Empfaengt verschluesselte Daten des Clients

        Funktioniert nur, falls die verschluesselte Verbindung aufgebaut wurde (Aufruf von _setup() sichern)
        """
        return self.__enc.receive()

    def _send_public_key(self):
        """ Sendet den oeffentlichen Schluessel an den Client """
        self.logger.debug("Public Key wird gesendet")
        self.verbindung.send(self.public_key.export_key())
        self.logger.debug("Public Key wurde gesendet")

    def _receive_aes_key(self):
        """ Wartet auf den vom Client generierten Schluessel fuer AES """
        self.logger.debug("AES Key soll empfangen werden")
        try:
            aes_cipher_key = self.verbindung.receive()
        except ConnectionResetError:
            self.logger.critical("VERBINDUNGSAUFBAU FEHLGESCHLAGEN:   "
                                 "(AES Key konnte nicht empfangen werden, "
                                 "vielleicht war der oeffentliche Schluessel falsch)")
            return
        self.logger.debug("AES Key wurde empfangen")
        self.logger.debug(f"{aes_cipher_key}")

        self.logger.debug("Entschlüsseln des Keys begonnen")
        aes_key = RSAKodierung.decrypt(self.secret_key, aes_cipher_key)
        self.logger.debug(f"Schluessel wurde dekodiert: {aes_key}")

        self.logger.debug("AES Schluessel wurde empfangen")
        return aes_key

    def _setup(self):
        """ Initialisiert die Verbindung """
        self._send_public_key()
        self.__aes_key = self._receive_aes_key()
        self.__enc = EncVerbindung(self.verbindung, AESKodierung(self.__aes_key))

    @property
    def aes_key(self) -> bytes:
        """ Der fuer AES zu verwendende Schluesel """
        return self.__aes_key

    pass
