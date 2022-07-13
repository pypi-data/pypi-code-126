from enc_netzwerkverbindung_heureka_code._generell.verbindung import BasisCOM


class EncVerbindung(BasisCOM):
    """ Verwaltet eine verschluesselte Verbindung mit AES """
    def __init__(self, verbindung: BasisCOM, aes_kodierung):
        """
        Verwaltet eine verschluesselte Verbindung mit AES

        :param verbindung: Die zu nutzende Verbindung
        :param aes_kodierung: Die fuer Ver- und Entschluesselung zustaendige Instanz
        """
        self._verbindung = verbindung
        self.__aes_kodierung = aes_kodierung

    def send(self, data: [str, bytes]):
        """
        Sendet eine verschluesselte Nachricht an den Client

        :param data: Die zu sendende Nachricht
        """
        if isinstance(data, str):
            data = data.encode("utf-8")
        if not isinstance(data, bytes):
            raise TypeError(data, type(data))

        encrypted_msg = self.__aes_kodierung.encrypt(data)
        self._verbindung.send(encrypted_msg)

    def receive(self) -> bytes:
        """ Wartet auf eine verschluesselte Nachricht und liefert diese zurueck """
        received_msg = self._verbindung.receive()
        decrypted = self.__aes_kodierung.decrypt(received_msg)
        return decrypted
    pass
