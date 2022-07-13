from Crypto.PublicKey.RSA import RsaKey

from enc_netzwerkverbindung_heureka_code._generell import RSASchluessel

from .rsa_basis import RSASchluesselpaar


class RSAVerwalter(RSASchluesselpaar):
    """ Variante eines RSA-Schluesselpaares """
    def _setup(self) -> RsaKey:
        """ Generiert bei jedem Start des Servers einen neuen privaten Schluessel """
        return RSASchluessel.generiere_rsa_schluessel()
