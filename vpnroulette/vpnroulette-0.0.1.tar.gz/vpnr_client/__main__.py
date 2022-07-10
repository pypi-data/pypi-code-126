
"""Vpnroulette command line.
Usage:
------
    $ realpython [options] [id] [id ...]

Available options are:
    -h, --help         Show this help
    -l, --show-links   Show links in text
Contact:
--------
- https://realpython.com/contact/
More information is available at:
- https://pypi.org/project/realpython-reader/
- https://github.com/realpython/reader
Version:
--------
- realpython-reader v1.0.0
"""

from .config import Configuration
from .info import Info
from .tunnel import Tunnel
from .parser import parse_args

def main() -> None:
    """
        Start VPNROULETTE client
    """
    args = parse_args()
    connection = Tunnel()

    info = Info()
    info.banner()

    if args.disclaimer:
        info.disclaimer()

    if args.status:
        print(args.status)
        #connection.start_tunnel()

    config = Configuration()
    config.config_exists()
    config.get_tunnel_config()
    tunnel = Tunnel()
    tunnel.start_tunnel()

    # # Implementing -c flag to allow credentials deletion and try to create a new ones again
    # # if args.clean:
    # #     config.clean_config()


if __name__ == "__main__":
    main()
