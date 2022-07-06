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

def list_datasets():
   data_sets = [
      'churn', 'courier_companies', 'customs_warehouse_licensees',
      'customs_warehouses', 'declaration_cargo_detail-1', 'declaration_cargo_detail-2', 
      'livebirths', 'new_sales', 'Services-En_0', 'vehicle_clearance_certificate'
   ]

   return print(data_sets )