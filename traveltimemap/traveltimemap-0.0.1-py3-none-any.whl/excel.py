import pandas as pd
import numpy as np
import openpyxl

#read multiple excel sheets
def read_excel(df):
    data = pd.read_excel(df, sheet_name=None)
    return data

#single DataFrame
def combine_data(df):
    data = read_excel(df)
    data = pd.concat(data, ignore_index=True)
    return data

#convert to csv
def convert_to_csv(df):
    data = combine_data(df)
    data.to_csv('data.csv')
    return data

