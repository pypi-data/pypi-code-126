

import sqlite3
import os 
import pandas as pd

def selectdata(databasepath, export_path, f_or_ot, add_or_rpl):
    conn = sqlite3.connect(databasepath)
    cursor = conn.cursor()
    table_name = input("table_name:")
    column_conditions = input("column_conditions:")
    row_conditions = input("row_conditions:")
    sqlcode = 'select ' + column_conditions + ' from ' + table_name + ' where ' + row_conditions
    cursor.execute(sqlcode)
    result1 = cursor.fetchall()
    list1 = column_conditions.split(',')
    if(f_or_ot == 'f'):
        df = pd.DataFrame(result1, columns=list1)
        if(add_or_rpl == 'add'):
          df.to_csv(export_path, index=0 ,mode='a')
        else:
          df.to_csv(export_path, index=0 )
    else:
        return result1
    cursor.close()
    conn.commit()
    conn.close()

#cursor.execute('create table 600036.SH (trade_date varchar(20) primary key)')                                                      
#cursor.execute('insert into user (id, name) values("kevin", "001")')
# databasepathname = 'D:\\database\\astockver1\\'
# databasename = 'database_for_astockver1.db'
# export_path = 'D:\\database\\astockver1\\export_data\\'

