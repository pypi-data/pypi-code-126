import pandas as pd
#test

def get_data(data_set):

   extension = '.csv'
   dir_name =  'https://raw.githubusercontent.com/maker57sk/aimluae/main/datasets/'
   filename = dir_name + data_set + extension

   return pd.read_csv(filename)



   
 

