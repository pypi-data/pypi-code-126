import pandas as pd
import sqlite3
import os
def import_data(datapath,databasepath,is_op,ft,ed):
    if(is_op == 0):
        ft_ = ''
        ed_ = ''
    else:
        ft_ = ft
        ed_ = ed
    conn = sqlite3.connect(databasepath)
    folder_name = datapath    #获取文件夹的名字，即路径
    file_names = os.listdir(folder_name)   #获取文件夹内所有文件的名字
    for name in file_names: 
        old_name = folder_name  + name   
        df = pd.read_csv(old_name)
        df.to_sql(ft + name + ed, conn, if_exists = 'append', index=False)
    
    conn.close()