import pandas as pd
import numpy as np
import talib
from scipy.stats import linregress

SISS_MANDATORY_COLUMNS = ['adj_close', 'adj_high', 'adj_low', 'popularity', 'sentiment']


def SiSS(stock:pd.Dataframe, backrollingN:float)->pd.DataFrame:
    check = siss_check_columns_name(dataset=stock)
    if not check:
        raise Exception(f"Dataset is not correct! It must contain the columns called as follows: {SISS_MANDATORY_COLUMNS} ")
    else:
        stock['popularity_variation'] = stock['popularity'].pct_change()
        stock['sentiment_variation'] = stock['sentiment'].pct_change()
        stock['popularity_variation'] = stock['popularity_variation'].replace(np.inf, 100000000)
        stock['sentiment_variation'] = stock['sentiment_variation'].replace(np.inf, 100000000)
        stock['pop_SMA(7)'] = talib.SMA(stock['popularity'], backrollingN)
        stock['ADX'] = talib.ADX(stock['adj_high'], stock['adj_low'], stock['adj_close'], timeperiod= backrollingN)
        stock['slope_ADX'] = stock['ADX'].rolling(window=backrollingN).apply(get_slope, raw=True)
        stock['Momentum'] = talib.MOM(stock['adj_close'], timeperiod=backrollingN)
        stock['SMA(160)'] = talib.SMA(stock['adj_close'], 160)
        stock['slope_SMA(160)'] = stock['SMA(160)'].rolling(window=backrollingN).apply(get_slope, raw=True)

        stock = stock.dropna()

        stock['entry_long'] = 0
        stock['close_long'] = 0
        stock['positions'] = None

        for i, date in enumerate(stock.index):
            pop_previous_day = stock['popularity'][i-1]
            sum_momentum = stock['Momentum'][i-7:i].sum()

            if ((stock['slope_SMA(160)'][i]>0) and (stock['slope_ADX'][i]>0) and (sum_momentum > 3)):
                # Conditon 1: DPV (summed) of today is greater that the rolling average of the popularity itself
                dpv = stock['popularity'][i]
                sma7 = stock['pop_SMA(7)'][i]
                # Conditon 2: popularity variation greater than 100% with respect to yesterday
                pop_var = ((dpv - pop_previous_day) / abs(pop_previous_day))*100
                # Conditon 3: sentiment of today greater than 0.05
                sent = stock['sentiment'][i]

                # if all the above conditions are true, then I open a long position
                if ((dpv>sma7) and (pop_var>100) and (sent>0.05)):
                    stock['entry_long'][i] = 1
                if ((dpv>sma7) and (pop_var>100) and (sent<(-0.05))):    
                    stock['close_long'][i] = 1

        log_returns = []
        close_long_index = -1
        for g, val in enumerate(stock.index):
            if ((g > 14) and (stock['entry_long'][g] == 1) and (g > close_long_index)):
                open_long_price = stock['adj_close'][g]
                flag_close = False
                for j, elem in enumerate(stock.index[(g+1):]):
                    if (stock['close_long'][g+1+j] == 1):
                        close_long_index = g+1+j
                        close_long_price = stock['adj_close'][close_long_index]
                        flag_close = True 
                        break
                if flag_close:
                    stock['positions'][g] = 1 
                    stock['positions'][g+1+j] = 0  
                    single_trade_log_ret = np.log(close_long_price/open_long_price) 
                    log_returns.append(single_trade_log_ret)

        sum_all_log_ret = sum(log_returns)
        performance = (np.exp(sum_all_log_ret) - 1)*100

    return(performance)