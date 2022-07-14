#  Copyright (c) 2017-2021 Jeorme Douay <jerome@far-out.biz>
#  All rights reserved.

import logging
import os
import mdfreader as mdfr
import pandas
from datetime import datetime
#logging.basicConfig(format='%(levelname)s:%(message)s')

class MDF(object):
    """
    MDF class to handle MDF read operation
    """

    def __init__(self):
        super().__init__()
        self.filename=None
        self.mdf=None
        self.timestamp=datetime.fromtimestamp(0)
        #self.filename = filename
        #self.mdf = mdfr.Mdf(filename)
        self.channels = pandas.DataFrame(columns=["channel", "rename","interpolate"])

    def is_channel(self, name):
        """
        check if the channel name supplied is in the MDF file

        :param name: name of the channel/channel
        :return: True if in file, otherwise False
        """
        for time in self.mdf.masterChannelList:
            t = self.mdf.masterChannelList[time]
            if name in t:
                return True
        return False

    def add_channel(self, channel, rename="",inter=False):
        """
        Set a channel to be retrieved from the MDF.
        If a rename name is supplied, the channels will be reneamed.
        If more than one channel as the same rename name, all channels will be checked
        until one available is found.
        Interpolation should not be used on digitial signal. The interpolation is linear and should be used on non digitial signals to improve accuracy lf signal in measurement with multiple time raster.

        :param channel: channel name
        :param rename: name to be renamed to
        :param inter: Set to True to interpolate missing values, default False.
        :return: None
        """
        if rename == "":
            rename = channel
        if len(self.channels.loc[self.channels['channel']==channel])!=0:
            return
        self.channels = pandas.concat([self.channels,
            pandas.DataFrame([[channel, rename, inter]], columns=["channel", "rename","interpolate"])] #,
            #axis=0, join='outer' #defaults
        )

    # # TODO Interpolation
    # def add_channels(self,channels,renames=[]):
    #     '''
    #     Add singals from a list.
    #     :param channels: list of channels to be added
    #     :param renames: list of new names for each channels
    #     :return: Nothing
    #     The length of the renames, if not empty has to be the same length as the channels list.
    #     '''
    #     if renames!=[]:
    #         if len(renames)!=len(channels):
    #             logging.error('Renames list not the same length as the channels list')
    #         for pos in range(0,len(channels),1):
    #             self.add_channel(channels[pos],renames[pos])
    #     else:
    #         for channel in channels:
    #             self.add_channel(channel)

    def _get_channel(self, channel):
        """
        Get the data designated by the channel name

        :param channel: channel name
        :return: pandas dataframe containing the data
        """
        try:
            data = pandas.DataFrame(
                self.mdf.get_channel_data(channel),
                index=self.mdf.get_channel_data(self.mdf.get_channel_master(channel))
                )
            # TODO: insert  the index as time reference column ( not index )
            data.columns = [channel]
            return data
        except Exception as e:
            logging.error(str(e))
            return pandas.DataFrame()

    def get_data(self):
        """
        Read the MDF file and retrieved the requested data

        :param filename: filename ( with full path ) of the MDF file to open
        :return: pandas dataframe containing the datas. The time offset for the channels is set to the column offset. The dataframe indes is based on the file timestamp with the measurement time offset. This allows datetime operation on the dataframe.
        """
        data = pandas.DataFrame()
        for index, row in self.channels.iterrows():
            if row['rename'] in data.columns:
                continue
            if self.is_channel(row['channel']):
                tmp = self._get_channel(row['channel'])
                tmp.rename(columns={row['channel']: row['rename']}, inplace=True)
                data = data.join(tmp, how="outer")

        # some signals not found
        for index,row in self.channels.iterrows():
            if row['rename'] not in data.columns:
                return pandas.DataFrame()

        data['offset']=data.index
        data=data.set_index(pandas.TimedeltaIndex(data.index, unit='s')+self.timestamp,drop=True)

        # ffill or interpolate
        for index,row in self.channels.iterrows():
            if row['interpolate']==True:
                data[row['rename']].interpolate(method='index',inplace=True)
            else:
                data[row['rename']]=data[row['rename']].ffill()

        data = data.drop_duplicates()
        path,filename=os.path.split(self.filename)
        data["filename"] = filename
        return data

    # reseting the file for multiple usage
    def _set_file(self,filename):
        self.filename = filename
        self.mdf = mdfr.Mdf(filename)
        if self.mdf.MDFVersionNumber<400:
            info=mdfr.MdfInfo()
            info.read_info(filename)
            self.timestamp=datetime.fromtimestamp(info['HDBlock']['TimeStamp']/10**9)
        if self.mdf.MDFVersionNumber>=400:
            info=mdfr.MdfInfo()
            info.read_info(filename)
            self.timestamp=datetime.fromtimestamp(info['HD']['time']/10**9)
