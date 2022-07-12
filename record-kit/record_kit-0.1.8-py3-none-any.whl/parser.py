from io import StringIO

import markdown
import pandas as pd
from html.parser import HTMLParser
import numpy as np
import pathlib
from .recorder import Recorder

class HTMLRecordParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.meta_string = None
        self.data_string = None
        self.stage = 0

    def handle_starttag(self, tag, attrs):
        pass

    def handle_endtag(self, tag):
        pass

    def handle_data(self, data):
        if data == "\n":
            return
        if data == "Meta":
            self.stage = 1
            return
        elif data == "Data":
            self.stage = 2
            return
        if self.stage == 1:
            self.meta_string = data
        elif self.stage == 2:
            self.data_string = data


def parse_token(type_str, value):
    if type_str == 'int':
        return int(value)
    elif type_str == 'float':
        return float(value)
    else:
        return value

def parse_table(table_string):
    table = table_string.split("\n")

    def parse_line(line):
        line = line.split('|')
        tokens = line[1:-1]
        tokens = list(map(lambda x: x[1:-1], tokens))
        # tokens[1] = parse_token(tokens[-1], tokens[1])
        return tokens

    header = parse_line(table[0])
    body = map(parse_line, table[2:])
    return header, body

class Record:
    def __init__(self, record_path):
        if isinstance(record_path, Recorder):
            self.record_path = record_path.record_name
        else:
            self.record_path = pathlib.Path(record_path)
        self.text = None
        self.html = None
        self.meta = {}
        self.data = None
        self._load_record()

    def reload(self):
        self._load_record()

    def _load_record(self):
        with self.record_path.open("r") as f:
            self.text = f.read()
        parser = HTMLRecordParser()

        self.html_text = markdown.markdown(self.text)
        parser.feed(self.html_text)
        self._parse_meta(parser.meta_string)
        self._parse_data(parser.data_string)


    def _parse_table(self, table_string: str):
        table = table_string.split("\n")
        def parse_line(line):
            line = line.split('|')
            tokens = line[1:-1]
            tokens = list(map(lambda x:x[1:-1], tokens))
            tokens[1] = parse_token(tokens[-1], tokens[1])
            return tokens
        header = parse_line(table[0])
        body = map(parse_line, table[2:])
        return header, body

    def _parse_meta(self, meta_string):
        header, body = parse_table(meta_string)
        for item in body:
            self.meta[item[0]] = parse_token(item[2],item[1])

    def _parse_data(self, data_string):
        header, body = parse_table(data_string)
        data = list(body)
        data = [','.join(seq) for seq in data]
        data_str = ','.join(header) + '\n' + '\n'.join(data)
        csv_str = StringIO(data_str)
        data = pd.read_csv(csv_str)
        self.data = data

    # def get_meta(self):
    #     pass
    #
    # def get_data(self):
    #     pass