import secrets
import string

from Crypto.Hash import SHA256


class AESSchluessel:
    """ Verwaltet die AES-Verschluesselung der Verbindung """

    CHARS = string.ascii_letters + string.digits + string.punctuation
    KEY_LEN = 139

    @classmethod
    def generiere_aes_schluessel(cls) -> bytes:
        """
        Generiert einen neuen kryptographischen AES Schlüssel für die Verbindung.

        Fuer das Passwort wird der SHA256-Hash aus KEY_LEN-Mal zufaellig aus CHARS ausgewaehlten Zeichen gebildet.

        :return: Der generierte Schlüssel
        :rtype: bytes
        """
        secret_chars = "".join(secrets.choice(cls.CHARS) for _ in range(cls.KEY_LEN))
        return SHA256.new(secret_chars.encode("utf8")).digest()
