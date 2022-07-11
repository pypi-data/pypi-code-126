# -*- coding: utf-8 -*-
import pandas
import matplotlib.pyplot as plt
import numpy as np

class rgraph:
	def __init__(self):
		self.var = {}
		self.chart = plt
		self.marker_color = "k"
		self.marker_line_style = "-"
		self.marker_style = "o"
		self.chart.rc("font", family="Malgun Gothic")
		self.chart_type ="plot"
		self.chart.grid(False)

	def set_data(self, input_list):
		#plt.axis([0, 5, 0, 20])  # X, Y축의 범위: [xmin, xmax, ymin, ymax]
		self.data = input_list

	def set_grid(self, input_list=False):
		self.chart.grid(input_list)

	def set_label(self, input_text):
		if input_text[0] !="": self.chart.xlabel(input_text[0])
		if input_text[1] !="": self.chart.ylabel(input_text[1])

	def set_xtick(self, input_list):
		self.chart.xticks(input_list[0], input_list[1])

	def set_ytick(self, input_list):
		self.chart.yticks(input_list[0], input_list[1])

	def set_marker_color(self, input_text):
		print(input_text)
		self.marker_color = self.check_marker_color_dic(input_text)
		print(self.marker_color)

	def check_marker_color_dic(self, input_text):
		m1_dic = {"b":"b",
		         "g": "g",
		         "r": "r",
		         "y": "y",
		         "bla": "k",
		          }
		result = m1_dic[input_text]
		print(result)
		return result

	def set_marker_line_style(self, input_text):
		self.marker_line_style = self.check_marker_line_style_dic(input_text)

	def check_marker_line_style_dic(self, input_text):
		m2_dic = {"-":"-",
		         "--": "--",
		         "-.": "-.",
		         ".": ":",
		         }
		result = m2_dic[input_text]
		return result

	def set_marker_style (self, input_list):
		self.marker_style = self.check_marker_style_dic(input_list)

	def check_marker_style_dic(self, input_text):
		m3_dic = {".":".",
		         "o": "o",
		         "rect": "s",
		         "x": "x",
		         }
		result = m3_dic[input_text]
		return result

	def set_title(self, input_text):
		self.chart.title(input_text)

	def check_scale(self):
		pass

	def check_grid(self):
		pass

	def set_chart_type(self, input_text="plot"):
		self.chart_type = input_text

	def check_chart_type(self):
		input_text = self.chart_type
		aaa = self.marker_color + self.marker_line_style + self.marker_style
		if input_text == "plot":
			self.chart.plot(self.data[0], self.data[0], aaa)
		elif input_text == "bar":
			self.chart.bar(self.data[0], self.data[0], aaa)
		elif input_text == "pie":
			self.chart.pie(self.data[0], self.data[0], aaa)
		elif input_text == "errorbar":
			self.chart.errorbar(self.data[0], self.data[0], aaa)
		elif input_text == "hist":
			self.chart.hist(self.data[0], self.data[0], aaa)
		elif input_text == "scatter":
			self.chart.scatter(self.data[0], self.data[0], aaa)
			plt.scatter(x, y, s=area, c=colors, alpha=0.5, cmap='Spectral')

	def set_figure(self):
		#figsize : (width, height)의 튜플을 전달한다. 단위는 인치이다.
		#dpi : 1인치당의 도트 수
		#facecolor : 배경색
		#edgecolor : 외곽선의 색
		pass

	def run(self):
		self.check_chart_type()
		self.chart.show()

aaa = rgraph()
aaa.set_data([[1, 2, 3, 4],[1, 2, 3, 4]])
#aaa.set_marker_color("b")
aaa.set_ytick([[1, 2, 8], ["Low", "Zero", "High"]])
aaa.set_title("title / 타이틀")
aaa.set_marker_line_style("-")
aaa.set_chart_type("scatter")
aaa.set_marker_style("o")
aaa.set_grid("o")
aaa.set_label(["xxx", "yyy"])

aaa.run()


#bcr.bar_chart_race(df = df,
#                   n_bars = 10,
#                   figsize=(6, 4),
#                   sort='desc',
#                   title='Premier League Clubs Points Since 1992')