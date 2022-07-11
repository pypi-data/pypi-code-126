import csv
from pathlib import Path

pinyin_file = Path(__file__).parent / 'pinyinList.csv'


class PinYinList(object):
    def __init__(self):
        self.csv = open(pinyin_file, 'r', encoding='utf-8')
        self.reader = csv.DictReader(self.csv)

    def __del__(self):
        self.csv.close()

    def get_pinyin(self):
        return {x['pinyin'] for x in self.reader}


PINYIN_LIST = PinYinList()
