import pandas as pd
import requests



def get_data(data_set):

   extension = '.csv'
   dir_name =  'https://github.com/aimluae/uaedata/tree/main/datasets/'
   filename = dir_name + data_set + extension

   if requests.get(filename).status_code == 200:
      return pd.read_csv(filename)
   else:
      extension = '.xlsx'
      filename = dir_name + data_set + extension
      return pd.read_excel(filename)

def list_datasets():
   data_sets = [
      'Number_of_teaching_staff_in_Higher_Education_2020_06_09', 'customs_warehouses', 'courier_companies',
'vehicle_clearance_certificate', 'UAE_National_Red_List_Species', 'customs_warehouse_licensees',
'declaration_cargo_detail-2', 'Services-En_0', 'Graduates_in_Highe_Education_20-06-09', 
'declaration_cargo_detail-1', 'livebirths',
   ]
   return data_sets