import sys
import os
from client import Client


class TestClient:
    def setup_class(self):
        client = Client()
        client.login('admin', 'admin')
        self.client = client

    def test_query(self):
        param = {
            'domain': 'sheet',
            'phylum': 'trading',
            'class': 'asharecalendar',
            'fields': ['TRADE_DAYS', 'S_INFO_EXCHMARKET'],
            'start_date': '20180101',
            'end_date': '20221231',
            'codes': ['000300.SH']
        }
        self.client.query(param)

    def test_extract(self):
        param = {
            'domain': 'sheet',
            'phylum': 'direct',
            'class': 'asharefinancialindicator_S_FA_INTERESTDEBT',
            'fields': [],
            'start_date': '20180101',
            'end_date': '20181231',
            'codes': []
        }
        param["class"] = param["class"].lower()
        self.client.extract(param)


