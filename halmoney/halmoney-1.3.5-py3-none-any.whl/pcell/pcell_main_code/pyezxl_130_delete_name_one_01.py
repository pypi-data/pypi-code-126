# -*- coding: utf-8 -*-
from halmoney import pcell

excel = pcell.pcell()



#현재 화일에서 이름을 삭제하는것
bbb=excel.read_messagebox_value("Please input text")
excel.delete_sheet_rangename(bbb)