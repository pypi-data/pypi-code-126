import pandas as pd
import requests



def get_data(data_set):

   extension = '.csv'
   dir_name =  'https://raw.githubusercontent.com/aimluae/uaedata/main/datasets/'
   filename = dir_name + data_set + extension

   if requests.get(filename).status_code == 200:
      df = pd.read_csv(filename)
      return print(df.head())
   else:
      extension = '.xlsx'
      filename = dir_name + data_set + extension
      df = pd.read_excel(filename)
      return print(df.head())

def list_datasets():
   data_sets = [
      'courier_companies', 'customs_warehouse_licensees', 'Number of teaching staff_in_Higher_Education_2020_06_09', 
      'customs_warehouses', 'declaration_cargo_detail-1', 'declaration_cargo_detail-2', 'Graduates_in_Highe_ Education_20-06-09',
      'livebirths', 'Services-En_0', 'vehicle_clearance_certificate', 'UAE_National_Red List_Species',
   ]
   return data_sets


get_data('customs_warehouse_licensees')