# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 18:02:49 2022

@author: RobWen
Version: 0.3.3
"""
# Packages
import requests
import pandas as pd
import numpy as np
from StockHero.Ticker_Sources.morningstar_quote import Morningstar_Quote

class Morningstar_Key_Statistics:
    
    def __init__(self, ticker, headers_standard):
        self.ticker = ticker
        self.headers_standard = headers_standard
        
    def __repr__(self):
        return(self.ticker)
        
    def __str__(self):
        return(self.ticker)
        #return(self.ticker or '') # by None
        
    #####################
    ###               ###
    ###  Morningstar  ###
    ###               ###
    #####################
    
    # Dummy Abfragen
    def morningstar_quote_abfrage_growth_revenue(self):
        
        if self.ticker is None or self.ticker == '':
            self.ticker = 'None'
            return None
        
        return self.morningstar_growth_revenue_df()
    
    def morningstar_quote_abfrage_operating_income(self):
        
        if self.ticker is None or self.ticker == '':
            self.ticker = 'None'
            return None
        
        return self.morningstar_operating_income_df()
    
    def morningstar_quote_abfrage_net_income(self):
        
        if self.ticker is None or self.ticker == '':
            self.ticker = 'None'
            return None
        
        return self.morningstar_net_income_df()
    
    def morningstar_quote_abfrage_growth_eps(self):
        
        if self.ticker is None or self.ticker == '':
            self.ticker = 'None'
            return None
        
        return self.morningstar_growth_eps_df()
    
    def morningstar_growth_revenue_df(self):
        morningstar_performance_id = Morningstar_Quote.morningstar_performance_id(self)
        
        if morningstar_performance_id is None:
            return None
        else:
            url = f'https://api-global.morningstar.com/sal-service/v1/stock/keyStats/growthTable/{morningstar_performance_id}?languageId=en&locale=en&clientId=undefined&component=sal-components-key-stats-growth-table&version=3.71.0'
    
            headers = {
                'ApiKey': 'lstzFDEOhfFNMLikKa0am9mgEKLBl49T',
            }
            
            r = requests.get(url, headers=headers)
            json = r.json()
            
            columns = []
            for i in range(len(json['dataList'])):
                columns.append(json['dataList'][i]['fiscalPeriodYearMonth'])
                
            liste_values = []
            for i in range(len(json['dataList'])):
                liste_values.append(list(json['dataList'][i]['revenuePer'].values()))
                
            array_table = np.array(liste_values).transpose()
            
            morningstar_growth_revenue_df = pd.DataFrame(array_table
                               , index =['Year over Year', '3-Year Average', '5-Year Average', '10-Year Average']
                               , columns = columns
                               )
            
            morningstar_growth_revenue_df = morningstar_growth_revenue_df.fillna(value=np.nan)
        
        return morningstar_growth_revenue_df
    
    def morningstar_operating_income_df(self):
        morningstar_performance_id = Morningstar_Quote.morningstar_performance_id(self)
        
        if morningstar_performance_id is None:
            return None
        else:
            url = f'https://api-global.morningstar.com/sal-service/v1/stock/keyStats/growthTable/{morningstar_performance_id}?languageId=en&locale=en&clientId=undefined&component=sal-components-key-stats-growth-table&version=3.71.0'
    
            headers = {
                'ApiKey': 'lstzFDEOhfFNMLikKa0am9mgEKLBl49T',
            }
            
            r = requests.get(url, headers=headers)
            json = r.json()
            
            columns = []
            for i in range(len(json['dataList'])):
                columns.append(json['dataList'][i]['fiscalPeriodYearMonth'])
                
            liste_values = []
            for i in range(len(json['dataList'])):
                liste_values.append(list(json['dataList'][i]['operatingIncome'].values()))
                
            array_table = np.array(liste_values).transpose()
            
            morningstar_operating_income_df = pd.DataFrame(array_table
                               , index =['Year over Year', '3-Year Average', '5-Year Average', '10-Year Average']
                               , columns = columns
                               )
            
            morningstar_operating_income_df = morningstar_operating_income_df.fillna(value=np.nan)
        
        return morningstar_operating_income_df
    
    def morningstar_net_income_df(self):
        morningstar_performance_id = Morningstar_Quote.morningstar_performance_id(self)
        
        if morningstar_performance_id is None:
            return None
        else:
            url = f'https://api-global.morningstar.com/sal-service/v1/stock/keyStats/growthTable/{morningstar_performance_id}?languageId=en&locale=en&clientId=undefined&component=sal-components-key-stats-growth-table&version=3.71.0'
    
            headers = {
                'ApiKey': 'lstzFDEOhfFNMLikKa0am9mgEKLBl49T',
            }
            
            r = requests.get(url, headers=headers)
            json = r.json()
            
            columns = []
            for i in range(len(json['dataList'])):
                columns.append(json['dataList'][i]['fiscalPeriodYearMonth'])
                
            liste_values = []
            for i in range(len(json['dataList'])):
                liste_values.append(list(json['dataList'][i]['netIncomePer'].values()))
                
            array_table = np.array(liste_values).transpose()
            
            morningstar_net_income_df = pd.DataFrame(array_table
                               , index =['Year over Year', '3-Year Average', '5-Year Average', '10-Year Average']
                               , columns = columns
                               )
            
            morningstar_net_income_df = morningstar_net_income_df.fillna(value=np.nan)
        
        return morningstar_net_income_df
    
    def morningstar_growth_eps_df(self):
        morningstar_performance_id = Morningstar_Quote.morningstar_performance_id(self)
        
        if morningstar_performance_id is None:
            return None
        else:
            url = f'https://api-global.morningstar.com/sal-service/v1/stock/keyStats/growthTable/{morningstar_performance_id}?languageId=en&locale=en&clientId=undefined&component=sal-components-key-stats-growth-table&version=3.71.0'
    
            headers = {
                'ApiKey': 'lstzFDEOhfFNMLikKa0am9mgEKLBl49T',
            }
            
            r = requests.get(url, headers=headers)
            json = r.json()
            
            columns = []
            for i in range(len(json['dataList'])):
                columns.append(json['dataList'][i]['fiscalPeriodYearMonth'])
                
            liste_values = []
            for i in range(len(json['dataList'])):
                liste_values.append(list(json['dataList'][i]['epsPer'].values()))
                
            array_table = np.array(liste_values).transpose()
            
            morningstar_growth_eps_df = pd.DataFrame(array_table
                               , index =['Year over Year', '3-Year Average', '5-Year Average', '10-Year Average']
                               , columns = columns
                               )
            
            morningstar_growth_eps_df = morningstar_growth_eps_df.fillna(value=np.nan)
        
        return morningstar_growth_eps_df

'''

print(json)
print(json['dataList'][0])

len(json['dataList'])
columns_ = []

for i in range(len(json['dataList'])):
    columns_.append(json['dataList'][i]['fiscalPeriodYearMonth'])
    
liste_values = []

for i in range(len(json['dataList'])):
    liste_values.append(list(json['dataList'][i]['epsPer'].values()))

epsPer_0 = json['dataList'][0]['epsPer']
list(epsPer_0.values())

morningstar_growth_eps_df = pd.DataFrame(liste_values
                   , index =['Year over Year', '3-Year Average', '5-Year Average', '10-Year Average']
                   , columns = columns_
                   )

print(morningstar_growth_eps_df)

'''