from abc import ABC, abstractmethod
from typing import final

from Crypto.PublicKey.RSA import RsaKey

from enc_netzwerkverbindung_heureka_code._generell.rsa import RSASchluessel


class RSASchluesselpaar(ABC):
    """ Verwaltet ein RSA-Schluesselpaar """
    def __init__(self):
        """ Verwaltet ein RSA-Schluesselpaar """
        self.__secret_key = None
        self.__public_key = None

        self.__secret_key = self._setup()
        self.__public_key = RSASchluessel.berechne_oeffentlichen_schluessel(self.__secret_key)

    @abstractmethod
    def _setup(self) -> RsaKey:
        """ Generiert einen privaten Schluessel """
        pass

    @final
    @property
    def secret_key(self) -> RsaKey:
        """ Der private Schluessel """
        return self.__secret_key

    @final
    @property
    def public_key(self) -> RsaKey:
        """ Der oeffentliche Schluessel """
        return self.__public_key

    @final
    @property
    def schluessel_erstellt(self) -> bool:
        """ Prueft, ob die Schluesselgenerierung abgeschlossen ist """
        return self.public_key is not None

    @final
    @property
    def fingerabdruck(self) -> str:
        """ Berechnet den Fingerabdruck des oeffentlichen Schluessels """
        while not self.schluessel_erstellt:
            pass
        return RSASchluessel.calc_footprint(self.public_key)
    pass
