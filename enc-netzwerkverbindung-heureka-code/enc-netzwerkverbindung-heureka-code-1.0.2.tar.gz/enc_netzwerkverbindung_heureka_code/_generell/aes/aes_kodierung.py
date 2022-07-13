from Crypto import Random
from Crypto.Cipher import AES


class AESKodierung:
    """ Verwaltet die AES-Verschluesselung der Verbindung """

    def __init__(self, key: bytes):
        """
        Verwaltet die AES-Verschluesselung der Verbindung

        :param key: Der Schluessel der Verbindung
        """
        self.__key = key
        self.CHUNKS = 32 * 1024

    @property
    def key(self) -> bytes:
        """ Der zu verwendende Schluessel """
        return self.__key

    def encrypt(self, msg: bytes, /) -> bytes:
        """
        Verschluesselt die gegebene Nachricht

        :param msg: Die zu verschluesselnde Nachricht
        :return: Die verschluesselte Nachricht
        :rtype: bytes
        """
        IV = Random.new().read(16)
        encryptor = AES.new(self.key, AES.MODE_CFB, IV)
        size = str(len(msg)).zfill(16)
        result = b""

        result += size.encode("utf8")
        result += IV

        index = 0
        while True:
            chunk = msg[index: index + self.CHUNKS]
            if len(chunk) == 0:
                break

            if len(chunk) % 16 != 0:
                chunk += b" " * (16 - (len(chunk) % 16))

            result += encryptor.encrypt(chunk)
            index += self.CHUNKS
        return result

    def decrypt(self, c: bytes, /) -> bytes:
        """
        Entschluesselt die gegebene Nachricht

        :param c: Die zu entschluesselnde Nachricht
        :return: Die entschluesselte Nachricht
        :rtype: bytes
        """
        result = b""
        size = int(c[:16])
        IV = c[16:32]

        decrypter = AES.new(self.key, AES.MODE_CFB, IV)

        index = 32
        while True:
            chunk = c[index: index + self.CHUNKS + 1]
            if len(chunk) == 0:
                break
            result += decrypter.decrypt(chunk)
            index += self.CHUNKS
        result = result[:size]
        return result
