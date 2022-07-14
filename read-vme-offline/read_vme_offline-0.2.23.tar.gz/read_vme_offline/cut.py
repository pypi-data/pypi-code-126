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








#=============================== MAIN1 EVA ==================
def eva_cut_time(filename,  chan, od=0, do=9999999 ,   TIMEWIN_US = 4,  tree = False):
    """
    EVA: use: read_vme_offline cut1 filename_with_asc 0 60 120; Or 0 60 0==cut to 1m pieces
    """
    # od = 0              OR  60
    # do = 999999          and 0 means  60s cuts


    #sys.exit(1)

    started = dt.datetime.now()
    tbar = ncbar.Topbar(1)
    tbar2 = tbar.add(2)
    tbar.print_to( (1,1),  f'{fg.white}{fx.bold}{dt.datetime.now()}{fg.default}' )
    tbar2.print_to( (1,2),  f'{fg.black}{fx.bold}{(dt.datetime.now()-started).total_seconds():.1f}{fg.default}' )
    tbar.print_to( (20,1),  f'{fg.black}  {filename}{fg.default}' )
    tbar.print_to( (60,1),  f'{fg.red}{fx.bold}  {TIMEWIN_US}{fg.default}' )

    def dummyfn(msg="foo"):
        tbar.print_to( (1,1),  f'{fg.white}{fx.bold}{dt.datetime.now()}{fg.default}' )
        tbar2.print_to( (1,2),  f'{fg.black}{fx.bold}{(dt.datetime.now()-started).total_seconds():.1f}{fg.default}' )
        tbar.place()
        #    print(msg)

    timer = RepeatTimer(0.2, dummyfn)
    timer.start()
    #time.sleep(5)


    print("D... expect 30Mevents processed per minute at best")
    print( general.freemem() )

    #tbar.place()
    #*************
    start = general.filename_decomp(filename)   #  - get start
    #tbar.place()


    print(f"D... real start",start)
    od_dt = dt.timedelta(seconds=od)
    do_dt = dt.timedelta(seconds=do)
    print(f"D... skip       {od} sec ... {od_dt}")

    #tbar.place()

    startcut = start + od_dt
    stopcut = start + do_dt
    print(f"D... CUT  start {startcut}")
    print(f"D... CUT  stop  {stopcut}  (demanded or max)")

    #tbar.place()

    #*************
    nlines   = general.get_number_of_lines(filename)
    ncolumns = general.get_number_of_columns(filename)
    print(f"i... reading the table of {nlines} lines ... ({nlines/1e+6:.1f} milion lines)")
    print(f"i... reading the table of {ncolumns} columns ... ")
    #print(f"i... reading the table of {ncolumns} columns ... ", end="")

    #tbar.place()


    tbar.print_to( (70,1),  f'{bg.yellow} reading table + sorting {bg.default}' )
    #tbar.place()

    #*************
    df = general.pd_read_table(filename, sort = True, fourcolumns = (ncolumns==4) )
    # df = general.pd_read_table(filename, sort = True, fourcolumns = False ) # we need to test PU and overflow with 4 colkumns only
    # print(df)

    #tbar.place()

    print("+"*50,"BASICS TOTAL BEGIN")
    chan_available = df['ch'].unique()
    print("D... channels available:", chan_available, "   chan selected:", chan)
    print(f"D... pu        present: {df['pu'].unique()} ... 1 or 0 (3v0 before 2020)" )
    if 'extras' in df:
        print(f"D... extras    present: {df['extras'].unique()}... 1..satur,3..roll,4..reset,8..fake" )
        print(f"D... total saturations: ",len( df.loc[ (df['extras']&1)==1]  ) )
    print("D... Emin            :",df['E'].min() )
    print("D... Emax            :",df['E'].max() )
    print("D... lasttime        :",df['time'].max() )
    print("+"*50,"BASICS TOTAL END")

    cava = " ".join( [str(i) for i in chan_available] )
    tbar.print_to( (70,1),  f'{bg.white} chan-avail: {chan_available} {bg.default}' )
    #tbar.place()

    #==========--------------------------AUTOMATIC TRICK TO CUT
    if od!=0:
        if do==0:
            last_moment = int(df['time'].max()+od+1)
            del df
            for i in range(0, last_moment, od ): #be sure
                eva_cut_time(filename,  chan, od=i, do=i+od ,   tree = False)
            print("i... done many cuts; end")
            return
    #--------------------------------------- but obviously bad........




    if not(chan in chan_available):
        print(f"X... no events in channel {chan}")
        return

    #------------------

    od_do_name = ""
    if (od!=0) or (do<9999999):
        od_do_name = f"_{od:06d}_{do:06d}"
        tbar.print_to( (70,1),  f'{bg.yellow} selecting {od_do_name} {bg.default}' )
        print()
        print(f"D...  selecting events    from {od}s to {do}s")
        print(f"D...  selecting events    from {od}s to {do}s")
        print(f"D...  selecting events    from {od}s to {do}s")
        print()
        #tbar.place()

        df1 = df[ (df.time>=od)&(df.time<do)  ].copy() # copy ELSE warning....
        df1.reset_index(inplace=True, drop=True)
        df1.fillna(0,inplace=True)

        print(df1)
        #tbar.place()

        if len(df1)==0:
            print(f"D... no data for channel {chan}")
            sys.exit(0)

    else:
        df1 = df



    #---------------------------------------------------DF1 ---------------------------
    #************* reduce the DF  when true-delete original....
    tbar.print_to( (70,1),  f'{bg.yellow} select ch= {chan} {bg.default}' )
    #tbar.place()

    df1 = general.select_channels(df1, [chan] , delete_original = True)
    #tbar.place()



    print("+"*50,"BASICS BEGIN CHANNEL ",chan)
    chan_available = df1['ch'].unique()
    print("D... channels available:", chan_available, "   chan selected:", chan)

    print(f"D... pu        present: {df1['pu'].unique()}... 1 or 0 (3v0 before 2020)" )
    #print(f"D... pu        present: {df1['pu'].unique()}... 1 or 0 (3v0 before 2020)" )
    pileups_ch = len(df1.loc[ df1['pu']==1])  # (3)for 4 columns, it is fixed in table_read

    if 'extras' in df:
        print(f"D... extras    present: {df1['extras'].unique()}... 1..satur,3..roll,4..reset,8..fake" )
        print(f"D... number of saturations: ",len( df1.loc[ (df1['extras']&1)==1]  ) )
    print("D... Emin            :",df1['E'].min() )
    print("D... Emax            :",df1['E'].max() , f" 2^15={2**15}")
    print("+"*50,"BASICS END     CHANNEL ",chan)



    #*************  dt us    and next_E

    tbar.print_to( (70,1),  f'{bg.yellow} enhancing df {bg.default}' )
    #tbar.place()
    df1, dtusmin, dtusmax = general.enhance_by_dtus_and_next_E(df1)

    tbar.print_to( (70,1),  f'{bg.yellow} enhanced {bg.default}' )
    #tbar.place()

    if 'extras' in  df1:
        satu_n_ch = len(df1.loc[ (df1['extras']&1)!=0] )
        print(f"D... SATURATIONS  n={satu_n_ch}\n",df1.loc[ (df1['extras']&1)!=0] )

        Tsatu_ch = df1.loc[ (df1['extras']&1)!=0]["prev_satu"].sum()/1e+6   # in sec...
        print(f"D... SATURATIONS {satu_n_ch} total: {Tsatu_ch} sec.")
    else:
        satu_n_ch = None
        Tsatu_ch = None




    stat_columns = ['ch','start','Treal','Ntot','rate']  # ----------- not final, adding later

    df_stat = pd.DataFrame( np.nan, index=[0], columns = stat_columns )
    df_stat['ch'] = chan
    df_stat['start'] = od
    df_stat['Twin'] = TIMEWIN_US

    if Tsatu_ch != None:
        df_stat['Nsat'] = satu_n_ch
        df_stat['Tsat'] = Tsatu_ch
    #    else:
    #        df_stat['satT'] = None


    #print(" ... trying min dtus this is very expensive with memory ...", flush=True)
    df_stat['min_dtus'] = dtusmin # I use the value from before......

    #df_stat['min_dtus'] = df1.loc[df1['dtus']!=0]['dtus'].min()
    #print( df1.loc[df1['dtus']!=0]['dtus'].min())
    #print( df1['dtus'].min())


    # SOME print("... ?", flush = True)
    if df_stat.iloc[-1]['min_dtus'] != df1['dtus'].min():
        print(f"... ? minimum dtus is not the same {df1['dtus'].min()}", flush = True)
        if len(df1.loc[ df1['dtus']==0] )!=1:
            print("X... some error in creation of dtus - i need to debug it")
            sys.exit(1)
    df_stat['Npu'] = pileups_ch

    print(" ... stat done")



    print("\n\n")
    tbar.print_to( (70,1),  f'{bg.yellow} stat done {bg.default}' )
    #tbar.place()


    tbar.print_to( (70,1),  f'{bg.yellow} saving histo {bg.default}' )

    #------------- histogram with time erlang---------------------------------
    bname = os.path.splitext(filename)[0]  #basename
    # hname = bname.split("_")[-1]  # last thing should be a comment
    #*************
    hname = general.generate_hname(filename, chan)+"_erlang"
    outfile = bname+"erlang_ch"+str(chan)+".txt"
    his = general.column_to_histo(df1['dtus'], binmax=1000, himax=1+int(df1["dtus"].max()),
                                  savename = outfile,
                                  hname = hname, writeondisk = True, writetxt = False)


    #*************
    hname = general.generate_hname(filename, chan)+"_erlang2"
    outfile = bname+"erlang2_ch"+str(chan)+".txt"
    his = general.column_to_histo(df1['dtus'], binmax=1000, himax=100,
                                  savename = outfile,
                                  hname = hname, writeondisk = True, writetxt = False)



    #--------------- histogram zeros in time
    #*************
    hname = general.generate_hname(filename, chan)+"_zerotime"
    outfile = bname+"zerotime_ch"+str(chan)+".txt"
    his = general.column_to_histo(  df1.loc[ (df1.E==0)  ]["time"]  ,
                                    binmax=1+int(df1.iloc[-1]["time"]),
                                    himax=1+int(df1.iloc[-1]["time"]),
                                    savename = outfile,
                                    hname = hname, writeondisk = True, writetxt = False)


    #--------------- histogram nonzeroes in time
    #*************
    hname = general.generate_hname(filename, chan)+"_nzerotime"
    outfile = bname+"nzerotime_ch"+str(chan)+".txt"
    his = general.column_to_histo(  df1["time"].loc[ (df1.E!=0)  ]  ,
                                    binmax=1+int(df1.iloc[-1]["time"]),
                                    himax=1+int(df1.iloc[-1]["time"]),
                                    savename = outfile,
                                    hname = hname, writeondisk = True, writetxt = False)


    if 'extras' in  df1:
        #--------------- histogram saturations distribution in time
        #*************
        hname = general.generate_hname(filename, chan)+"_saturations"
        outfile = bname+"saturations_ch"+str(chan)+".txt"
        his = general.column_to_histo(  df1["time"].loc[ (df1.prev_satu!=0)  ]  ,
                                        binmax=1+int(df1.iloc[-1]["time"]),
                                        himax=1+int(df1.iloc[-1]["time"]),
                                        savename = outfile,
                                        hname = hname, writeondisk = True, writetxt = False)


        #--------------- histogram saturations length
        #*************
        hname = general.generate_hname(filename, chan)+"_satlength"
        outfile = bname+"satlength_ch"+str(chan)+".txt"
        his = general.column_to_histo(  df1["prev_satu"].loc[ (df1.prev_satu!=0)  ]  ,
                                        binmax=100,
                                        himax=1+int(df1["prev_satu"].max()),
                                        savename = outfile,
                                        hname = hname, writeondisk = True, writetxt = False)



    tbar.print_to( (70,1),  f'{bg.yellow} histograms saved {bg.default}' )
    #tbar.place()


    #*************   one channel; time span
    #
    #


    print("D... DETECTION of zeroes..............")
    tbar.print_to( (70,1),  f'{bg.yellow} detect zeroes {bg.default}' )
    len_zeroes,len_dzeroes,len_szeroes,len_izeroes,len_stazeroes,zoutput = general.pd_detect_zeroes(df1, chan, TIMEWIN_US=TIMEWIN_US) # df1[ (df1.E==0) ]




    print()
    print(f"D...  selecting nonzero events for  channel {chan} ")
    print(f"D...  selecting nonzero events for  channel {chan} ")
    print(f"D...  selecting nonzero events for  channel {chan} ")
    print()

    df2 = df1[ df1.E!=0 ]
    df2.reset_index(inplace=True, drop=True)


    print()
#    print("i... ZEROES == ", len(dfzero))
#    print("i... EVENTS == ", len(df2))

    # deadtpr = len_zeroes/len(df2) * 100# ????
    deadtpr = len_zeroes/len(df1) * 100

    fev = df1.time.iloc[0]
    lev = df1.time.iloc[-1]
#    print(f"i... DT %   == {deadtpr:.2f}")
    # print(f"i... events == {fev} ... {lev}")
    # print(f"i... times  == {fev:.2f} ... {lev:.2f}")
    dift = lev - fev  # difference of times
    deadt = dift*deadtpr/100
    livet = dift - deadt

    if Tsatu_ch == None:
        livetprsat = None
        deadtprsat = None
    else:
        livetprsat = (dift - deadt - Tsatu_ch)
        deadtprsat = (dift - livetprsat)/dift*100

        deadtprsatonly = Tsatu_ch/dift*100


    stopcut = start + dt.timedelta(seconds=lev)

    tot_evts = len(df1)
    rate = tot_evts/dift # divided by total time

    blind_time = float(df_stat['min_dtus']*1e-6*tot_evts)  # time
    deadtprsatbli = deadtprsat + blind_time/dift*100  #% + %

    blind_erlang = erlang.erlang_cum(float(df_stat['min_dtus'])*1e-6, rate, 1)*100  # in %
    wind_erlang = erlang.erlang_cum(float(TIMEWIN_US)*1e-6, rate, 1)*100  # in %
    # I have 2 time information:
    # df_stat['min_dtus']
    # TIMEWIN_US


    # ???? I dont know ????
    deadtprsatblier = deadtprsat + blind_erlang # %+%

    median_time = 0.693/rate # m.distance to next event (k=1) # in second
    nevents = 2
    med_triple_rate = nevents/rate*(1 - 1/(3*nevents+0.2) ) #  dista
    median_time3= med_triple_rate # is seconds (median distance of 3rd event k=2)


    # with open("stat.log", "a") as f:
    #     f.write( f"{filename} {rate:7.1f} {deadtpr:6.3f} {startcut} {stopcut} {TIMEWIN_US:6.2f} {len_zeroes:8d} {len_dzeroes:8d} {len_szeroes:8d} {len_izeroes:8d} {len_stazeroes:8d}\n" )


    df_stat['Tblind'] = blind_time
    df_stat['bliER%'] = blind_erlang # in %
    df_stat['DtSBl%'] = deadtprsatbli
    df_stat['DtSBlE%'] = deadtprsatblier



    df_stat['Z'] = len_zeroes
    df_stat['Zd'] = len_dzeroes
    df_stat['Zs'] = len_szeroes
    df_stat['Zi'] = len_izeroes
    df_stat['Zsta'] = len_stazeroes

    output = f"""
     file   == {filename}
    channel == {chan}
     rate   == {rate:7.1f} cps
     times  == {fev:7.2f} ... {lev:7.2f}
     real T == {dift:7.2f} s

     live T == {livet:7.2f} s            (CAEN zeroes/total)
     dead T == {deadt:7.2f} s   {deadtpr:6.3f} % (CAEN zeroes/total)
     start  == {start}
     CUTsta == {startcut}
     CUTsto == {stopcut}


   med time == {median_time*1000000:7.1f} us  (median between 2 events from erlang)
   med tim3 == {median_time3*1000000:7.1f} us  (median between 3 events from erlang)

blind time  == {blind_time:7.3f} sec      (simple estimate = min.time*total events)
blind timEr == {blind_erlang:7.3f} %     (Erlang estimate for t<min_dtus)
wind_timeEr == {wind_erlang:7.3f} %      (Erlang for t <  {TIMEWIN_US:6.2f})
dblzero_ERL == {wind_erlang-blind_erlang:7.3f}   (check if consistent to dbl zeroes ?!?!)


     zeroes       = {len_zeroes:8d}   (standalone = {len_stazeroes:8d})
     nonz events  = {len(df2):8d}
     tot events   = {len(df1):8d}
     saturations  = {Tsatu_ch:8.3f} s    (n= {satu_n_ch} )
"""




    output+=f"""

   DEADTIMES SUMMARY ------ with all considerations:
     DT(saturation) = {deadtprsatonly:6.3f} %
     DT(BlindSimpl) = {blind_time/dift*100:6.3f} %
     DT(BlinErlang) = {blind_erlang:6.3f} %
___________________
     DT             = {deadtpr+blind_erlang+deadtprsatonly:7.3f} %
     Live T         = {(100 -deadtpr-blind_erlang-deadtprsatonly)*0.01*dift:7.1f} s
     Dead T         = {(deadtpr+blind_erlang+deadtprsatonly)*0.01*dift:7.1f} s
 __________________
"""



    output = output + zoutput

    tbar.print_to( (70,1),  f'{bg.yellow} Final statistics {bg.default}' )


    print(output)

    df_stat['rate'] =  rate
    df_stat['DT%'] = deadtpr
    #df_stat['DT+S%'] = deadtprsat

    df_stat['Treal'] =dift
    df_stat['Tlive'] = livet
    df_stat['Tdead'] = deadt
    df_stat['Nzero'] = len_zeroes
    df_stat['sum_dsi'] = len_dzeroes+len_szeroes+len_izeroes
    df_stat['Ntot'] = len(df1)

#     if satu_n_ch != None:
#         df_stat['DtSaAvg%'] = 100*( (1/rate) * satu_n_ch )/dift   #  average dt * nsatur
#         df_stat['DtSaMin%'] = 100*( df_stat['min_dtus']*1e-6 * satu_n_ch )/dift  #  mintime * nsatur
# #    else:
# #        df_stat['iDTavg%'] = None
# #        df_stat['iDTmin%'] = None
#     #    df_stat['tSAT'] =



#    df_stat = df_stat.round( decimals = 2 )
    df_stat = df_stat.round( decimals = 2 )

    print( tabulate(df_stat, headers='keys',showindex="never"))#, tablefmt='psql'

    logexists = False
    if os.path.exists( "stat.log" ): logexists = True
    df_stat.to_csv( "stat.log", mode="a" , sep="\t", index = False, header = not(logexists) )
    print()

    outinfo = os.path.splitext(filename)[0]+f"_ch{chan}{od_do_name}_{TIMEWIN_US}.info"
    print(f"D... creating info FILE {outinfo}")
    with open(outinfo,"w") as f:
        f.write(output)



    bname = os.path.splitext(filename)[0]  #basename
    # hname = bname.split("_")[-1]  # last thing should be a comment
    #*************

    tbar.print_to( (70,1),  f'{bg.yellow} saving txt cut {bg.default}' )


    hname = general.generate_hname(filename, chan)

    outfile = bname+f"_ch{chan}{od_do_name}.txt"
    #*************
    his = general.column_to_histo(df2['E'],
                                  savename = outfile,
                                  hname = hname, writeondisk = True)

    #outfile2 = bname+".asc1"
    #print(f"D... {outfile2} is save as a duplicate")
    #copyfile(outfile, outfile2)

    print( general.freemem() )


    if tree:
        #*************
        tbar.print_to( (70,1),  f'{bg.yellow} saving tree {bg.default}' )

        general.save_to_tree(df1, filename, treename = f"df{chan}") # no modname...

    print( general.freemem() )




    print( f"{fg.green}VERIFY:\n{fg.default}")
    print( f"{fg.green}Erlang prediction for double zeroes % == really double zeroes %\n{wind_erlang-blind_erlang:7.3f} % ==  {2*len_dzeroes/len(df1)*100:5.2f}%  \n" )

    print("")
    print( f"{fg.green} ALL LOW NUMBERS (single,ilogic,standalone zeroes) :  {fg.default}")
    print( f"{fg.green} {len_szeroes/len(df1)*100:7.3f}% {len_izeroes/len(df1)*100:7.3f}% {len_stazeroes/len(df1)*100:7.3f}% {fg.default}")
    print()


    tbar.print_to( (70,1),  f'{bg.yellow} DONE {bg.default}' )

    time.sleep(0.4)
    timer.cancel()
    tbar.place()





    return






if __name__=="__main__":
    print("D... fastread can be called too, from bin_readvme")
    Fire(eva_cut_time)
