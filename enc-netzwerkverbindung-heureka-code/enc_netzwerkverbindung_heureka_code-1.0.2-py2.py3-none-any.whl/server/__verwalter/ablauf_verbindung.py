import logging
from enc_netzwerkverbindung_heureka_code.__generell import AESKodierung, AESSchluessel
from .ablauf_verwalter import Verbindungsablauf


class AblaufVerbindung(Verbindungsablauf):
    def __init__(self, handler, aes_kodierung, public_key, secret_key):
        super(AblaufVerbindung, self).__init__(
            handler=handler
        )
        self.aes_kodierung: AESKodierung = aes_kodierung
        self.public_key = public_key
        self.secret_key = secret_key

    def send_encrypted(self, msg: bytes):
        """ Sendet eine verschluesselte Nachricht an den Client """
        encrypted_msg = self.aes_kodierung.encrypt(msg)
        length = len(encrypted_msg)
        self.logger.debug(f"Wurde zu {encrypted_msg} (Laenge {length}) verschluesselt")

        self.handler.wfile.write(str(length).encode("utf8") + b"\n")
        self.handler.wfile.write(encrypted_msg + b"\n")

    def send(self, data: bytes):
        """ Sendet eine Nachricht """
        x = str(len(data))
        self.handler.wfile.write(bytes(x, encoding="utf8") + b"\n")
        self.logger.debug(f"Length send {x}")
        self.handler.wfile.write(data + b"\n")
        self.logger.debug(f"Data send {data}")

    def receive_encrypted(self) -> bytes:
        """ Wartet auf eine verschluesselte Nachricht """
        received_size = self.handler.rfile.readline().rstrip(b"\n").decode("utf-8")
        received_msg = self.handler.rfile.read(int(received_size))
        decrypted = self.aes_kodierung.decrypt(received_msg)
        self.logger.debug(f"{decrypted} wurde empfangen")
        return decrypted

    def receive(self) -> bytes:
        length = int(self.handler._sock.recv(1024).strip(b"\n"))
        return self.handler._sock.recv(length)

    def warten_auf_startnachricht(self):
        """ Leitet die Verbindung ein """
        with LoggingKontext(self._logger,
                            "Initiale Nachricht", verb_enter=" wird erwartet.",
                            verb_exit=" wurde empfangen.", verb_error=" konnte nicht empfangen werden.",
                            level_enter=logging.DEBUG, level_exit=logging.DEBUG):
            initial_msg = self.handler.rfile.readline()
            self.logger.debug(f"{initial_msg} empfangen.")

    def send_public_key(self):
        """ Sendet den oeffentlichen Schluessel an den Client """
        with LoggingKontext(self.logger, "Public Key senden", level_enter=logging.DEBUG, level_exit=logging.DEBUG):
            self.send(self.public_key.export_key())

    def receive_aes_key(self):
        """ Wartet auf den vom Client generierten Schluessel fuer AES """
        self.logger.debug("AES Key soll empfangen werden")
        try:
            aes_b64_key = self.handler.rfile.readline()
        except ConnectionResetError:
            self.logger.critical("VERBINDUNGSAUFBAU FEHLGESCHLAGEN:   "
                                  "(AES Key konnte nicht empfangen werden, "
                                  "vielleicht war der oeffentliche Schluessel falsch)")
            return
        with LoggingKontext(self.logger,
                            "AES Key ermitteln", verb_exit=" abgeschlossen  ---->  Sichere Verbindung moeglich",
                            level_exit=logging.DEBUG):
            self.logger.debug("AES Key wurde empfangen")
            self.logger.debug(f"{aes_b64_key}")

            aes_cipher_key = b64decode(aes_b64_key)
            self.logger.debug("AES Key wurde base 64 dekodiert")
            self.logger.debug(f"{aes_cipher_key}")

            self.logger.debug("Entschlüsseln des Keys begonnen")
            aes_key = RSAKodierung.decrypt(self.secret_key, aes_cipher_key)
            self.logger.debug(f"Schluessel wurde dekodiert: {aes_key}")

            self.logger.debug("AES Schluessel wurde empfangen")
        return aes_key
    pass
