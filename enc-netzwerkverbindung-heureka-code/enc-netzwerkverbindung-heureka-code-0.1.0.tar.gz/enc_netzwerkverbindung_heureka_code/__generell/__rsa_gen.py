from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256


class RSASchluessel:
    @classmethod
    def generiere_rsa_schluessel(cls) -> RSA.RsaKey:
        """
        Generiert einen neuen Schlüssel für RSA

        :return: Der generierte Schlüssel
        :rtype: RSA.RsaKey
        """
        return RSA.generate(4096)

    @classmethod
    def fussabdruck_berechnen(cls, k: RSA.RsaKey, /) -> str:
        """
        Berechnet den Fingerabdruck des gegebenen Schluessels

        :param k: Der gegebene Schluessel
        :return: Der Fingerabdruck des Schluessels
        :rtype: str
        """
        return SHA256.new(k.export_key()).hexdigest().upper()

    @classmethod
    def berechne_oeffentlichen_schluessel(cls, sk: RSA.RsaKey, /) -> RSA.RsaKey:
        """
        Generiert den zu einem privaten Schluessel gehoerigen oeffentlichen Schluessel

        :param sk: Der private Schluessel
        :return: Der oeffentliche Schluessel
        """
        return sk.public_key()

    pass
