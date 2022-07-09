def categorical_data_encoding(data, column, method='one_hot'):
    """This function encodes the categorical data.By default it uses one-hot encoding.
    Args:data: pandas dataframe
         column: column name. It needs to be a list and categorical column
         method: one_hot or label_encoding
    Returns: pandas dataframe with encoded categorical data.

    We encode the categorical data because many algorithms are not able to handle the categorical data.
    """

    import pandas as pd
    from sklearn.preprocessing import OrdinalEncoder

    if type(data) == pd.core.frame.DataFrame:
        if data.isna().sum().sum() == 0:
            data_column = list(data.columns)
            if type(column) == list:
                available_column = []
                for i in column:
                    if i in data_column:
                        available_column.append(i)
                if available_column:
                    if method == 'one_hot':
                        result = pd.get_dummies(data[available_column], prefix=available_column, prefix_sep='_', drop_first=True)
                        return result
                    elif method == 'ordinal' and len(available_column) > 1:
                        encode = OrdinalEncoder()
                        value = encode.fit_transform(data[available_column])
                        result = pd.DataFrame(value, columns=available_column)
                        return result
                    elif method == 'ordinal' and len(available_column) == 1:
                        encode = OrdinalEncoder()
                        value = encode.fit_transform(data[available_column])
                        result = pd.DataFrame(value, columns=[available_column])
                        return result
                    else:
                        result = "The input given to the function is incorrect. Please give valid input and try again."
                        return result
                else:
                    print("Some given columns are not present in the given dataframe")
            else:
                print("The value given to the parameter column should be list.")
        else:
            print("The given dataframe consist of NA values. Please fill the NA values and try again.")
    else:
        print("The value given to the parameter data is not a dataframe.")   