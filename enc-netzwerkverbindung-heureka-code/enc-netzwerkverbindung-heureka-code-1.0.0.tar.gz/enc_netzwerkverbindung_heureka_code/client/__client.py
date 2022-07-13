from enc_netzwerkverbindung_heureka_code._generell import (AESKodierung,
                                                           AESSchluessel,
                                                           EncVerbindung,
                                                           RSAKodierung,
                                                           verbindung)


class CryptoClient(verbindung.BasisCOM):
    """ Verwaltet die Clientseitige verschluesselte Verbindung """
    def __init__(self, host: str, port: int = 3901):
        """
        Verwaltet die Clientseitige verschluesselte Verbindung

        :param host: Der Hostname des Servers
        :param port: Der offene Port
        """
        super(CryptoClient, self).__init__()
        self.__verbindung = verbindung.ClientVerbindungsVerwalter(host, port)
        rsa_key = self.__verbindung.receive()
        aes_key = AESSchluessel.generiere_aes_schluessel()
        aes_kodierung = AESKodierung(aes_key)

        self.__enc = EncVerbindung(self.__verbindung, aes_kodierung)

        rsa_kodierung = RSAKodierung()
        self.__verbindung.send(rsa_kodierung.encrypt(rsa_key, aes_key))

    def send(self, data: [str, bytes]):
        """
        Sendet Daten verschluesselt an den Server

        :param data: Die zu sendenden Daten
        """
        return self.__enc.send(data)

    def receive(self) -> bytes:
        """ Empfaengt verschluesselte Daten vom Server """
        return self.__enc.receive()
