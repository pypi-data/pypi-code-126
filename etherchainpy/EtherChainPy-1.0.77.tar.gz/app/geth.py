"""
    Filename    :   geth.py
    Description :   Part of EtherChainPy
    By          :   Emmanuel Adigun (emmanuel@zignal.net)
    Date        :   14 May 2022
"""


class Geth(object):
    """
    Geth Module
    """
    def __init__(self, client=None):
        super().__init__()
        self.client = client

    def get(self,parameters):
        return self.client.post(parameters)

    def convert(self, result, to ):
        from .conversions import Conversions
        c = Conversions()
        c.response = result
        c.math_base = 16  # Hexadecimal
        return c.to(to)


    """
    Returns the number of most recent block
    """
    def getBlock(self):
        return self.get( {"module":"proxy","action":"eth_blockNumber"} )

    """
    Returns information about a block by block number. The block number MUST be prepended with 0x e.g 0x32780
    """
    def getBlockByNumber(self,blockNo,flag):
        return self.get( {"module":"proxy","action":"eth_getBlockByNumber", "tag":blockNo, "boolean":flag} )
    
    """
    Returns information about an uncle by block number at index
    """
    def getUncleByIndex(self,blockNo,index):
        return self.get( {"module":"proxy","action":"eth_getUncleByBlockNumberAndIndex", "tag":blockNo, "index":index} )

    """
    Returns the number of transactions in a block
    """
    def getBlockTransactions(self,blockNo):
        return self.get( {"module":"proxy","action":"eth_getBlockTransactionCountByNumber", "tag":blockNo} )

    """
    Query a specific transaction by hash value
    """
    def getTransactionByHash(self,txhash):
        return self.get( {"module":"proxy","action":"eth_getTransactionByHash", "txhash":txhash} )

    """
    Query a specific transaction by block and/or index
    """
    def getTransactionByBlockNumberAndIndex(self,txhash,index):
        return self.get( {"module":"proxy","action":"eth_getTransactionByBlockNumberAndIndex", "txhash":txhash, "index":index} )

    """
    Query a specific address for total transactions carried out
    """
    def getTransactionCount(self,address,tag="latest"):
        return self.get( {"module":"proxy","action":"eth_getTransactionCount", "address":address, "tag":tag} )

    """
    Submits a pre-signed transaction for broadcast to the Ethereum network.
    """
    def sendRawTransaction(self,txhash):
        return self.get( {"module":"proxy","action":"eth_sendRawTransaction", "hex":txhash} )

    """
    Returns the receipt of a transaction by transaction hash.
    """
    def getTransactionReceipt(self,txhash):
        return self.get( {"module":"proxy","action":"eth_getTransactionReceipt", "txhash":txhash} )

    """
    Executes a new message call immediately without creating a transaction on the block chain.
    """
    def executeCall(self,to,data,tag="latest"):
        return self.get( {"module":"proxy","action":"eth_call", "to":to, "data":data, "tag":tag} )

    """
    Returns code at a given address.
    """
    def getCode(self,address,tag="latest"):
        return self.get( {"module":"proxy","action":"eth_getCode", "address":address, "tag":tag} )

    """
    Returns the value from a storage position at a given address.
    """
    def getStorageAt(self,address,position,tag="latest"):
        return self.get( {"module":"proxy","action":"eth_getStorageAt", "address":address, "position":position, "tag":tag} )

    """
    Returns the current price per gas in wei/gwei/eth or fiats ...
    """
    def getGasPrice(self,to="WEI"):
        return self.convert(self.get( {"module":"proxy","action":"eth_gasPrice"} ), to)

    """
    Returns an estimation of gas for a given call/transaction without adding to the etherum blockchain
    """
    def getEstimatedGasPrice(self,data,to,value,gasPrice,gas,convertTo="WEI"):
        return self.convert(self.get( {"module":"proxy","action":"eth_estimateGas","data":data,"to":to,"value":value,"gasPrice":gasPrice,"gas":gas} ), convertTo)
        





