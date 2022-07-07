import socket
import threading
from time import sleep
class TCPSocketClient:
    def __init__(self,port: int,host: str = "127.0.0.1",writer_delay: float = 0.1) -> None:
        self.writer_delay = writer_delay
        self.__socket__ = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.host = host
        self.port = port
        self.__socket__.connect((self.host,self.port))
        self.__read_buffer__ = []
        self.__write_buffer__ = []
        threading.Thread(target=self.__socket_reader__).start()
        threading.Thread(target=self.__socket_writer__).start()
    def __socket_reader__(self) -> None:
        while True:
            data = self.__socket__.recv(1024)
            if data != "":
                self.__read_buffer__.append(data.decode())
    def __socket_writer__(self) -> None:
        while True:
            if self.__write_buffer__:
                try:
                    self.__socket__.send(self.__write_buffer__.pop(0).encode())
                except:
                    print("Socket Error!, Reconnecting . . .")
                    self.__socket__.connect((self.host,self.port))
                sleep(self.writer_delay)
            sleep(0.03)
    def send(self, payload) -> None:
            self.__write_buffer__.append(str(payload))
    def read(self) -> str:
        if self.__read_buffer__:
            return self.__read_buffer__.pop(0)
        return ""
    def get_buffer_length(self) -> int:
        return len(self.__read_buffer__)
    def is_avaliable(self):
        if self.__read_buffer__:
            return True
        return False