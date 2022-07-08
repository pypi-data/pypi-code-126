from src.so4gp import so4gp
import json

out_json, gps = so4gp.rsgps('DATASET.csv', max_iteration=20, return_gps=True)
# out_json, gps = so4gp.graank('DATASET.csv', return_gps=True)
print(out_json)

out_obj = json.loads(out_json)
print(out_obj["Invalid Count"])
