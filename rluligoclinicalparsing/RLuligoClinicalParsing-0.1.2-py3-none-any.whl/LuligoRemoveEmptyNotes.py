def LuligoRemoveEmptyNotes(df, columnIndex):
    rows = df[df[df.columns[columnIndex]].isna()].index
    df.drop(rows, inplace=False)
    return df
    #return (3 + df)