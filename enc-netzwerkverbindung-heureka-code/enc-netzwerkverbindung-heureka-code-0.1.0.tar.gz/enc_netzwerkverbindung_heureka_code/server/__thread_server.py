from .__server import StdSocketServer


class SocketServer(StdSocketServer):
    def start(self, server_kontext: ServerKontext):
        """
        Startet den Server in einem separaten Thread

        :param server_kontext: Der Kontext des Servers
        """
        self.__thread = threading.Thread(
            target=lambda *args: super(ThreadServer, self).start(server_kontext), name="Server", daemon=True
        )
        self.__thread.start()
    pass
