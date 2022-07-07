

def ChurnPrediction(file):
    import pandas as pd
    import numpy as np

    import seaborn as sns
    import fileinput
    import pathlib
    import os
    import os.path
    import sys
    import sklearn.utils._cython_blas
    import sklearn.utils._vector_sentinel
    import sklearn.tree  
    import sklearn.tree._utils
    df = pd.read_csv(file,dtype={'TotalCharges':float})
    path=pathlib.Path(file).parent.resolve()
    print("we are loading given file\n ")
    co=len(df.columns)
    print(str(co)+" features loaded\n ")




    df.columns = df.columns.str.lower().str.replace(' ', '_')

    string_columns = list(df.dtypes[df.dtypes == 'object'].index)

    for col in string_columns:
        df[col] = df[col].str.lower().str.replace(' ', '_')

    mask = df['churn'].isnull()
    df2= (df[mask])
    df2 = df2.drop(columns='churn')
    total=len(df2)
    df=df.dropna(axis=0, how='all', subset=['churn'])


    df.churn = (df.churn == 'yes').astype(int)

    print("working on data\n ")

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



    print("generating prediction file\n ")

    test_dict = df2[categorical + numerical].to_dict(orient='records')
    X_test = dv.transform(test_dict)
    y_testpred= model.predict_proba(X_test)[:, 1]
    churn = y_testpred > 0.5


    df3 = pd.DataFrame(y_testpred,columns=['churn score'])
    df4= pd.DataFrame(churn,columns=['churned'])
    churning= (df4['churned']==1).sum()

    df3[c] = df[c]


    df3.to_csv(os.path.join(path, 'prediction.csv'))

    print("you prediction file is stored in the same folder as of python file\n ")
    print("out of "+str(total)+" customers,"+str(churning)+" customers are expected to churn\n ")

    return 0

