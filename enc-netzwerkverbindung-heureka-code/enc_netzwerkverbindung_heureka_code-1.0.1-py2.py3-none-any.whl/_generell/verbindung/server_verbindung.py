from enc_netzwerkverbindung_heureka_code._generell.verbindung import BasisCOM


class ServerVerbindungsVerwalter(BasisCOM):
    """ Verwaltet die Serverseitige Netzwerkverbindung """
    def __init__(self, wfile, rfile):
        """
        Verwaltet die Serverseitige Netzwerkverbindung

        :param wfile: Das Schreibobjekt des Servers (socketserver)
        :param rfile: Das Leseobjekt des Servers (socketserver)
        """
        self.__wfile = wfile
        self.__rfile = rfile

    def send(self, data: bytes):
        """
        Sendet Daten an den Client

        :param data: Die zu sendende Nachricht
        """
        length = str(len(data)).encode("utf-8")
        self.__wfile.write(length + b"\n")
        self.__wfile.write(data)

    def receive(self) -> bytes:
        """ Wartet auf eine Nachricht des Clients und liefert diese zurueck """
        length = int(self.__rfile.readline().rstrip(b"\n"))
        return self.__rfile.read(length)
