import os, sys, json
from .ark_setting import *



def get_tot_pool_info(pool_name_file):
    res = []
    with open(pool_name_file, 'r', encoding='utf-8') as f:
        tmp_json = json.load(f)
    return tmp_json

