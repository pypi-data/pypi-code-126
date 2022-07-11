import pandas as pd
import numpy as np
import talib
from scipy.stats import linregress


TI_SISS_MANDATORY_COLUMNS = ['adj_close', 'popularity', 'sentiment', 'company_name', 'Trend_Predictions']

def TI_SiSS(stock: pd.DataFrame, backrollingN: float)->pd.DataFrame:
    check = ti_siss_check_columns_name(dataset=stock)
    if not check:
        raise Exception(f"Dataset is not correct! It must contain the columns called as follows: {TI_SISS_MANDATORY_COLUMNS} ")
    else:
        stock['popularity_variation'] = stock['popularity'].pct_change()
        stock['sentiment_variation'] = stock['sentiment'].pct_change()
        stock['popularity_variation'] = stock['popularity_variation'].replace(np.inf, 100000000)
        stock['sentiment_variation'] = stock['sentiment_variation'].replace(np.inf, 100000000)
        stock['pop_SMA(7)'] = talib.SMA(stock['popularity'], backrollingN)
        stock['SMA(160)'] = talib.SMA(stock['adj_close'], 160)
        stock['slope_SMA(160)'] = stock['SMA(160)'].rolling(window=backrollingN).apply(get_slope, raw=True)

        stock = stock.dropna()

        stock['entry_long'] = 0
        stock['close_long'] = 0
        stock['positions'] = None

        for i, date in enumerate(stock.index):
            pop_giorno_precedente = stock['popularity'][i-1]

            if ((stock['slope_SMA(160)'][i]>0) and (stock['Trend_Predictions'][i] is not None) and (stock['Trend_Predictions'][i]>=1)):
                # Condizione 1: DPV (sommato) di oggi maggiore della media della media mobile della popolarità
                dpv = stock['popularity'][i]
                sma7 = stock['pop_SMA(7)'][i]
                # Condizione 2: variazione di popolarità tra ieri ed oggi maggiore del 100%
                pop_var = ((dpv - pop_giorno_precedente) / abs(pop_giorno_precedente))*100
                # Condizione 3: sentiment di oggi maggiore di 0.05
                sent = stock['sentiment'][i]

                # Se tutte le condizioni sugli indicatori classici avvengono allora apro una posizione long alle seguenti condizioni:
                if ((dpv>sma7) and (pop_var>100) and (sent>0.05)):
                    stock['entry_long'][i] = 1
                if ((dpv>sma7) and (pop_var>100) and (sent<(-0.05))):    
                    stock['close_long'][i] = 1

    log_returns = []
    indice_chiusura_long = -1
    for g, val in enumerate(stock.index):
        if ((g > 14) and (stock['entry_long'][g] == 1) and (g > indice_chiusura_long)):
            open_long_price = stock['adj_close'][g]
            flag_chiusura = False
            for j, elem in enumerate(stock.index[(g+1):]):
                if (stock['close_long'][g+1+j] == 1):
                    indice_chiusura_long = g+1+j
                    close_long_price = stock['adj_close'][indice_chiusura_long]
                    flag_chiusura = True 
                    break
            if flag_chiusura:
                stock['positions'][g] = 1 
                stock['positions'][g+1+j] = 0  
                single_trade_log_ret = np.log(close_long_price/open_long_price) 
                log_returns.append(single_trade_log_ret)

    somma_di_tutti_i_single_log_ret = sum(log_returns)
    performance = (np.exp(somma_di_tutti_i_single_log_ret) - 1)*100

    return(performance)