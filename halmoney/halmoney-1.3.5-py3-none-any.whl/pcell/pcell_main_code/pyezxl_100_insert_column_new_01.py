# -*- coding: utf-8 -*-
from halmoney import pcell

excel = pcell.pcell()

#선택한 영역에 한칸씩 가로열을 넣는다
sheet_name = excel.read_activesheet_name()
[x1, y1, x2, y2] = excel.read_select_address()

for y in range(y2, y1, -1):
	excel.insert_y_line(sheet_name, y)