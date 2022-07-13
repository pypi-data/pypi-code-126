import pandas as pd
import datetime

# Helper Functions

def _choose_cols(df, colmap):
    cols = list(colmap.keys())
    return df.loc[:, cols]

def _query(c):
    name, op, value = c
    #if op == "NOT LIKE":
    #if isinstance(value, datetime.date): value = '20220101'
    expr = f'{name} {op} {repr(value)}'
    print(expr)
    return expr

def _filter(df, conds, ands=True):
    sep = " AND " if ands else " OR "
    exprs = [_query(c) for c in conds]
    q = sep.join(exprs)
    return df.query(q)

# DAD Functions

def load(vm, da):
    # Assume columns + data
    df = pd.DataFrame(data=da.data, columns=da.columns)
    return df

def select(vm, da):
    df = vm.get(da.from_key)
    if da.cols: df = _choose_cols(df, da.cols)
    if da.where_all: df = _filter(df, da.where_all, True)
    if da.where_any: df = _filter(df, da.where_any, False)
    return df
