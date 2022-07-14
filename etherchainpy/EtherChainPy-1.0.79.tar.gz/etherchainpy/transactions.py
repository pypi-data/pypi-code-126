"""
    Filename    :   transactions.py
    Description :   Part of EtherPY
    By          :   Emmanuel Adigun (emmanuel@zignal.net)
    Date        :   10 May 2022
"""


class Transactions(object):
    """
    Transactions Module
    """
    def __init__(self, client=None):
        super().__init__()
        self.client = client

    def check(self,parameters):
        return self.client.post(parameters)

    """
    Returns the status code of a contract execution by hash
    """
    def checkStatus(self, txhash):
        return self.check( {"module":"transaction","action":"getstatus","txhash":txhash} )

    """
    Returns the status code of a contract execution by hash. Note: Only applicable for Byzantium transactions  
    https://www.investopedia.com/news/what-byzantium-hard-fork-ethereum/
    """
    def checkByzantiumStatus(self, txhash):
        return self.check( {"module":"transaction","action":"gettxreceiptstatus","txhash":txhash} )




    






