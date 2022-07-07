import pandas as pd
import requests



def get_data(data_set):

   extension = '.csv'
   dir_name =  'https://raw.githubusercontent.com/aimluae/uaedata/main/datasets/'
   filename = dir_name + data_set + extension

   if requests.get(filename).status_code == 200:
      return pd.read_csv(filename)
   else:
      extension = '.xlsx'
      filename = dir_name + data_set + extension
      return pd.read_excel(filename)

# def file_to_list():
#     # empty list to read list from a file
#     names = []
#     # open file and read the content in a list
#     with open(r'data_file_name.txt', 'r') as fp:
#         for line in fp:
#             # remove linebreak from a current name
#             # linebreak is the last character of each line
#             x = line[:-1]
#             # add current item to the list
#             names.append(x)
#     # display list
#     return names




def list_datasets():
   data_sets = ['Number_of_teaching_staff_in_Higher_Education_2020_06_09', 'customs_warehouses', 'courier_companies', 'Abu_Dhabi_Hotel_Performance_Statistics_for_year_2021', 'Total_Guests__by_Purpose_of_Visit,Year_and_Quarter', 'CustomerSatisfaction_0', 'vehicle_clearance_certificate', 'UAE_National_Red_List_Species', 'Number_of_visitors_to_the_Abu_Dhabi_International_Boat_Show', 'QCC_ODS_45_Registered_CABs_Raw_Data.V.1', 'احصائية_بيانات_ابوظبي_المفتوحة_-_التجارة_-_لشهر_يناير_2021', 'BookFairs_Number_of_Visitors_and_Exhibitors_Year_2021', 'DCT_Number_of_Students_enrolled_in_art_Classes_by_Year_2021', 'Number_of_visitors_to_events_during_the_year', 'customs_warehouse_licensees', 'declaration_cargo_detail-2', 'Services-En_0', 'Graduates_in_Highe_Education_20-06-09', 'declaration_cargo_detail-1', 'livebirths', 'Number_of_members_by_city', 'Industrial_Sector_Products_in_Emirate_of_Abu_Dhab']
   return data_sets

