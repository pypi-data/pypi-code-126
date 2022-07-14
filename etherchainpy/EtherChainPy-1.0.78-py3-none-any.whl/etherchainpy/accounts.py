"""
    Filename    :   etherpy.py
    Description :   Part of EtherChainPy
    By          :   Emmanuel Adigun (emmanuel@zignal.net)
    Date        :   10 May 2022
"""
from .conversions import Conversions
class Accounts(Conversions):
    """
    Accounts Module
    """
    def __init__(self, client=None):
        super().__init__(client=client)
        self.client = client

    """
    Returns the Ether balance of a single address.
    """
    def balance(self, address, tag="latest"):
        p = {"module":"account","action":"balance","address":address,"tag":tag}
        self.response = self.client.post(p)
        return self

    """
    Returns the Ether balance of a multiple addresses.
    """
    def balances(self, addresses, tag="latest"):
        p = {"module":"account","action":"balancemulti","tag":tag}
        if isinstance(addresses, list):
            addr = ""
            first = True
            for address in addresses:
                if not first: addr += ","
                first = False
                addr += address
            p.update({"address":addr})
            self.response = self.client.post(p)
        return self




    """
    Returns the list of transactions performed by an address, with optional pagination. Max 10000
    """
    def normalTransactionByAddress(self,address=None, startblock=0, endblock=99999999, page=1, offset=0, sort="asc"):
        p = {"module":"account","action":"txlist","address":address,"startblock":startblock,"endblock":endblock,"page":page,"offset":offset,"sort":sort}
        self.response = self.client.post(p)
        return self

    
    """
    Returns the list of internal transactions performed by an address, hash and/or block ranges with optional pagination.
    """
    def internalTransactions(self,address=None,hashvalue=None, startblock=0, endblock=99999999, page=1, offset=0, sort="asc"):
        if address == None and hashvalue == None: # By block range
            p = {"module":"account","action":"txlistinternal","startblock":startblock,"endblock":endblock,"page":page,"offset":offset,"sort":sort}
        elif hashvalue != None: #By Hash
            p = {"module":"account","action":"txlistinternal","txhash":hashvalue}
        elif address != None:
            p = {"module":"account","action":"txlistinternal","address":address,"startblock":startblock,"endblock":endblock,"page":page,"offset":offset,"sort":sort}
        self.response = self.client.post(p)
        return self

    """
    Returns the list of ERC-20, ERC-721 and ERC-1155 tokens transferred by an address, with optional filtering by token contract address.
    """
    def getTokenList(self,token_type="ERC-20",address=None,contractaddress=None,startblock=0, endblock=99999999, page=1, offset=0, sort="asc"):
        if   token_type == "ERC-20": action = "tokentx"
        elif token_type == "ERC-721": action = "tokennfttx"
        elif token_type == "ERC-1155": action = "token1155tx"
        else: action = "tokentx"
        p = {"module":"account","action":action,"address":address,"contractaddress":contractaddress,"startblock":startblock,"endblock":endblock,"page":page,"offset":offset,"sort":sort}
        self.response = self.client.post(p)
        return self

    """
    Returns the list of blocks mined by an address.
    """
    def getTotalBlocksMined(self, address=None, page=1, offset=0):
        p = {"module":"account","action":"getminedblocks","address":address,"blocktype":"block","page":page,"offset":offset}
        self.response = self.client.post(p)
        return self


    """
    Get Historical Ether Balance for a Single Address By BlockNo
    """
    def getHistoricalBalanceAtBlock(self, address=None, blockno=0):
        p = {"module":"account","action":"balancehistory","address":address,"blockno":blockno}
        self.response = self.client.post(p)
        return self









