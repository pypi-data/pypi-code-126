import pandas as pd
import numpy as np
import talib
from scipy.stats import linregress
import pandas_ta as ta
from lightgbm import LGBMClassifier

SISS_MANDATORY_COLUMNS = ['adj_close', 'adj_high', 'adj_low', 'popularity', 'sentiment']

def siss_check_columns_name(dataset:pd.DataFrame)->bool:
    list_cols = dataset.columns
    return set(SISS_MANDATORY_COLUMNS).issubset(list_cols)

def get_slope(array):
    y = np.array(array)
    x = np.arange(len(y))
    slope, intercept, r_value, p_value, std_err = linregress(x,y)
    return slope

def SiSS(stock, backrollingN)->pd.DataFrame:
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


TI_SISS_MANDATORY_COLUMNS = ['adj_close', 'popularity', 'sentiment', 'Trend_Predictions']

def ti_siss_check_columns_name(dataset:pd.DataFrame)->bool:
    list_cols = dataset.columns
    return set(TI_SISS_MANDATORY_COLUMNS).issubset(list_cols)

def get_slope(array):
    y = np.array(array)
    x = np.arange(len(y))
    slope, intercept, r_value, p_value, std_err = linregress(x,y)
    return slope

def TI_SiSS(stock, backrollingN)->pd.DataFrame:
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


MANDATORY_COLUMNS = ['adj_close', 'adj_high', 'adj_low']

def check_columns_name(dataset:pd.DataFrame)->bool:
    list_cols = dataset.columns
    return set(MANDATORY_COLUMNS).issubset(list_cols)

# UPWARD TREND = 2
# LATERAL PHASE  = 1
# DOWNWARD TREND = 0
def labeling(x):
    out = None
    if ((x is not None) and  (x > 0)):
        out = 2
    elif ((x is not None) and  (x < 0)):
        out = 0
    elif ((x is not None) and (x == 0)):
        out = 1
    return out
    

def Trend_Indicator(dataset:pd.DataFrame, Donchian_periods:int, test_percentage:float):
    dataset = dataset.copy()
    check = check_columns_name(dataset=dataset)
    if not check:
        raise Exception(f"Dataset is not correct! It must contain the columns called as follows: {MANDATORY_COLUMNS} ")
    else: 
        donchian = ta.donchian(dataset['adj_low'], dataset['adj_high'],lower_length=Donchian_periods, upper_length= Donchian_periods).dropna()
        donchian_up = donchian[f'DCU_{Donchian_periods}_{Donchian_periods}']
        donchian_pct = donchian_up.pct_change()

        donchian_right_size = donchian_up.tolist()
        [donchian_right_size.append(None) for _ in range(Donchian_periods-1)]
        dataset['Donchian channel'] = donchian_right_size

        donchian_pct_right_size = donchian_pct.tolist()
        [donchian_pct_right_size.append(None) for _ in range(Donchian_periods-1)]
        dataset['Donchian change'] = donchian_pct_right_size

        Labels = dataset["Donchian change"].apply(labeling).dropna()

        dataset = dataset.dropna()
        del dataset["adj_high"]
        del dataset["adj_low"]
        del dataset["Donchian channel"]
        del dataset["Donchian change"]
        

        LGBM_model = LGBMClassifier(objective='softmax', n_estimators=300, random_state=123, learning_rate=0.3)
        test_size = int(len(dataset['adj_close'])*test_percentage)

        Y = Labels
        X = dataset

        test_predictions = []

        for i in range(test_size):
            x_train = X[:(-test_size+i)]
            y_train = Y[:(-test_size+i)]
            x_test = X[(-test_size+i):]

            LGBM_model.fit(x_train,y_train)
            pred_test = LGBM_model.predict(x_test)
            test_predictions.append(pred_test[0])

        array_of_predictions = []
        [array_of_predictions.append(None) for _ in range(len(X[:(-test_size)]))]
        array_of_predictions.extend(test_predictions)

        dataset['Trend_Predictions'] = array_of_predictions

    return dataset, LGBM_model


MANDATORY_COLUMNS = ['adj_close', 'adj_high', 'adj_low']

def check_columns_name(dataset:pd.DataFrame)->bool:
    list_cols = dataset.columns
    return set(MANDATORY_COLUMNS).issubset(list_cols)

# UPWARD TREND = 2
# LATERAL PHASE  = 1
# DOWNWARD TREND = 0
def labeling(x):
    out = None
    if ((x is not None) and  (x > 0)):
        out = 2
    elif ((x is not None) and  (x < 0)):
        out = 0
    elif ((x is not None) and (x == 0)):
        out = 1
    return out

def Trend_Indicator_for_MultIndex(dataset:pd.DataFrame, Donchian_periods:int, test_percentage:float):
    dataset = dataset.copy()
    check = check_columns_name(dataset=dataset)
    if not check:
        raise Exception(f"Dataset is not correct! It must contain the columns called as follows: {MANDATORY_COLUMNS} ")
    else:
        for figi in dataset.index.get_level_values(0).unique():
            donchian = ta.donchian(dataset.loc[(figi, slice(None)), 'adj_low'], dataset.loc[(figi, slice(None)), 'adj_high'],lower_length=Donchian_periods, upper_length= Donchian_periods).dropna()
            donchian_up = donchian[f'DCU_{Donchian_periods}_{Donchian_periods}']
            donchian_pct = donchian_up.pct_change()

            donchian_right_size = donchian_up.tolist()
            [donchian_right_size.append(None) for _ in range(Donchian_periods-1)]
            dataset.loc[(figi, slice(None)), 'Donchian channel'] = donchian_right_size

            donchian_pct_right_size = donchian_pct.tolist()
            [donchian_pct_right_size.append(None) for _ in range(Donchian_periods-1)]
            dataset.loc[(figi, slice(None)), 'Donchian change'] = donchian_pct_right_size

            dataset.loc[(figi, slice(None)), "Labels"] = dataset.loc[(figi, slice(None)), "Donchian change"].apply(labeling).dropna()

        dataset = dataset.dropna()
        del dataset["adj_high"]
        del dataset["adj_low"]
        del dataset["Donchian channel"]
        del dataset["Donchian change"]

        df_for_train = dataset.copy()
        del df_for_train["Labels"]

        LGBM_model = LGBMClassifier(objective='softmax', n_estimators=300, random_state=123, learning_rate=0.3)
        for num, figii in enumerate(dataset.index.get_level_values(0).unique()):
            test_size = int(len(dataset.loc[(figii,slice(None)), 'adj_close'])*0.2)

            Y = dataset.loc[(figii,slice(None)), 'Labels']
            X = df_for_train.loc[(figii,slice(None))]

            test_predictions = []

            for i in range(test_size):
                x_train = X[:(-test_size+i)]
                y_train = Y[:(-test_size+i)]
                x_test = X[(-test_size+i):]

                LGBM_model.fit(x_train,y_train)
                pred_test = LGBM_model.predict(x_test)
                test_predictions.append(pred_test[0])

            array_of_predictions = []
            [array_of_predictions.append(None) for _ in range(len(X[:(-test_size)]))]
            array_of_predictions.extend(test_predictions)

            dataset.loc[(figii,slice(None)), 'Trend_Predictions'] = array_of_predictions

    return dataset, LGBM_model