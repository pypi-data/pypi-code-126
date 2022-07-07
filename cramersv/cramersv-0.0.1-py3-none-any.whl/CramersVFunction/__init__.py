def cramer_correlation_coefficient(data, column_1, column_2):
    """
    Calculates the CramersV correlated statistics for two categorical data
    without encoding the values.
    This function will returns the correlation value for two categorical data and the crosstab of two given data.
    :param data: pandas dataframe
    :param column_1: string or categorical column name
    :param column_2: string or categorical column name
    :return: float
    :return: pandas dataframe or crosstabulation

        E.G --> cramer_correlation_coefficient(data = dataframe, column_1 = 'categorical_column_name', column_2 = 'categorical_column_name')
    """
    import pandas as pd
    import numpy as np
    import scipy.stats as ss

    categorical_column = list(data.select_dtypes(include=['object', 'category']).columns)

    if column_1 in categorical_column and column_2 in categorical_column:
        confusion_matrix = pd.crosstab(data[column_1], data[column_2])
        chi2 = ss.chi2_contingency(confusion_matrix)[0]
        n = confusion_matrix.sum().sum()
        phi2 = chi2/n
        r,k = confusion_matrix.shape
        phi2corr = max(0, phi2 - ((k-1)*(r-1))/(n-1))    
        rcorr = r - ((r-1)**2)/(n-1)
        kcorr = k - ((k-1)**2)/(n-1)
        return np.sqrt(phi2corr / min( (kcorr-1), (rcorr-1))), confusion_matrix

    else:
        print("The given either column is not categorical or the column is not in the dataframe. Please check and try again.")
        return None