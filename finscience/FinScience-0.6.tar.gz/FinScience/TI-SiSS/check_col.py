def siss_check_columns_name(dataset:pd.DataFrame)->bool:
    list_cols = dataset.columns
    return set(SISS_MANDATORY_COLUMNS).issubset(list_cols)