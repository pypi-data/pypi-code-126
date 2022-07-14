from distutils.command.install_egg_info import safe_name
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
import os
from sklearn.model_selection import train_test_split
import glob
import openpyxl

def learn(division,num,mode):

    return_pref_str = str

    pref_dict = {"./weather/miyagi.csv":4,"./weather/saitama.csv":11,"./weather/chiba.csv":12,"./weather/tokyo.csv":13,"./weather/kanagawa.csv":14,"./weather/aichi.csv":23,"./weather/kyoto.csv":26,"./weather/osaka.csv":27,"./weather/hiroshima.csv":34,"./weather/fukuoka.csv":40}
    #熱中症データを結合
    
    
    files = glob.glob("./heatstroke_data/*")
    df_heat = pd.DataFrame()
    for file in files:
        sheets = pd.read_excel(file,sheet_name=None,engine='openpyxl')
        for sheet in sheets:
            df_heat = df_heat.append(sheets[sheet])
    df_heat['date'] = pd.to_datetime(df_heat['日付'])
    df_heat['year'] = df_heat['date'].dt.year
    df_heat['month'] = df_heat['date'].dt.month
    df_heat['day'] = df_heat['date'].dt.day

    df_heat = df_heat.loc[:,['都道府県コード','搬送人員（計）','year','month','day']]


    #対象都道府県の熱中症データを抜き出す
    code_list = []
    cnt = 0
    target_pref_code_index = num
    for file in pref_dict:

        cnt += 1
        if mode == 1:
            if cnt != target_pref_code_index:
                continue
        code_list.append(pref_dict[file])
        
        if cnt == target_pref_code_index:
            if mode == 1:
                return_pref_str = file[18:]
            break

    df_heat = df_heat[df_heat['都道府県コード'].isin(code_list)]


    #気象データを加工
    files = glob.glob("./weather/*")
    df_temp = pd.DataFrame()


    for file in files:
        #都道府県コードを代入
        tmp_df = pd.read_csv(file)
        tmp_df['都道府県コード'] = pref_dict[file]
        
        #整数値へ変換
        tmp_df = tmp_df.round()
        
        #欠損値を修正
        mean_humidity=round(tmp_df['humidity'].mean())
        tmp_df['humidity']= tmp_df['humidity'].fillna(mean_humidity)

        mean_sun = round(tmp_df['sun'].mean())
        tmp_df['sun'] = tmp_df['sun'].fillna(mean_sun)

        mean_wind = round(tmp_df['wind'].mean())
        tmp_df['wind'] = tmp_df['wind'].fillna(mean_wind)

        #データ型変換
        tmp_df = tmp_df.astype('int64')

        #都道府県データを追加
        df_temp = df_temp.append(tmp_df)

        
    #熱中症データと気温データを統合
    df_total = pd.merge(df_heat,df_temp)

    #人口データ追加(オプション)
    df_population = pd.read_excel('population.xlsx',engine='openpyxl')
    df_total = pd.merge(df_total,df_population)

    #不必要データをドロップ
    df_total = df_total.drop(['都道府県コード','year','month','day'],axis=1)
    df_total['搬送人員（計）'].fillna(0,inplace=True)
    df_total['target_division'] = round(df_total['搬送人員（計）'] / division)
    print(df_total['target_division'].isnull().sum())
    
    df_total['target_division'] = df_total['target_division'].astype('int64')

    #df_total.to_excel('fixed_data.xlsx')

    target = df_total['target_division']
    
    data=df_total.drop(['搬送人員（計）','target_division'],axis=1)

    data.info()
    target.info()

    X_train,X_test,y_train,y_test=train_test_split(data,target,test_size=0.1,random_state=54,shuffle=True)
    
    rfr = RandomForestRegressor(n_estimators=500, max_depth=None,min_samples_split=2,random_state=8)
    rfr.fit(X_train,y_train)

    pred = rfr.predict(X_test)
    score = rfr.score(X_test,y_test)
    print ("score:{}".format(score))
    dic = dict(zip(data.columns,rfr.feature_importances_))
    for item in dic.items():
        print(item[0],round(item[1],4))
    
    y_list = y_test.tolist()
    for i in range(100):
        c = y_list[i]
        p = pred[i]
        print('[{0}] correct:{1:.3f}, predict:{2:.3f} ({3:.3f})'.format(i, c, p, c-p))
    

def basic_learn():
    learn(1,10,0)

def main():
    basic_learn()

if __name__ == "__main__":

    main()
    
