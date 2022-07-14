#  Copyright (c) 2017-2021 Jeorme Douay <jerome@far-out.biz>
#  All rights reserved.
# Far-Out extraction
import glob
import pandas
import progressbar
import logging
from .mdf import MDF

class Extract(MDF):
    '''
    Extract class extract channels from single or multiple files
    '''
    def __init__(self):
        super().__init__()
        #self.channels = pandas.DataFrame(columns=['channel', 'rename','interpolate'])
        self.files = []

    def add_file(self, filename):
        '''
        Add single file to the list of files to be processed
        '''
        # TODO: docu add_file
        self.files.append(filename)
        self.files=list(set(self.files)) # remove dual entries just in case

    def add_directory(self, pathname):
        '''
        Add a directory recursively to the files to be processed.
        Files recognize are mdf and mf4 exensions
        '''
        # TODO: docu add directory
        self.files.extend(glob.glob(pathname + '/**/*.mdf', recursive=True))
        self.files.extend(glob.glob(pathname + '/**/*.mf4', recursive=True))
        self.files.extend(glob.glob(pathname + '/**/*.dat', recursive=True))
        self.files=list(set(self.files)) # remove dual entries just in case
        # TODO log info how may files were added

    # def add_channel(self, channel, rename='', inter=False):
    #     '''
    #     Set a channel to be retrieved from the MDF.
    #     If a rename name is supplied, the channels will be reneamed.
    #     If more than one channel as the same rename name, all channels will be checked
    #     until one available is found.

    #     :param channel: channel name
    #     :param rename: name to be renamed to
    #     :return: None
    #     '''
    #     if rename == "":
    #         rename = channel
    #     if len(self.channels.loc[self.channels['channel']==channel])!=0:
    #         return
    #     self.channels = pandas.concat([self.channels,
    #         pandas.DataFrame([[channel, rename,inter]], columns=["channel", "rename",'interpolate'])] #,
    #         #axis=0, join='outer' #defaults
    #     )

#     def add_channels(self, channels, renames=[]):
#         '''
#         Add singals from a list.

#         :param channels: list of channels to be added
#         :param renames: list of new names for each channels
#         :return: Nothing
# y
#         The length of the renames, if not empty has to be the same length as the channels list.
#         '''
#         # TODO extraoolation for multiple
#         if renames!=[]:
#             if len(renames)!=len(channels):
#                 logging.error('Renames list not the same length as the channels list')
#             for pos in range(0,len(channels),1):
#                 self.add_channel(channels[pos],renames[pos])
#         else:
#             for channel in channels:
#                 self.add_channel(channel)

    def get_all(self):
        '''
        Read the MDF files and retrieved the requested data.

        :return: pandas dataframe contaiing the datas.
        '''
        data = pandas.DataFrame()
        count=0
        with progressbar.ProgressBar(max_value=len(self.files)) as bar:
            bar.update(count)
            for filename in self.files:
                self._set_file(filename)
                data = pandas.concat([data,self.get_data()]) #data.append(mdf.get_data())
                count+=1
                bar.update(count)
        return data

    # def set_rename(self, channel, rename):
    #     """
    #     Set the rename of a channel.

    #     :param channel: channel name
    #     :param rename: name to be renamed to
    #     :return: None
    #     """
    #     rows=self.channels.loc[self.channels['channel']==channel]

    #     if len(rows)==0:
    #         #if not in list, add !
    #         self.channels = pandas.concat([self.channels,
    #             pandas.DataFrame([[channel, rename]], columns=["channel", "rename"])] #,
    #             #axis=0, join='outer' #defaults
    #         )
    #     else:
    #         # update the rename if already in list
    #         self.channels.loc[self.channels['channel']==channel,'rename'] =rename

    # def set_renames(self,channels,renames):
    #     '''
    #     Set renames to channels.

    #     :param channels: list of channels to be added
    #     :param renames: list of new names for each channels
    #     :return: Nothing

    #     The length of the renames has to be the same length as the channels list.
    #     '''
    #     if len(renames)!=len(channels):
    #         logging.error('Renames list not the same length as the channels list')
    #     #self.channels.loc[self.channels['channel']==channels,'rename']=renames
    #     for pos in range(0,len(channels),1): # could be done faster with pandas remplace, reusing code
    #         self.set_rename(channels[pos],renames[pos])

    # TODO set interpolation

    def __iter__(self):
        self.index=0
        return self

    def __next__(self):
        if self.index>=len(self.files):
            raise StopIteration
        filename=self.files[self.index]
        self.index+=1
        self._set_file(filename)
        return self.get_data()

