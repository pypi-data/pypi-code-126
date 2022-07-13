import logging
import socket
from logging import getLogger

logger = getLogger(__name__)


def get_ip() -> str:
    """ Ermittelt die IP-Adresse des Computers """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 1))
        ip = s.getsockname()[0]
    except Exception:
        ip = "127.0.0.1"
    finally:
        s.close()
    return ip
