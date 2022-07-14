#!/usr/bin/env python3

from fire import Fire
from read_vme_offline.version import __version__

#print("i... module read_vme_offline/ascdf is being run")
import pandas as pd
import tables # here, to avoid a crash when writing pandas
import h5py
import datetime
import subprocess as sp
import numpy as np
import os
import datetime as dt
import matplotlib.pyplot as plt
import read_vme_offline.general as general
from shutil import copyfile
import sys
import ROOT
from tabulate import tabulate
import nocurses_bar as ncbar
from console import fg, bg, fx
import time
from threading import Timer

import  read_vme_offline.erlang as erlang

#---------------------------------- tbar timer thing (to move later)
class RepeatTimer(Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)






def shift_channels(df , TSHIFT, TWIN, x,y):

    # df = df.loc[  df["ch"]==1 , "time"] = df["time"] + 100
    # df['time'] = df['ch'].apply(lambda x: df["time"]+100 if  x==1 else df["time"] )

    #works
    #df["time"] = df["time"] + TSHIFT*df["ch"]

    #df.loc[df['chan'] == x, 'time'] = df.loc[ df['chan']==x , 'time'] + TSHIFT
    df.loc[df['ch'] == y, 'time'] = df.loc[ df['ch']==y , 'time'] + TSHIFT
    return df


def only_read( filename, x=0, y=1, batch=0, read_last=0, MAXROWS=1000*1000):
    """
    reads the filename to DF and returns it
    """
    basename = os.path.basename(filename)
    basename = os.path.splitext(basename)[0]
    startd = basename.split("_")[1]
    startt = basename.split("_")[2]
    print("D...  time start MARK=",startd+startt)


    ok = False
    try:
        start = dt.datetime.strptime(startd+startt,"%Y%m%d%H%M%S" )
        ok = True
        print("D... succesfull start with 4 digit year")
    except:
        print("x... year may not by 4 digits")

    if not(ok):
        print("X... trying 2 digits for year")
        start = dt.datetime.strptime(startd+startt,"%y%m%d%H%M%S" )

    with open(filename) as f:
        count = sum(1 for _ in f)

    print("D... total lines=",count)
    print("D... real start",start)

    print("D... basename = ",basename)
    if read_last>0:
        print("D... read_table last",read_last)
        df = pd.read_table( filename, names=['time',"e",'x','ch','y'],
                            sep = "\s+", comment="#",
                            nrows = read_last,
                            skiprows=count-read_last,
                            error_bad_lines=False,

        )
                        #nrows = MAXROWS,
                        #skiprows=MAXROWS*batch)
    else:
        print("D... read_table batch#",batch)
        df = pd.read_table( filename, names=['time',"e",'x','ch','y'],
                        sep = "\s+", comment="#",
                        nrows = MAXROWS,
                        skiprows=MAXROWS*batch)

        print(df)
    return df


#----------------- used during the expseriment-----------------
# plot is true by default to run from cmdline
# overwrite when running from code
def fastread(filename, x=0, y=1, batch = 0, read_last=0, df = None, plot = True):
    """
    COINCIDENCES: use: ./bin_readvme fast run0023_20200220_144753.asc 0 1  --read_last 500
    """
    TSHIFT = 30 # 10 seems ok, 20 is safe (200ns)  40 broke some detetors
    TWIN = 2*TSHIFT
    CHAN0=x
    CHAN1=y
    ENE_0="chan_"+str(CHAN0)
    ENE_1="chan_"+str(CHAN1)
    MAXROWS = 1000*1000*35


    if df is None:
        df = only_read(filename, x,y,batch, read_last, MAXROWS)

    # energy is marked "e"
    df = df.rename(columns={"e":ENE_0})


    if (len(df)<MAXROWS):
        print("X... END OF FILE REACHED ***")
        CONTINUE = False
    else:
        CONTINUE = True
    print("D... len=", len(df)," SHIFTING chan IN TIME BY ",TSHIFT*10,"ns")
    df = shift_channels(df, TSHIFT, TWIN, x, y)
    print("D... len=", len(df) )


    print("D... SORTING BY TIME")
    df1=df.sort_values(by="time")
    df1.reset_index(inplace=True, drop=True)
    print("D... len=", len(df) )

    print(f"D... select channels {x},{y}")
    df1 = df1.loc[  (df1["ch"]==CHAN0)|(df1["ch"]==CHAN1) ]
    print("D... len=", len(df) )


    print("D... introducing shift differences")
    df1['prev'] = df1['time'] - df1.shift(1)['time']
    df1['next'] = - df1['time'] + df1.shift(-1)['time']

    print("D... len=", len(df1) , " dropping lonely events" )
    #df1 = df1[ (df1["prev"]<TWIN) | (df1["next"]<TWIN) ]
    df1 = df1[ (df1["prev"]<TWIN) | (df1["next"]<TWIN) ]


    print("D... len=", len(df1))

    if (1==0): # CHECK THE EVENTS IN WINDOW ========== NEXT IS GOOD
        dfnext = df1[ (df1["ch"]==0) & (df1["next"]<TWIN)]
        print("D... DF next", len(dfnext) )
        dfprev = df1[ (df1["ch"]==0) & (df1["prev"]<TWIN)]
        print("D... DF prev", len(dfprev) )


    df1[ENE_1] = df1.shift(-1)[ENE_0]
    print(df1)

    print("D... dropping all when NEXT < ",TWIN )
    df2 = df1.loc[  df1["next"]<TWIN ]
    print( "D... len =",len(df2) )
    print("D...  window mean / 3sigma ... {:.1f} +- {:.1f}".format(df2["next"].mean(),  3*df2["next"].std() ))


    if CONTINUE:
        print(f"D... only {MAXROWS} read")
        print("X...  INCOMPLETE FILE, TRY TO READ batch=", batch+1)

    if plot:
        df2.plot.scatter(x=ENE_0,  y=ENE_1,
                     ylim=(0, 6000), xlim=(0,6000),
                     s=.01);
        plt.show()
        return

    return df2


#=====================================================================

def coincidences(filename, ch0, ch1,  tree = False, TIMESHIFT = 2):
    """
    """
    print( general.freemem() )

    #*************
    nlines   = general.get_number_of_lines(filename)
    ncolumns = general.get_number_of_columns(filename)
    print(f"i... reading the table of {nlines} lines ... ({nlines/1e+6:.1f} milion lines)")
    print(f"i... reading the table of {ncolumns} columns ... ")


    #*************
    df = general.pd_read_table(filename, sort = True,  fourcolumns = (ncolumns==4) )
    #print(df.dtypes)
    #print(df)
    chan_available = df['ch'].unique()
    print("D... channels available:", chan_available )
    print("D... x        present:",df['pu'].unique() )
    if 'extras' in df:
        print("D... y        present:",df['extras'].unique() )
    print("D... Emin            :",df['E'].min() )
    print("D... Emax            :",df['E'].max() )

    if not((ch0 in chan_available) and (ch1 in chan_available)):
        print(f"X... channels {ch0} OR {ch1} not in the file !!")
        sys.exit(1)

    #-------------------------here shold be something to check double events in a detector

    #-------------------------here shold be something to check double events in a detector

    #**************** select
    df1 = general.select_channels(df, [ch0,ch1] , delete_original = True)

    n_ch0 = len(df1.loc[ df1['ch']==ch0  ])
    n_ch1 = len(df1.loc[ df1['ch']==ch1  ])
    print(f"D... # events {n_ch0} and {n_ch1}")


    #df1['time'] = np.where( df1['ch']==ch1,  df1['time'] ,  df1['time']+5.0)


    # TIMESHIFT = 2

    df1.loc[ df1['ch'] ==ch1, 'time'] += TIMESHIFT*1e-6 # ADD  x us to ch1 time
    df1 = df1.sort_values(by="time")
    df1.reset_index(inplace=True, drop=True)


    # df1.drop( df[df. < 50].index, inplace=True)
    #*************  dt us    and next_E
    df1 = general.enhance_by_dtus_and_next_E(df1)


    df1.drop(df1.tail(1).index,inplace=True) # drop last n rows


    #drop all longer than
    df1 = df1.loc[ df1['dtus']<TIMESHIFT*2 ]

    print(df1)

    print(f"D... RANDOM EVENTS starting with ch=={ch1}: ",len(df1.loc[ df1['ch']==ch1] ) )
    print(f"D... ZERO E EVENTS                       : ",len(df1.loc[ df1['E']==0] ) )
    print(f"D... ZERO E EVENTS                       : ",len(df1.loc[ df1['next_E']==0] ) )
    print()
    print(f"D... N{ch0}={n_ch0} , N{ch1}={n_ch1},  COIN# {ch0}x{ch1} = {len(df1)} ... {100*len(df1)/min(n_ch0,n_ch1):.2f} %" )

    print(f"D... dtus statistics:           MEAN = {df1['dtus'].mean():.2f}  STD={df1['dtus'].std():.2f} us" )
    print()

    bname = os.path.splitext(filename)[0]  #basename
    #--------------- histogram coincidence time
    hname = general.generate_hname(filename, ch0)+f"_coin{ch1}"
    outfile = bname+f"_{ch0}_coin{ch1}"+".txt"
    #*************
    his = general.column_to_histo(  df1['dtus']  , binmax=int(2*TIMESHIFT*100),
                                    himax=2*TIMESHIFT,
                                    savename= outfile,
                                    hname = hname,
                                    writeondisk = True, writetxt = False) # 500 for 2us is exactly channel by channel


    if tree:
        df1.rename(columns = {'E':f'E{ch0}','next_E':f'E{ch1}'}, inplace = True)
        general.save_to_tree( df1, filename, modname=f"coin" , treename = f"df{ch0}{ch1}")

    return

















if __name__=="__main__":
    print("D... fastread can be called too, from bin_readvme")
    Fire(eva_cut_time)
