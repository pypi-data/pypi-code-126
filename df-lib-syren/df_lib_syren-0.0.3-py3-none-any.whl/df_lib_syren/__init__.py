import pandas as pd
import numpy as np
'''
"""//Step1:Initiating files//"""
source = 'files/file1.csv' #source file path
target = 'files/file2.csv' #target file path
'''
def syr_compareDF(source_file,target_file):
    source = source_file
    target = target_file
    """//Step2:Loading files based on the format//"""
    df_scr = pd.read_csv(source)
    df_tar = pd.read_csv(target)
    """//Step3:Instead of using join operations based on SQL, 
    here we are using merge operation between the tables//"""
    df_join = df_scr.merge(right=df_tar,
                           left_on=df_scr.columns.to_list(),
                           right_on=df_tar.columns.to_list(),
                           how='outer', indicator=True)
    print(df_join.head())
    """//Step4:For better interpretation of data frames we are 
    using lambda function to replace the suffix of column names//"""
    df_scr.rename(columns=lambda x: x + '_df1', inplace=True)
    df_tar.rename(columns=lambda x: x + '_df2', inplace=True)
    """//Step5:Merging the data frames with changed names//"""
    df_join2 = df_scr.merge(right=df_tar,
                            left_on=df_scr.columns.to_list(),
                            right_on=df_tar.columns.to_list(),
                            how='outer')
    print(df_join2.head())
    """//Step5: checking the records_present_in_df1_not_in_df2 and vice versa 
    and saving into csv format//"""
    entries_in_df1_not_in_df2 = df_join2.loc[df_join2[df_tar.columns.to_list()]
                                             .isnull().all(axis=1),
                                             df_scr.columns.to_list()]
    entries_in_df2_not_in_df1 = df_join2.loc[df_join2[df_scr.columns.to_list()]
                                             .isnull().all(axis=1),
                                             df_tar.columns.to_list()]
    entries_in_df1_not_in_df2.to_csv('differences_in_df1.csv', index=1)
    entries_in_df2_not_in_df1.to_csv('differences_in_df2.csv', index=1)
    print('Entries found in DF-2', '\n', entries_in_df2_not_in_df1)
    print('Entries found in DF-1', '\n', entries_in_df1_not_in_df2)
    return

