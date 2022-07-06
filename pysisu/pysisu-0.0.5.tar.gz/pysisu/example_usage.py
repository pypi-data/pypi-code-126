import pysisu
import os

API_KEY = os.environ.get('SISU_API_KEY')
ANALYSIS_ID = 13234

table = pysisu.get_results(ANALYSIS_ID, API_KEY, {"top_drivers": "False"}, auto_paginate=False, url="https://dev.sisu.ai")
print(','.join([x.column_name for x in table.header]))
for row in table.rows:
    print(row)
