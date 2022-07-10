import argparse


def parse_args():
    parser = argparse.ArgumentParser(
        description="""VPNROULETTE CLIENT""",
        add_help=True,
        prog="vpnroulette"
    )
    parser.add_argument(
        "-l",
        "--level",
        choices=["INFO", "WARNING", "ERROR", "CRITICAL", "DEBUG"],
        required=False,
        dest="log_level",
        default="DEBUG",
        help="""level of logging""",
        type=str,
    )
    parser.add_argument(
        "-d",
        "--disclaimer",
        required=False,
        dest="disclaimer",
        action='store_true',
        help="""Display VPNR disclaimer""",
    )
    parser.add_argument('status', nargs='?')
    # parser.add_argument(
    #     "connect",
    #     nargs='?',
    #     required=False,
    #     dest="connect",
    #     # action="store_true",
    #     help="""Connect vpnroulette in our servers""",
    # )
    # parser.add_argument(
    #     "-c",
    #     "--clean",
    #     required=False,
    #     dest="clean",
    #     action='store_true',
    #     help="""Clean credentials""",
    # )

    return parser.parse_args()
