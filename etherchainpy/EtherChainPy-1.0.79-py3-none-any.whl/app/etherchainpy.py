"""
    Filename    :   etherchainpy.py
    Description :   Part of EtherChainPY
    By          :   Emmanuel Adigun (emmanuel@zignal.net)
    Date        :   10 May 2022
"""

import requests
from functools      import wraps
from .accounts      import Accounts
from .contracts     import Contracts
from .transactions  import Transactions
from .blocks        import Blocks
from .logs          import Logs
from .geth          import Geth

def sign_request(f):
    @wraps(f)
    def wrapper(self, *args, **kwargs):
        if isinstance(args[0], dict): args[0].update({"apikey":self.apikey})
        return f(self,*args,**kwargs)
    return wrapper

class EtherChainPy(object):
    """
    Etherpy for querying etherum transactions on https://www.etherscan.io
    Usage: ep = EtherPy(apikey=environ['API_KEY_ETHERSCAN'])
    """
    def __init__(self,base_url="https://api.etherscan.io/api", apikey=None):
        self.session = requests.session()
        self.base_url = base_url
        self.apikey = apikey
        self._accounts      = Accounts(self)
        self._contracts     = Contracts(self)
        self._transactions  = Transactions(self)
        self._blocks        = Blocks(self)
        self._logs          = Logs(self)
        self._geth          = Geth(self)
        
    @sign_request
    def post(self,parameters):
        self.response = None
        r = self.session.post(self.base_url, params=parameters)
        if r.status_code != 200: raise Exception("Unexpected Status Code: %s received " % r.status_code )
        return r

    @property
    def accounts(self):
        return self._accounts

    @property
    def contracts(self):
        return self._contracts

    @property
    def transactions(self):
        return self._transactions

    @property
    def blocks(self):
        return self._blocks

    @property
    def logs(self):
        return self._logs

    @property
    def geth(self):
        return self._geth







        
