import pandas as pd
import requests


def get_data(data_set):

   extension = '.csv'
   dir_name =  'https://raw.githubusercontent.com/maker57sk/aimluae/main/datasets/'
   filename = dir_name + data_set + extension

   if requests.get(filename).status_code == 200:
      return pd.read_csv(filename)
   else:
      extension = '.xlsx'
      filename = dir_name + data_set + extension
      return pd.read_excel(filename)





   
 

