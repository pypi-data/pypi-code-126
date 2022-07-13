from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA


class RSAKodierung:
    """ Verwaltet die RSA-Verschluesselung der Verbindung """

    @classmethod
    def encrypt(cls, pk: [RSA.RsaKey, bytes], msg: bytes, /) -> bytes:
        """
        Verschluesselt eine Nachricht mit RSA

        :param pk: Der oeffentliche Schluessel
        :param msg: Die zu verschluesselnde Nachricht
        :return: Die verschluesselte Nachricht
        :rtype: bytes
        """
        pk = pk if isinstance(pk, RSA.RsaKey) else RSA.import_key(pk)
        cipher = PKCS1_OAEP.new(pk)
        c = cipher.encrypt(msg)
        return c

    @classmethod
    def decrypt(cls, sk: RSA.RsaKey, c, /) -> bytes:
        """
        Entschluesselt die verschluesselte Nachricht mit dem privaten Schluessel

        :param sk: Der private Schluessel fuer die Entschluesselung
        :param c: Die verschluesselte Nachricht
        :return: Die entschluesselte Nachricht
        :rtype: bytes
        """
        cipher = PKCS1_OAEP.new(sk)
        msg = cipher.decrypt(c)
        return msg

    pass
