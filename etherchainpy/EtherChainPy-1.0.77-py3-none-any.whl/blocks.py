"""
    Filename    :   blocks.py
    Description :   Part of EtherChainPy
    By          :   Emmanuel Adigun (emmanuel@zignal.net)
    Date        :   10 May 2022
"""


class Blocks(object):
    """
    Blocks Module - Some of the functions in this module require PRO subscription from etherscan. Please support them.
    """
    def __init__(self, client=None):
        super().__init__()
        self.client = client

    def getBlock(self,parameters):
        return self.client.post(parameters)


    """
    Returns the Block And Uncle Rewards by BlockNo
    """
    def getBlockByNumber(self, blockno=None):
        return self.getBlock( {"module":"block","action":"getblockreward","blockno":blockno} )

    """
    Returns the estimated time remaining, in seconds, until a certain block is mined. by BlockNo
    """
    def getBlockCountDown(self, blockno=None):
        return self.getBlock( {"module":"block","action":"getblockcountdown","blockno":blockno} )

    """
    Returns the block number that was mined at a certain timestamp : unix format e.g 1578638524, closest=before|after
    """
    def getBlockByTimestamp(self, timestamp=None, closest="before"):  #unix timestamp
        return self.getBlock( {"module":"block","action":"getblocknobytime","timestamp":timestamp, "closest":closest} )

    """
    Returns the daily average block size within a date range. PRO subscription required
    """
    def getBlockByDateRange(self, startdate=None, enddate=None, sort="asc"):  
        return self.getBlock( {"module":"stats","action":"dailyavgblocksize","startdate":startdate, "enddate":enddate, "sort":sort} )

    """
    Returns the daily average block counts and associated rewards within a date range. PRO subscription required
    """
    def getBlockCountAndRewardByDateRange(self, startdate=None, enddate=None, sort="asc"):  
        return self.getBlock( {"module":"stats","action":"dailyblkcount","startdate":startdate, "enddate":enddate, "sort":sort} )

    """
    Returns the daily MINERS block rewards. PRO subscription required
    """
    def getDailyMinersRewards(self, startdate=None, enddate=None, sort="asc"):  
        return self.getBlock( {"module":"stats","action":"dailyblockrewards","startdate":startdate, "enddate":enddate, "sort":sort} )

    """
    Returns the daily average mining block period in secs. The average time it takes for a block to be successfully mined. PRO subscription required
    """
    def getDailyAverageMiningTime(self, startdate=None, enddate=None, sort="asc"):  
        return self.getBlock( {"module":"stats","action":"dailyavgblocktime","startdate":startdate, "enddate":enddate, "sort":sort} )

    """
    Returns the daily uncle blocks + rewards. PRO subscription required
    """
    def getDailyUncleBlocks(self, startdate=None, enddate=None, sort="asc"):  
        return self.getBlock( {"module":"stats","action":"dailyuncleblkcount","startdate":startdate, "enddate":enddate, "sort":sort} )





