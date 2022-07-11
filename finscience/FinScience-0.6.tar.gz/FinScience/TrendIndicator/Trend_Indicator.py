import pandas as pd
import pandas_ta as ta
from lightgbm import LGBMClassifier

MANDATORY_COLUMNS = ['adj_close', 'adj_high', 'adj_low']

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

        Target = Labels.shift(-1)
        Y = Target
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