# -*- coding: utf-8 -*-
from halmoney import pcell
import time

excel = pcell.pcell()

# 5초마다 반복되는 코드

for one in range(1,1000):
	print(excel.read_time_now())
	
	# 이곳에 반복 실행할 코드를 넣으면 됩니다

	time.sleep(5)