# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 18:02:49 2022

@author: RobWen
Version: 0.3.3
"""
# Packages
import pandas as pd
import requests
from bs4 import BeautifulSoup
import numpy as np

class Morningstar_Quote:
    
    def __init__(self, ticker, headers_standard):
        self.ticker = ticker
        self.headers_standard = headers_standard
        
    def __repr__(self):
        return(self.ticker)
        
    def __str__(self):
        return(self.ticker)
        #return(self.Morningstar_Key_Ratios or '') # by None
        
    #####################
    ###               ###
    ###  Morningstar  ###
    ###               ###
    #####################
    
    # Dummy Abfrage
    def morningstar_quote_abfrage(self):
        
        ' Dummy Abfrage'
        if self.ticker is None or self.ticker == '':
            self.ticker = 'None'
            return None
        
        return self.morningstar_quote_df()
    
    # Führt eine Abfrage durch um die Performance ID zu finden 
    def morningstar_performance_id(self):
        url = "https://www.morningstar.co.uk/uk/funds/SecuritySearchResults.aspx"
        params = {'search': f'{self.ticker}'}
        
        data = requests.get(url, params=params, headers = self.headers_standard)
        data = BeautifulSoup(data.content, 'html.parser')
        
        try:
            performance_id = data.find('td', {'class':'msDataText searchLink'})
            performance_id = performance_id.prettify().split()[4].split('=')[2].split(']')[0]
        except:
            return None
        
        return performance_id
    
    ### Morningstar Quote                                       ###
    ### e.g. https://www.morningstar.com/stocks/xnas/nvda/quote ###
    ### Rückgabe None implementiert und getestet                ###
    ### Ungültige Werte = NaN implementiert                     ###
    def morningstar_quote_df(self):
        morningstar_performance_id = self.morningstar_performance_id()
        
        if morningstar_performance_id is None:
            return None
        else:
            url = f'https://api-global.morningstar.com/sal-service/v1/stock/header/v2/data/{morningstar_performance_id}/securityInfo?showStarRating=&languageId=en&locale=en&clientId=MDC&benchmarkId=category&component=sal-components-quote&version=3.69.0'
            
            headers = {
                'ApiKey': 'lstzFDEOhfFNMLikKa0am9mgEKLBl49T',
            }
            
            r = requests.get(url, headers=headers)
            dictionary = r.json()
            
            priceEarnings = dictionary["priceEarnings"]
            priceBook = dictionary["priceBook"]
            priceSale = dictionary["priceSale"]
            forwardPE = dictionary["forwardPE"]
            forwardDivYield = dictionary["forwardDivYield"]
            
            url = f'https://api-global.morningstar.com/sal-service/v1/stock/keyStats/{morningstar_performance_id}?languageId=en&locale=en&clientId=MDC&benchmarkId=category&component=sal-components-quote&version=3.69.0'
            
            headers = {
                'ApiKey': 'lstzFDEOhfFNMLikKa0am9mgEKLBl49T',
            }
            
            r = requests.get(url, headers=headers)
            json = r.json()
            
            revenue3YearGrowth = json['revenue3YearGrowth']['stockValue']
            netIncome3YearGrowth = json['netIncome3YearGrowth']['stockValue']
            operatingMarginTTM = json['operatingMarginTTM']['stockValue']
            netMarginTTM = json['netMarginTTM']['stockValue']
            roaTTM = json['roaTTM']['stockValue']
            roeTTM = json['roeTTM']['stockValue']
            freeCashFlowTTM = json['freeCashFlow']['cashFlowTTM']
            
            try:
                priceEarnings = '{:.2f}'.format(float(priceEarnings))
                priceBook = '{:.2f}'.format(float(priceBook))
                priceSale = '{:.2f}'.format(float(priceSale))
                forwardPE = '{:.2f}'.format(float(forwardPE))
                forwardDivYield = float(forwardDivYield) * 100 # in %
                revenue3YearGrowth = '{:.2f}'.format(float(revenue3YearGrowth))
                netIncome3YearGrowth = '{:.2f}'.format(float(netIncome3YearGrowth))
                operatingMarginTTM = '{:.2f}'.format(float(operatingMarginTTM))
                netMarginTTM = '{:.2f}'.format(float(netMarginTTM))
                roaTTM = '{:.2f}'.format(float(roaTTM))
                roeTTM = '{:.2f}'.format(float(roeTTM))
                freeCashFlowTTM = '{:,.2f}'.format(float(freeCashFlowTTM)) # locale='en_US'
            except(TypeError):
                pass
            
            df_morningstar_quote = pd.DataFrame([priceEarnings, priceBook, priceSale, forwardPE, forwardDivYield
                               , revenue3YearGrowth, netIncome3YearGrowth, operatingMarginTTM, netMarginTTM, roaTTM, roeTTM
                               , freeCashFlowTTM]
                              , index =['Price/Earnings', 'Price/Book', 'Price/Sales', 'Consensus Forward P/E', 'Forward Div Yield %'
                                        , 'Rev 3-Yr Growth', 'Net Income 3-Yr Growth'
                                        , 'Operating Margin % TTM', 'Net Margin % TTM', 'ROA % TTM'
                                        , 'ROE % TTM', 'Current Free Cash Flow']
                              , columns =[self.ticker + ' Ratio'])
            
            df_morningstar_quote = df_morningstar_quote.fillna(value=np.nan) # None mit NaN ersetzen für df
        
        return df_morningstar_quote