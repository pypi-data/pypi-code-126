"""
    Filename    :   logs.py
    Description :   Part of EtherChainPy
    By          :   Emmanuel Adigun (emmanuel@zignal.net)
    Date        :   14 May 2022
"""


class Logs(object):
    """
    Logs Module
    """
    def __init__(self, client=None):
        super().__init__()
        self.client = client

    def getLogs(self,parameters):
        return self.client.post(parameters)


    """
    Returns the event logs from an address, with optional filtering by block range.
    """
    def getLogsByAddressAndBlocks(self, address="", fromBlock="", toBlock="", page=1, offset=1000):
        return self.getLogs( {"module":"logs","action":"getLogs","address":address, "fromBlock":fromBlock, "toBlock":toBlock, "page":page, "offset":offset } )
    
    """
    Returns the event logs from block range with optional filtering by topics
    """
    def getLogsByBlockRangeAndTopic(self, fromBlock="", toBlock="", topic0="", topic0_1_opr="", topic1="", page=1, offset=1000):
        return self.getLogs( {"module":"logs","action":"getLogs","fromBlock":fromBlock, "toBlock":toBlock, "topic0":topic0, "topic0_1_opr":topic0_1_opr, "topic1":topic1, "page":page, "offset":offset } )

    """
    Returns the event logs by address,block range with optional filtering topics
    """
    def getLogsByBlockRangeAndTopic(self, address="", fromBlock="", toBlock="", topic0="", topic0_1_opr="", topic1="", page=1, offset=1000):
        return self.getLogs( {"module":"logs","action":"getLogs", "address":address, "fromBlock":fromBlock, "toBlock":toBlock, "topic0":topic0, "topic0_1_opr":topic0_1_opr, "topic1":topic1, "page":page, "offset":offset } )
