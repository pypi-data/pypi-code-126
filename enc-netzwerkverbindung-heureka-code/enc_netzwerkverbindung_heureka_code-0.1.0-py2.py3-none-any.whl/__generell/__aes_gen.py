import secrets
import string
from Crypto.Hash import SHA256


class AESSchluessel:
    """ Verwaltet die AES-Verschluesselung der Verbindung """

    CHARS = string.ascii_letters + string.digits + string.punctuation
    CHUNKS = 32 * 1024
    KEY_LEN = 139

    @classmethod
    def generiere_aes_schluessel(cls) -> bytes:
        """
        Generiert einen neuen kryptographischen AES Schlüssel für die Verbindung

        :return: Der generierte Schlüssel
        :rtype: bytes
        """
        secret_chars = "".join(secrets.choice(CHARS) for _ in range(KEY_LEN))
        return SHA256.new(secret_chars.encode("utf8")).digest()
