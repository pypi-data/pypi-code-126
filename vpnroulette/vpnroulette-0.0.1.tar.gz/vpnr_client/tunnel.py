import os
import subprocess
from .logger import Logger
from .config import Configuration

class Tunnel:
    """
        Connection with our VPNR servers
    """
    def __init__(self) -> None:
        self.log = Logger()
        self.tunnel_config = os.path.expanduser('~/.vpnr-client/tunnel.ovpn')
        self.configuration = Configuration()

    def start_tunnel(self):
        """
            Start the tunnel
        """

        if os.geteuid() != 0:
            self.log.info("You are not root, we need sudo permissions: ")
            subprocess.Popen(['sudo', 'openvpn', '--config', self.tunnel_config])
        else:
            subprocess.Popen(['sudo', 'openvpn', '--config', self.tunnel_config])

