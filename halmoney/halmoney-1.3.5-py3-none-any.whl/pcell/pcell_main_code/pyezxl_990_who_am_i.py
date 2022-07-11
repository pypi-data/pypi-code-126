# -*- coding: utf-8 -*-
from halmoney import pcell
excel = pcell.pcell()

list_wai = [
"Name : S. J. Park",
"Web Site : www.halmoney.com",
"Date : 2021-04-19",
"Version : 1.0.0"
]

all_text=""
for a in list_wai:
	all_text = all_text + a + '\n'

excel.show_messagebox("Name : S. J. Park")