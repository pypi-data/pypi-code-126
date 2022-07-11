"""
通り
"""

from _toori import *
from .constants import *

import socketio
import socket

from cryptography.fernet import Fernet
import base64

import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

from engineio.payload import Payload

# Increase the packet buffer
Payload.max_decode_packets = 2500000


class TooriClient:
    # Attempts WebSocket first, else fallback to polling
    def __init__(
        self,
        server_url: str,
        server_port: int,
        pkt_filter: str,
        transport: str,
        pkt_key: str,
        loggerSignal=None,
        connectedSignal=None,
    ):
        # Set default parameters if not given
        if not server_url:
            server_url = URL_DEFAULT
        if not server_port:
            server_port = PORT_DEFAULT
        if not pkt_filter:
            pkt_filter = FILTER_DEFAULT
        if not transport:
            transport = TRANSPORT_DEFAULT
        if not pkt_key:
            pkt_key = PKT_KEY_DEFAULT

        self.connectedSignal = connectedSignal

        # Set logging function to signal instead of print if GUI is used
        self.log = print
        if loggerSignal:
            self.loggerSignal = loggerSignal
            self.log = self._logger

        self.fernet = Fernet(base64.urlsafe_b64encode(pkt_key.encode()))

        # Transport must be None for auto
        self.log(f"Using {transport} transport")
        if transport == TRANSPORT_DEFAULT:
            transport = None

        # Intercept only outbound and non loopback traffic
        # And allow traffic to the Iro server
        server_ip = self.get_ip(server_url)
        pkt_filter = (
            f"outbound && !loopback && ip.DstAddr != {server_ip} && ({pkt_filter})"
        )
        self.log(f"Using filter ({pkt_filter})")

        # Add SSL if not specified
        if not server_url.startswith("http"):
            if server_port == 443:
                server_url = f"https://{server_url}"
            else:
                server_url = f"http://{server_url}"

        self.local_ip = self.get_local_ip()

        self.sio = socketio.Client(ssl_verify=False)

        self.server_url = server_url
        self.server_port = server_port
        self.pkt_filter = pkt_filter
        self.transport = transport

    def get_ip(self, url):
        return socket.gethostbyname(url.split("//")[-1])

    def get_local_ip(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]

    def _logger(self, *args):
        self.loggerSignal.emit(" ".join(*args))

    def uninit_WinDivert(self):
        uninit_outbound()
        uninit_inbound()
        self.log("Toori unestablished")

    def disconnect_sio(self):
        self.sio.disconnect()
        self.log("Disconnected from server")

    def start_inbound_handler(self):
        @self.sio.on("ret")
        def injector(data):
            if not self.sio.connected:
                return
            inject_once(self.fernet.decrypt(data))

    def connect(self):
        self.log(f"Connecting to {self.server_url}:{self.server_port}")
        try:
            self.sio.connect(
                f"{self.server_url}:{self.server_port}", transports=self.transport
            )
        except socketio.exceptions.ConnectionError:
            self.log("Could not connect")
            return -1

        self.log(f"Connected to server")

    def start(self):
        if self.connect() == -1:
            return

        try:
            # Initialize WinDivert injector with address to replace
            init_inbound(self.local_ip)
        except (TooriException, WinDivertException) as e:
            self.log(str(e))
            self.disconnect_sio()
            return

        try:
            # Initialize WinDivert sniffer with filter
            init_outbound(self.pkt_filter)
        except (TooriException, WinDivertException) as e:
            self.log(str(e))
            self.disconnect_sio()
            uninit_inbound()
            return

        self.start_inbound_handler()

        if self.connectedSignal:
            self.connectedSignal.emit(1)

        self.log(f"Toori established")

        while True:
            try:
                self.sio.emit("out", self.fernet.encrypt(recv_once()))
            except socketio.exceptions.BadNamespaceError:
                continue