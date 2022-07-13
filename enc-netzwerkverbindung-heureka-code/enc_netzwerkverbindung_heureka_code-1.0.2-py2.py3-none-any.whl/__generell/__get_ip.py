import socket
from logging import getLogger
from .__logging_kontext import LoggingKontext
logger = getLogger(__name__)


def get_ip():
    """ Ermittelt die IP-Adresse des Servers """
    with LoggingKontext(
            logger, "IP-Adresse", verb_enter=" soll ermittelt werden", verb_exit=" wurde ermittelt",
            verb_error=" konnte nicht ermittelt werden", level_exit=logging.DEBUG):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.connect(("8.8.8.8", 1))
            ip = s.getsockname()[0]
        except Exception:
            ip = "127.0.0.1"
        finally:
            s.close()
    return ip
