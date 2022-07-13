#AlgoFnO Library for Delivery Data and Derivative Data Analysis

#=============================================================================================

import csv
import os
import glob
import pandas as pd

#=============================================================================================

class insertData:

#=============================================================================================

    def insertCM(self,folder,ticker):
        location = folder+'/'+"cm*.csv"
        files = os.path.join(location)
        files = glob.glob(files)
        df = pd.concat(map(pd.read_csv, files), ignore_index=True)
        df =df.loc[df['SYMBOL']==ticker]
        return df

#=============================================================================================

    def insertFO(self,folder,ticker):

        location = folder+'/'+"fo*.csv"
        files = os.path.join(location)
        files = glob.glob(files)
        df = pd.concat(map(pd.read_csv, files), ignore_index=True)
        df = df.loc[df['SYMBOL']==ticker]
        df = df.loc[df['INSTRUMENT']=='FUTSTK']
        df = df.groupby(['TIMESTAMP']).sum()
        return df

#=============================================================================================

class BhavCopyAnalysis:

#=============================================================================================

    def doAnalysis(self,folder,tickerList):
        for ticker in tickerList:
            insertDataObject = insertData()

            dataFrameCM = insertDataObject.insertCM(folder,ticker)
            dataFrameFO = insertDataObject.insertFO(folder,ticker)

            result = pd.merge(dataFrameCM, dataFrameFO, on='TIMESTAMP', how='outer')

            result['%_OI_change'] = (result['CHG_IN_OI'] / result['OPEN_INT'])*100
            result['Quantity/Trades'] = (result['TOTTRDQTY'] / result['TOTALTRADES'])*100
            result['%_Price_change'] = ((result['CLOSE_x']-result['PREVCLOSE']) / result['PREVCLOSE'])*100

            cols = [1,6,12,13,14,15,16,17,18,19,20,21]
            result.drop(result.columns[cols],axis=1,inplace=True)

            result = result.sort_values(by=['TIMESTAMP'], ascending=False)

            location = folder + '/FnOAnalysisFor_' + ticker + '.csv'
            result.to_csv(location)

#=============================================================================================
