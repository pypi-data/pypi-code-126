from toori import TooriClient
import argparse


def main():
    parser = argparse.ArgumentParser(description="Connect to an Iro server")

    mode_group = parser.add_mutually_exclusive_group(required=True)
    mode_group.add_argument("-g", "--gui", action="store_true", help="Toori GUI")
    mode_group.add_argument(
        "-a", "--addr", help="address of server to connect to", type=str, required=False
    )

    parser.add_argument("-p", "--port", help="server port to connect to", type=int)
    parser.add_argument("-k", "--key", help="key to encrypt packets", type=str)
    parser.add_argument("-f", "--filter", help="sniffing filter to use", type=str)
    parser.add_argument(
        "-t",
        "--transports",
        help="socketIO transport method",
        type=str,
        choices=["websocket", "polling", "auto"],
    )

    args = parser.parse_args()

    if args.gui:
        from toori.gui import gui_main

        gui_main()
    else:
        cli = TooriClient(args.addr, args.port, args.filter, args.transports, args.key)
        cli.start()


if __name__ == "__main__":
    from toori.gui import gui_main

    gui_main()
