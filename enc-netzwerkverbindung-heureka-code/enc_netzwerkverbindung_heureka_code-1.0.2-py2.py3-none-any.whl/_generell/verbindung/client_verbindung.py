import socket
from weakref import finalize

from enc_netzwerkverbindung_heureka_code._generell.verbindung import BasisCOM
from enc_netzwerkverbindung_heureka_code.exceptions import VerbindungFehlgeschlagen


class ClientVerbindungsVerwalter(BasisCOM):
    """ Verwaltet die Clientseitige Netzwerkverbindung """
    def __init__(self, host: str, port: int):
        """
        Verwaltet die Clientseitige Netzwerkverbindung

        :param host: Der Hostname des Servers
        :param port: Der offene Port
        """
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.HOST, self.PORT = host, port
        try:
            self.__socket.connect((self.HOST, self.PORT))
        except ConnectionRefusedError:
            raise VerbindungFehlgeschlagen(host, port) from None
        self.__destructor = finalize(self, lambda *args, **kwargs: self.__socket.close())

    def send(self, data: bytes):
        """
        Sendet Daten an den Server

        :param data: Die zu sendende Nachricht
        """
        x = str(len(data)).encode("utf-8")
        self.__socket.sendall(x + b"\n")
        self.__socket.sendall(data)

    def receive(self) -> bytes:
        """ Wartet auf eine Nachricht des Servers und liefert diese zurueck """
        length = int(self.__socket.recv(1024).strip(b"\n"))
        return self.__socket.recv(length)
