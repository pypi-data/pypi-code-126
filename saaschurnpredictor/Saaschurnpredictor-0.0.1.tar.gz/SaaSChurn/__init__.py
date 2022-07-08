


def ChurnPrediction(df):
    import pandas as pd
    import numpy as np

    import seaborn as sns
    import fileinput
    import pathlib
    import os
    import os.path
    import sys
    import sklearn.tree  
    
    


    y_train = df.churn.values

    b= (df.nunique()==len(df))
    d=[i for i, x in enumerate(b) if x]

    c=b.index[d]
    df1=df.drop(c,axis=1)

    categorical= list(df1.select_dtypes(['object']).columns)
    numerical= [x for x in df1.columns if x not in categorical]
    numerical.remove('churn')

    from sklearn.feature_extraction import DictVectorizer
    train_dict = df[categorical + numerical].to_dict(orient='records')
    dv = DictVectorizer(sparse=False)
    dv.fit(train_dict)

    X_train = dv.transform(train_dict)

    from sklearn.linear_model import LogisticRegression
    model = LogisticRegression(solver='liblinear', random_state=1)
    model.fit(X_train, y_train)
    import pickle



    

    test_dict = df2[categorical + numerical].to_dict(orient='records')
    X_test = dv.transform(test_dict)
    y_testpred= model.predict_proba(X_test)[:, 1]
    


    df3 = pd.DataFrame(y_testpred,columns=['churn score'])
    

    df3[c] = df[c]


    


    return df3

