import os
import platform
import getpass
import json
import requests
from itsdangerous import base64_decode
from .logger import Logger
from .utils import Utils


class Configuration():
    """
        Configuration of the app
    """
    def __init__(self) -> None:
        self.log = Logger()
        self.utils = Utils()
        self.vpnr_dir = os.path.join(os.environ.get('HOME'), '.vpnr-client')
        self.config_file = os.path.join(self.vpnr_dir, 'config')
        self.token_file = os.path.join(self.vpnr_dir, 'token')
        self.tunnel_ovpn_file = os.path.join(self.vpnr_dir, 'tunnel.ovpn')

    def get_token(self, email: str, password: str) -> None:
        """
            Get token with your login credentials to get the tunnel
        """

        data = {'email': email, 'password': password}
        url = "http://api2.vpnroulette.net:8181/auth/login"
        r = requests.post(url, data=data)

        self.log.info("Trying to get token")
        if r.status_code == 200:
            self.log.info("You are successfully loged in!")
            self.utils.write_config(r.json(),self.token_file)
        else:
            self.log.error_and_exit(f"{r.status_code}: Bad credentials, can't get the token")

    def credentials(self) -> str:
        """
            Ask credentials with your VPNR account
        """
        email = getpass.getpass("Introduce your email: ")
        password = getpass.getpass("Introduce your password: ")
        data = {
            "email": email,
            "password": password
        }
        self.utils.write_config(data,self.config_file)
        self.get_token(email,password)

    def config_exists(self) -> None:
        """
            Check if config exists
        """
        if not os.path.isfile(self.config_file):
            self.log.warn(f"Config file {self.config_file} don't exists, creating new one")
            if not os.path.isdir(self.vpnr_dir):
                os.mkdir(self.vpnr_dir)
            self.credentials()
        else:
            config = self.utils.read_config(self.config_file)
            self.get_token(config["email"],config['password'])

    def get_tunnel_config(self) -> None:
        """
            Get your openvpn config using your credentials
        """
        token = self.utils.read_config(self.token_file)["auth_token"]
        headers = {
            'Authorization': 'Token: ' + token,
            'Content-Type': 'application/json',
            'User-Agent': platform.system(),  # Darwin, Linux, Windows
        }
        r = requests.get('http://api2.vpnroulette.net:8181/tunnel/random', headers=headers)

        self.log.info("Trying to get token")
        if r.status_code == 200:
            self.log.info("Status ok, saving tunnel.ovpn")
            tunnel_encoded_data = json.loads(r.text)
            tunnel_data = base64_decode(tunnel_encoded_data['content'])
            tunnel = str(tunnel_data, 'utf-8')
            print(self.tunnel_ovpn_file)
            self.utils.write_tunnel_config(tunnel,self.tunnel_ovpn_file)
             
            if platform.system() == "Darwin":
                self.log.info("Tunnel data specific for Mac OSX")
                with open(self.tunnel_ovpn_file, 'a+') as file:
                    file.write('script-security 2\n')
                    file.write('up /usr/local/bin/update-resolv-conf\n')
                    file.write('down /usr/local/bin/update-resolv-conf\n')
                    file.write('dhcp-option DNS 8.8.8.8\n')
                    file.write('\n')

    def clean_config(self):
        """
            Clean VPNR configurations
        """
        validation = input(str(
            "This will remove your current config and token file, are you sure [yes/no]? "))
        if validation == "yes":
            self.log.warn(f"Removing {self.config_file}")
            os.remove(self.config_file)
            self.log.warn(f"Removing {self.token_file}")
            os.remove(self.token_file)
        else:
            self.log.warn("Nothing to do with -c clean flag")
