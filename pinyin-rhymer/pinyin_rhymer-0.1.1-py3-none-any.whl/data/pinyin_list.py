import csv
from pathlib import Path

pinyin_file = Path(__file__).parent / 'pinyinList.csv'

csv_file = open(pinyin_file, 'r', encoding='utf-8')
reader = csv.DictReader(csv_file)
PINYIN_LIST = {x['pinyin'] for x in reader}
csv_file.close()
