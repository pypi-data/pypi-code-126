"""
    Filename    :   contracts.py
    Description :   Part of EtherChainPy
    By          :   Emmanuel Adigun (emmanuel@zignal.net)
    Date        :   10 May 2022
"""


class Contracts(object):
    """
    Contracts Module
    """
    def __init__(self, client=None):
        super().__init__()
        self.client = client

    def find(self,parameters):
        return self.client.post(parameters)

    """
    Returns the Contract Application Binary Interface ( ABI ) of a verified smart contract.
    """
    def findABI(self, address):
        return self.find( {"module":"contract","action":"getabi","address":address} )

    """
    Returns the Solidity source code of a verified smart contract.
    """
    def findSourceCode(self, address):
        return self.find( {"module":"contract","action":"getsourcecode","address":address} )


    






