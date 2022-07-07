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

def file_to_list():
    # empty list to read list from a file
    names = []
    # open file and read the content in a list
    with open(r'data_file_name.txt', 'r') as fp:
        for line in fp:
            # remove linebreak from a current name
            # linebreak is the last character of each line
            x = line[:-1]
            # add current item to the list
            names.append(x)
    # display list
    return names


def list_datasets():
   data_sets = file_to_list()
   return data_sets
