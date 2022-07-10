import platform
import datetime
import getpass
from termcolor import cprint
from .logger import Logger, LogColors

class Info():
    def __init__(self) -> None:
        # self.banner = cprint(figlet_format(
        #     'VPNroulette', font='smslant'), 'green')
        self.log = Logger()

    # def system_info(self) -> None:
    #     self.log.info(f"OS: {platform.system()}")
    #     self.log.info(f"SYSTEM USER: {getpass.getuser()}")
    #     self.log.info(f"Time: {datetime.datetime.now()}")

    def banner(self) -> None:
        """
            Print VPNR banner in the command line
        """
        cprint(f"""
                ,,,,,,,                
            ,,,,,,,,,,,,,,,            
        ,,,,,,,///////////,,,,,,,       
    ,,,,,,,//////,,,,/////,,,,,,,,,,,   
    ,,,,,/////,,///////////////,,,,,,   
    ,,,//////,/////,,,,,,,///////,,,,       Status: test
    ,,,/////,////,////////,,//////,,,       Country: test
    ,,/////,,///,,/////,///,,/////,,,       Test: test
    ,,,/////,*///,,//,,,///,,/////,,,       OS: {platform.system()}
    ,,,//////,,//////////,,//////,,,,       USER: {getpass.getuser()}
    ,,,,////////,,,,,,,,,///////,,,,,       Time: {datetime.datetime.now()}
    ,,,,,,////////////////////,,,,,,,   
        .,,,,,////////////,,,,,,        
            ,,,,,,,,,,,,,,,            
                ,,,,,,,
        """, "green")

    def disclaimer(self):
        """
            Print VPNR disclaimer
        """
        cprint(
        f"""
        {LogColors.ERROR}-----------------------------------------< D I S C L A I M E R >------------------------------------------{LogColors.NOCOLOR}
        {LogColors.ERROR}VPNroulette is a free VPN service that allows you to connect to any country in the world.{LogColors.NOCOLOR}
        {LogColors.ERROR}This software comes without any kind of guarantee and it's going to be used under your own responsability.{LogColors.NOCOLOR}
        {LogColors.ERROR}Please don't be evil, or your account will be suspended inmediately without notice{LogColors.NOCOLOR}
        {LogColors.ERROR}For more information visit: https://vpnroulette.com{LogColors.NOCOLOR}
        """)
