# -*- coding: utf-8 -*-
import win32com.client
import re
import string
import win32gui
import math
import random
import itertools
import numpy

from halmoney import scolor, youtil, basic_data, jfinder

class pcell:
	def __init__(self, filename=""):
		#공통으로 사용할 변수들을 설정하는 것이다
		self.basic = basic_data.basic_data()

		self.common_data = self.basic.basic_data()
		self.util = youtil.youtil()
		self.finder = jfinder.jfinder()
		self.color = scolor.scolor()

		# 만약 화일의 경로가 있으면 그 화일을 열도록 한다
		self.xlApp = win32com.client.dynamic.Dispatch('Excel.Application')
		self.xlApp.Visible = 1

		if filename != None :
			self.filename = filename.lower()

		if self.filename == 'activeworkbook' or self.filename == '':
			# activeworkbook으로 된경우는 현재 활성화된 workbook을 그대로 사용한다
			self.xlBook = self.xlApp.ActiveWorkbook
			if self.xlBook == None:
				# 만약 activework북을 부르면서도 화일이 존재하지 않으면 새로운 workbook을 만드는 것이다
				try:
					self.xlApp.WindowState = -4137
					self.xlBook = self.xlApp.WorkBooks.Add()
				except:
					win32gui.MessageBox(0, "There is no Activeworkbook", "www.halmoney.com", 0)
		elif filename.lower() == 'new':
			# 빈것으로 된경우는 새로운 workbook을 하나 열도록 한다
			self.xlApp.WindowState = -4137
			self.xlBook = self.xlApp.WorkBooks.Add()
		elif not (self.filename == 'activeworkbook') and self.filename:
			# 만약 화일 이름이 따로 주어 지면 그 화일을 연다
			try:
				self.xlApp.WindowState = -4137
				self.xlBook = self.xlApp.Workbooks.Open(self.filename)
			except:
				win32gui.MessageBox(0, "Please check file path", "www.halmoney.com", 0)

	def add_macro_button(self, sheet_name="", xyxy="", macro_code="입력필요", title=""):
		"""
		버튼을 만들어서 그 버튼에 매크로를 연결하는 것이다
		매크로와 같은것을 특정한 버튼에 연결하여 만드는것을 보여주기위한 것이다
		"""
		xlmodule = self.xlBook.VBProject.VBComponents.Add(1)
		excelcode = """Sub Macro_1()
		        MsgBox ("WOOOOOO WAAAAAA")
		        End Sub"""
		xlmodule.CodeModule.AddFromString(excelcode)

		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		new_btn = sheet.Buttons()
		new_btn.Add(x1, x2, y1, y2)
		new_btn.OnAction = "Macro_1"
		new_btn.Text = title
		#excel.Application.Run("Macro_1")

	def add_picture(self, sheet_name="", file_path="입력필요", xywh="입력필요", link=0, image_in_file = 1):
		"""
		이미지 화일을 넣는것
		"""
		sheet = self.check_sheet_name(sheet_name)
		rng = sheet.Cells(xywh[0],xywh[1])
		rng_x_pixel = rng.Left
		rng_y_pixel = rng.Top

		#sh.Shapes.AddPicture("화일이름", "링크가있나", "문서에저장", "x좌표", "y좌표", "넓이","높이")
		sheet.Shapes.AddPicture(file_path, link, image_in_file, rng_x_pixel,rng_y_pixel,xywh[2],xywh[3] )

	def add_picture_pixcel(self, sheet_name="", file_path="입력필요", pxpywh="입력필요", link=0, image_in_file = 1):
		"""
		이미지 화일을 넣는것
		"""
		sheet = self.check_sheet_name(sheet_name)
		#sh.Shapes.AddPicture("화일이름", "링크가있나", "문서에저장", "x픽셀", "y픽셀", "넓이","높이")
		sheet.Shapes.AddPicture(file_path, link, image_in_file, pxpywh[0],pxpywh[1],pxpywh[2],pxpywh[3] )

	def add_range_text_right(self, sheet_name="", xyxy="", input_text="입력필요"):
		"""
		영역의 모든 자료에 글자를 추가하는 것이다
		"""
		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)

		for x in range(x1, x2 + 1):
			for y in range(y1, y2 + 1):
				one_value = str(self.read_cell_value(sheet_name, [x, y]))
				if one_value == None:
					one_value = ""
				self.write_cell_value(sheet_name, [x, y], (str(one_value) + str(input_text)))

	def add_range_text_left(self, sheet_name="", xyxy="", input_text="입력필요"):
		"""
		영역의 모든 자료에 글자를 추가하는 것
		"""
		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)

		for x in range(x1, x2 + 1):
			for y in range(y1, y2 + 1):
				cell_value = str(self.read_cell_value(sheet_name, [x, y]))
				if cell_value == None: cell_value = ""
				print(x, y, str(cell_value))
				self.write_cell_value(sheet_name, [x, y], (str(input_text) + str(cell_value)))

	def add_range_text_bystep(self, sheet_name="", xyxy="", input_text="입력필요", step="입력필요"):
		"""
		선택한 셀에서 n번째마다 셀에 값을 넣기
		현재 셀이 있는 곳부터 입력을 시작하면서 계산함
		"""
		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)

		basic_list = []
		for one_data in input_text.split(","):
			basic_list.append(one_data.strip())

		for x in range(int(basic_list[0]), int(basic_list[1]) + 1, int(basic_list[2])):
			for y in range(y1, y2 + 1):
				self.write_cell_value(sheet_name, [x, y], basic_list[3])

	def add_sheet(self):
		"""
		새로운 시트하나 추가
		"""
		self.xlBook.Worksheets.Add()

	def change_address_all(self, xyxy="", input_datas="입력필요"):
		"""
		입력된 주소와 입력갯수에 따라서 가능한 모든 종류의 영역을 돌려준다
		"""
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		result = {}
		x_len = len(input_datas)
		y_len = len(input_datas[0])

		x_len_rng = x2 - x1
		y_len_rng = y2 - y1

		max_num = max(map(lambda x : len(x), input_datas))
		min_num = min(map(lambda x : len(x), input_datas))

		max_x = max(x_len, x_len_rng)
		max_y = max(max_num, y_len_rng)

		min_x = max(x_len, x_len_rng)
		min_y = max(y_len, y_len_rng)

		# 입력할것중 가장 적은것을 기준으로 적용
		result["xyxy_min"] = [x1, y1, x1+min_x, y1+min_num]
		# 입력할것중 가장 큰것을 기준으로 적용
		result["xyxy_max"] = [x1, y1, x1+max_x, y1+max_y]
		#일반적인기준으로 적용하는것
		result["xyxy_basic"] = [x1, y1, x1+x_len, y1+max_num]
		return result

	def change_char_num(self, input_text="입력필요"):
		"""
		b를 2로 바꾸어 주는것
		"""
		if str(input_text).lower()[0] in string.digits:
			result = input_text
		else:
			no = 0
			result = 0
			for one in input_text.lower()[::-1]:
				num = string.ascii_lowercase.index(one) + 1
				result = result + 26 ** no * num
				no = no + 1
		return result

	def change_address_xyxy(self, input_value="입력필요"):
		"""
		입력으로 들어오는 범위를 표시하는 다른 값을,
		엑셀에서 사용가능한 주소형태로 변환시켜주는것
		개인적으로 ~를 사용하고 싶어서 그렇다
		"3~4" => [0,3,0,4]
		"""
		if type(input_value) == type([]) or type(input_value) == type(()):
			if len(input_value) == 2:
				result = [input_value[0], input_value[1], input_value[0], input_value[1]]
			elif len(input_value) == 4:
				result = input_value
		elif type(input_value) == type("string"):
			if "~" in str(input_value):
				aaa = input_value.split("~")
				result = [0, int(aaa[0]), 0, int(aaa[1])]
			elif ":" in str(input_value):
				aaa = input_value.split(":")
				result = [0, int(aaa[0]), 0, int(aaa[1])]
		return result

	def change_list_1d_to2d(self, input_list="입력필요"):
		"""
		1차원의 리스트가 오면 2차원으로 만들어주는 것
		입력값중 길이가 다른 리스트를 같게 만들어 주는것
		"""
		result = []
		if len(input_list) > 0:
			if type(input_list[0]) != type([]):
				for one in input_list:
					result.append([one, ])
		return result

	def change_list1d_list2d(self, input_list="입력필요"):
		result = self.change_list_1d_to2d(input_list)
		return result

	def change_list_samelen(self, input_list2d="입력필요"):
		"""
		2차원 리스트의 최대 길이로 같게 만드는 것
		가끔 자료의 갯수가 달라서 생기는 문제가 발생할 가능성이 있는것을 맞추는것이다
		추가할때는 ""를 맞는갯수를 채워넣는다
		"""
		input_text = None
		max_num = max(map(lambda x : len(x), input_list2d))
		result = []
		for one in input_list2d:
			one_len = len(one)
			if max_num == one_len:
				result.append(one)
			else:
				one.extend([input_text]*(max_num - one_len))
				result.append(one)
		return result

	def change_num_char(self, input_data="입력필요"):
		"""
		input_data : 27 => result : aa
		숫자를 문자로 바꿔주는 것
		"""
		if str(input_data).lower()[0] == string.ascii_lowercase:
			result_01 = input_data
		else:
			base_number = int(input_data)
			result_01 = ''
			result = []
			while base_number > 0:
				div = base_number // 26
				mod = base_number % 26
				if mod == 0:
					mod = 26
					div = div - 1
				base_number = div
				result.append(mod)
			for one_data in result:
				result_01 = string.ascii_lowercase[one_data - 1] + result_01
		return result_01

	def change_range_swapcase(self, sheet_name="", xyxy=""):
		"""
		*입력값없이 사용가능*
		입력문자중 대소문자를 변경하는것
		"""
		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)

		for x in range(x1, x2 + 1):
			for y in range(y1, y2 + 1):
				value = str(self.read_cell_value(sheet_name, [x, y]))
				if value == None: value = ""
				self.write_cell_value(sheet_name, [x, y], value.swapcase())

	def change_range_upper(self, sheet_name="", xyxy=""):
		"""
		*입력값없이 사용가능*
		입력문자중 대문자를 변경하는것
		"""
		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)

		for x in range(x1, x2 + 1):
			for y in range(y1, y2 + 1):
				value = str(self.read_cell_value(sheet_name, [x, y]))
				if value == None: value = ""
				self.write_cell_value(sheet_name, [x, y], value.upper())

	def change_range_lower(self, sheet_name="", xyxy=""):
		"""
		*입력값없이 사용가능*
		선택영역안의 모든글자를 소문자로 만들어 주는것
		"""
		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)

		for x in range(x1, x2 + 1):
			for y in range(y1, y2 + 1):
				value = str(self.read_cell_value(sheet_name, [x, y]))
				if value == None: value = ""
				self.write_cell_value(sheet_name, [x, y], value.lower())

	def change_xyxy_r1r1(self, xyxy=""):
		"""
		[1,2,3,4] => "b1:d3"로 바꾸는것
		"""
		str_1 = self.change_num_char(xyxy[1])
		str_2 = self.change_num_char(xyxy[3])

		result = str_1+str(xyxy[0])+":"+str_2+str(xyxy[1])
		return result

	def change_range_capital(self, sheet_name="", xyxy=""):
		"""
		*입력값없이 사용가능*
		첫글자만 대문자로 변경
		"""
		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)

		for x in range(x1, x2 + 1):
			for y in range(y1, y2 + 1):
				value = str(self.read_cell_value(sheet_name, [x, y]))
				if value == None: value = ""
				self.write_cell_value(sheet_name, [x, y], value.capitalize())

	def change_sheet_name(self, old_name="입력필요", new_name="입력필요"):
		"""
		시트이름을 바꿉니다
		"""
		self.xlBook.Worksheets(old_name).Name = new_name

	def change_list_list2d(self, input_data="입력필요"):
		"""
		입력으로 들어온 리스트형태의 자료가 모든 원소또한 리스트인지를 파악하는 것이다
		1차원안의 모든자료가 문자열이면, 2차원은 리스트로 만들지만
		그중일부만 리스트이면 형태가 다른 것이라 가정해야 한다
		"""
		result = []
		type_result = "list"

		if type(input_data) == type([]):
			if type(input_data[0]) == type("string"):
				type_result = "string"
				exit
		if type_result =="list":
			result = input_data
		elif type_result =="string":
			for one in input_data:
				result.append([one])
		return result

	def check_string_address(self, input_text="입력필요"):
		"""
		입력형태 : "$1:$8", "1", "a","a1", "a1b1", "2:3", "b:b"
		숫자와 문자로 된부분을 구분하는 것이다
		"""
		result = []
		aaa = re.compile("[a-zA-Z]*|\d*")
		temp_text = aaa.findall(str(input_text))
		for one in temp_text:
			if one != "":
				result.append(one)
		print(result)
		return result

	def check_address_value(self, input_data="입력필요"):
		"""
		입력형태 :, "", [1,2], [1,2,3,4], "$1:$8", "1", "a","a1", "a1b1", "2:3", "b:b"
		입력된 주소값을 [x1, y1, x2, y2]의 형태로 만들어 주는 것이다
		"""
		# 입력된 자료의 형태에 따라서 구분을 한다
		if input_data == "" or input_data == None:
			# 아무것도 입력하지 않을때
			input_type = self.read_selection_address()
			result = self.check_string_address(input_type)
		elif type(input_data) == type("string"):
			# 문자열일때
			result = self.check_string_address(input_data)
		elif type(input_data) == type([]):
			# 숫자만 들어온것과 구별하기위해 리스트로 들어온것은 4개의요소로 변경을 하였다
			if len(input_data) == 2:
				result = input_data + input_data
			elif len(input_data) == 4:
				# 리스트형태 일때
				result = input_data
		res = self.check_list_address(result)
		final_result =[int(res[0]), int(res[1]), int(res[2]), int(res[3])]
		return final_result

	def check_list_address(self, input_list="입력필요"):
		"""
		입력형태 : [1,2], [1,2,3,4],
		리스트형태로 주소를 모두 [1,2,3,4]의 형태로 만드는 것이다
		"""
		result = []
		if len(input_list) == 1:
			xy = str(input_list[0]).lower()
			# 값이 1개인경우 : ['1'], ['a']
			if xy[0] in string.digits:
				result = [xy, 0, xy, 0]
			elif xy[0].lower() in string.ascii_lowercase:
				result = [0, xy, 0, xy]
		elif len(input_list) == 2:
			# 값이 2개인경우 : ['a', '1'], ['2', '3'], ['a', 'd']
			x1 = str(input_list[0]).lower()
			y1 = str(input_list[1]).lower()
			if x1[0] in string.digits:
				if y1[0] in string.digits:
					result = [x1, 0, y1, 0]
				elif y1[0] in string.ascii_lowercase:
					result = [x1, y1, x1, y1]
			elif x1[0] in string.ascii_lowercase:
				if y1[0] in string.digits:
					result = [y1, x1, y1, x1]
				elif y1[0] in string.ascii_lowercase:
					result = [0, x1, 0, y1]
		elif len(input_list) == 4:
			x1 = str(input_list[0]).lower()
			y1 = str(input_list[1]).lower()
			x2 = str(input_list[2]).lower()
			y2 = str(input_list[3]).lower()
			# 값이 4개인경우 : ['aa', '1', 'c', '44'], ['1', 'aa', '44', 'c']
			if x1[0] in string.digits and x2[0] in string.digits:
				if y1[0] in string.ascii_lowercase and y2[0] in string.ascii_lowercase:
					result = [x1, y1, x2, y2]
				elif y1[0] in string.digits and y2[0] in string.digits:
					result = [x1, y1, x2, y2]
			elif x1[0] in string.ascii_lowercase and x2[0] in string.ascii_lowercase:
				if y1[0] in string.digits and y2[0] in string.digits:
					result = [y1, x1, y2, x2]
		final_result = []
		for one in result:
			one_value = str(one)[0]
			if one_value in string.ascii_lowercase:
				aaa = self.change_char_num(one)
			else:
				aaa = str(one)
			final_result.append(aaa)
		return final_result

	def check_cell_type(self, input_data="입력필요"):
		"""
		입력값 : 주소형태의 문자열
		하나의 영역으로 들어온 것이 어떤 형태인지를 알아 내는 것이다
		"""
		result = ""
		if input_data[0][0] in string.ascii_lowercase and input_data[1][0] in string.digits:
			result = "a1"
		if input_data[0][0] in string.ascii_lowercase and input_data[1][0] in string.ascii_lowercase:
			result = "aa"
		if input_data[0][0] in string.digits and input_data[1][0] in string.digits:
			result = "11"
		return result

	def change_colorindex_int(self, input_color="입력필요"):
		"""
		색깔에 대한 자료를 받으면 rgb값을 돌려준다
		Font.Color.ColorIndex = 2
		ws.Cells(1, 1).Interior.color = rgb_to_hex((218, 36, 238))
		"""

		result_rgb = self.common_data["excel_rgb_56"][input_color]
		result = self.color.change_rgb_int(result_rgb)

		return result

	def check_data_type(self, input_data="입력필요"):
		"""
		영역으로 입력된 자료의 형태를 확인해서 돌려주는 것
		"""
		if type(input_data) == type([]):
			result = "list"
		elif len(str(input_data).split(":")) > 1:
			result = "range"
		elif type(input_data) == type("aaa"):
			result = "cell"
		else:
			result = "error"
		return result

	def check_sheet_name(self, sheet_name=""):
		"""
		sheet이름을 확인해서 sheet객체로 맍들어서 돌려준다.
		아무것도 없으면 현재 활성화된 activesheet를 객체로 만들어서 돌려주는 것이다
		"""
		if sheet_name == "" or sheet_name == None :
			sheet = self.xlApp.ActiveSheet
		elif str(sheet_name).lower() == "activesheet":
			sheet = self.xlApp.ActiveSheet
		else:
			sheet = self.xlBook.Worksheets(sheet_name)
		return sheet

	def check_xline_empty(self, sheet_name="", x="입력필요"):
		"""
		가로열 전체가 빈 것인지 확인해서 돌려준다
		전체가 비었을때는 0을 돌려준다
		"""
		sheet = self.check_sheet_name(sheet_name)
		result = self.xlApp.WorksheetFunction.CountA(sheet.Rows(x).EntireRow)
		return result

	def check_xx_address(self, xx="입력필요"):
		"""
		입력 주소중 xx가 맞는 형식인지를 확인하는것
		결과  = [2, 2]의 형태로 만들어 주는것
		"""
		if type([]) == type(xx):
			if len(xx) == 1:
				result = [xx, xx]
			elif len(xx) == 2:
				result = xx
			elif len(xx) > 2:
				result = [xx[0], xx[1]]
		elif type(123) == type(xx):
			result = [xx, xx]
		elif type("123") == type(xx):
			result = [xx, xx]
		return result

	def check_range_yy(self, sheet_name="", yy="입력필요"):
		"""
		yy영역을 돌려주는것
		"""
		new_y = self.check_yy_address(yy)
		sheet = self.check_sheet_name(sheet_name)
		result = sheet.Columns(str(new_y[0]) + ':' + str(new_y[1]))
		return result

	def check_range_xx(self, sheet_name="", xx="입력필요"):
		"""
		yy영역을 돌려주는것
		"""
		new_x = self.check_xx_address(xx)
		sheet = self.check_sheet_name(sheet_name)
		result = sheet.Rows(str(new_x[0]) + ':' + str(new_x[1]))
		return result

	def check_yy_address(self, yy="입력필요"):
		"""
		결과  = ["b", "b"]의 형태로 만들어 주는것
		"""
		if type([]) == type(yy):
			if len(yy) == 1:
				result = [yy, yy]
			elif len(yy) == 2:
				result = yy
			elif len(yy) > 2:
				result = [yy[0], yy[1]]
		elif type(123) == type(yy):
			result = [yy, yy]
		result_y1 = self.change_num_char(result[0])
		result_y2 = self.change_num_char(result[1])
		return [result_y1, result_y2]

	def check_xy_address(self, xyxy=""):
		"""
		입력의 형태 : 3, [3], [2,3], D, [A,D], [D]
		출력 : [3,3], [2,3], [4,4], [1,4]
		x나 y의 하나를 확인할때 입력을 잘못하는 경우를 방지하기위해 사용
		"""
		result = []
		if type([]) == type(xyxy):
			if len(xyxy) == 1:
				x1 = self.change_char_num(str(xyxy[0]))
				result = [x1, x1]
			if len(xyxy) == 2:
				x1 = self.change_char_num(str(xyxy[0]))
				y1 = self.change_char_num(str(xyxy[1]))
				result = [x1, y1]
		else:
			xyxy = str(xyxy)
			if re.match('[a-zA-Z0-9]', xyxy):
				if re.match('[a-zA-Z]', xyxy):
					xyxy = self.change_char_num(xyxy)
					result = [xyxy, xyxy]
				else:
					result = [xyxy, xyxy]
		return result

	def check_yline_empty(self, sheet_name="", y_no="입력필요"):
		"""
		세로열 전체가 빈 것인지 확인해서 돌려준다.
		전체가 비었을때는 0을 돌려준다
		"""
		y_check = self.check_xy_address(y_no)
		y1 = self.change_char_num(str(y_check[0]))
		sheet = self.check_sheet_name(sheet_name)
		result = self.xlApp.WorksheetFunction.CountA(sheet.Columns(y1).EntireColumn)
		return result

	def close(self):
		"""
		엑셀워크북만이 아니라 엑셀자체도 종료 시킵니다
		"""
		self.xlBook.Close(SaveChanges=0)
		del self.xlApp

	def copy_range(self, sheet_list="입력필요", xyxy_list="입력필요"):
		"""
		영역을 복사하기
		두개의 자료들이 필요하므로, 리스트형태로 사용한다
		"""
		x1, y1, x2, y2 = self.check_address_value(xyxy_list[0])
		sheet1 = self.xlBook.Worksheets(sheet_list[0])
		range1 = sheet1.Range(sheet1.Cells(x1, y1), sheet1.Cells(x2, y2))

		x3, y3, x4, y4 = self.check_address_value(xyxy_list[1])
		sheet2 = self.xlBook.Worksheets(sheet_list[1])
		range2 = sheet2.Range(sheet2.Cells(x3, y3), sheet2.Cells(x4, y4))

		self.xlBook.Worksheets(sheet1).Range(range1).Select()
		self.xlBook.Worksheets(sheet2).Range(range2).Paste()
		self.xlApp.CutCopyMode = 0

	def copy_xline(self, sheet_list="입력필요", xx_list="입력필요"):
		"""
		가로의 값을 복사
		"""
		sheet1 = self.check_sheet_name(sheet_list[0])
		sheet2 = self.check_sheet_name(sheet_list[1])

		xx0_1, xx0_2 = self.check_xy_address(xx_list[0])
		xx1_1, xx1_2 = self.check_xy_address(xx_list[1])

		xx0_1 = self.change_char_num(xx0_1)
		xx0_2 = self.change_char_num(xx0_2)
		xx1_1 = self.change_char_num(xx1_1)
		xx1_2 = self.change_char_num(xx1_2)

		sheet1.Select()
		sheet1.Rows(str(xx0_1) + ':' + str(xx0_2)).Select()
		sheet1.Rows(str(xx0_1) + ':' + str(xx0_2)).Copy()
		sheet2.Select()
		sheet2.Rows(str(xx1_1) + ':' + str(xx1_2)).Select()
		sheet2.Paste()

	def copy_xxline_another_sheet(self, sheet_list="입력필요", xx_list="입력필요"):
		"""
		다른시트에 현재 위치한 한줄을 특정 위치에 복사하기
		이것은 사용자가 코드를 넣어서 사용하기위한 자료인 것이다
		자료를 옮길 시트가 기존에 있는지 확인한후
		없다면 만드는 것이다
		"""
		sheet1 = self.check_sheet_name(sheet_list[0])
		sheet2 = self.check_sheet_name(sheet_list[1])

		# 자료를 복사하는 코드
		self.copy_x_line([sheet1, sheet2], [xx_list[0], xx_list[1]])

	def copy_yline(self, sheet_list="입력필요", yy_list="입력필요"):
		"""
		"""
		# 세로의 값을 복사
		sheet1 = self.check_sheet_name(sheet_list[0])
		sheet2 = self.check_sheet_name(sheet_list[1])

		yy0_1, yy0_2 = self.check_xy_address(yy_list[0])
		yy1_1, yy1_2 = self.check_xy_address(yy_list[1])

		yy0_1 = self.change_num_char(yy0_1)
		yy0_2 = self.change_num_char(yy0_2)
		yy1_1 = self.change_num_char(yy1_1)
		yy1_2 = self.change_num_char(yy1_2)

		sheet1.Select()
		sheet1.Columns(str(yy0_1) + ':' + str(yy0_2)).Select()
		sheet1.Columns(str(yy0_1) + ':' + str(yy0_2)).Copy()
		sheet2.Select()
		sheet2.Columns(str(yy1_1) + ':' + str(yy1_2)).Select()
		sheet2.Paste()

	def count_range_empty_cell(self, sheet_name="", xyxy=""):
		"""
		빈셀의 갯수를 계산한다
		"""
		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		temp_result = 0
		for x in range(x1, x2 + 1):
			for y in range(y1, y2 + 1):
				cell_value = self.read_cell_value(sheet_name, [x, y])
				if cell_value == None:
					self.paint_cell_color(sheet_name, [x, y], 16)
					temp_result = temp_result + 1
		return temp_result

	def count_same_value(self, ):
		"""
		*입력값없이 사용가능*
		선택한 영역의 반복되는 갯수를 구한다
		1. 선택한 영역에서 값을 읽어온다
		2. 사전으로 읽어온 값을 넣는다
		3. 열을 2개를 추가해서 하나는 값을 다른하나는 반복된 숫자를 넣는다
		"""
		sheet_name = self.read_activesheet_name()
		[x1, y1, x2, y2] = self.read_selection_address()

		all_data = self.read_range_value("", [x1, y1, x2, y2])
		py_dic = {}
		# 읽어온 값을 하나씩 대입한다

		for line_data in all_data:
			for one_data in line_data:
				# 키가와 값을 확인
				if one_data in py_dic:
					py_dic[one_data] = py_dic[one_data] + 1
				else:
					py_dic[one_data] = 1

		self.insert_yy(sheet_name, 1)
		self.insert_yy(sheet_name, 1)
		dic_list = list(py_dic.keys())
		for no in range(len(dic_list)):
			self.write_cell_value("", [no + 1, 1], dic_list[no])
			self.write_cell_value("", [no + 1, 2], py_dic[dic_list[no]])

	def count_sheet_shape(self, sheet_name=""):
		"""
		*입력값없이 사용가능*
		"""
		sheet = self.check_sheet_name(sheet_name)
		result = sheet.Shapes.Count
		return result

	def delete_range_value_byno(self, sheet_name="", xyxy="입력필요", input_no="입력필요"):
		"""
		선택한 영역에서 각셀마다 왼쪽에서 N번째까지의글자삭제하기
		"""
		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)

		for x in range(x1, x2 + 1):
			for y in range(y1, y2 + 1):
				cell_value = str(self.read_cell_value(sheet_name, [x, y]))
				if cell_value == "" or cell_value == None or cell_value == None:
					pass
				else:
					self.write_cell_value(sheet_name, [x, y], cell_value[int(input_no):])

	def delete_values_between_specific_letter(self, sheet_name="", xyxy="", input_list=["(",")"]):
		"""
		입력형식 : ["(",")"]
		입력자료의 두사이의 자료를 포함하여 삭제하는것
		예: abc(def)gh ==>abcgh
		"""
		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)

		# re_basic = "\\"+str(input_new[0]) + "[\^" + str(input_new[0]) +"]*\\" + str(input_new[1])

		input_list[0] = str(input_list[0]).strip()
		input_list[1] = str(input_list[1]).strip()

		special_char = ".^$*+?{}[]\|()"
		# 특수문자는 역슬래시를 붙이도록
		if input_list[0] in special_char: input_list[0] = "\\" + input_list[0]
		if input_list[1] in special_char: input_list[1] = "\\" + input_list[1]

		re_basic = str(input_list[0]) + ".*" + str(input_list[1])

		#찾은값을 넣을 y열을 추가한다
		new_y = int(y2)+1
		self.insert_yy(sheet_name, new_y)
		for x in range(x1, x2 + 1):
			temp = ""
			for y in range(y1, y2 + 1):
				cell_value = str(self.read_cell_value(sheet_name, [x, y]))
				result_list = re.findall(re_basic, cell_value)
				if result_list == None or result_list == []:
					pass
				else:
					print("result_list ==>", result_list)
					temp = temp + str(result_list)
					#발견된곳에 색을 칠한다
					self.paint_cell_color("", [x,y], "yel++")
			self.write_cell_value(sheet_name, [x, new_y], temp)

	def delete_cell_value(self, sheet_name="", xy="입력필요"):
		"""
		range의 입력방법은 [row1, col1, row2, col2]이다
		선택한영역에서 값을 clear기능을 한다
		"""
		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xy)
		my_range = sheet.Range(sheet.Cells(x1, y1), sheet.Cells(x2, y2))
		my_range.ClearContents()

	def delete_from_n_words_01(self, sheet_name="", xyxy="", num="입력필요"):
		"""
		선택한 영역에서 각셀마다 왼쪽에서 N번째까지의 글자삭제하기
		"""
		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)

		for x in range(x1, x2 + 1):
			for y in range(y1, y2 + 1):
				current_data = str(self.read_cell_value(sheet_name, [x, y]))
				print(current_data)
				if current_data == "" or current_data == None or current_data == None:
					pass
				else:
					self.write_cell_value(sheet_name, [x, y], current_data[int(num):])

	def delete_range_memo(self, sheet_name="", xyxy=""):
		"""
		*입력값없이 사용가능*
		선택영역의 메모를 삭제
		"""
		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		my_range = sheet.Range(sheet.Cells(x1, y1), sheet.Cells(x2, y2))

		my_range.ClearComments()

	def delete_range_samevalue_unique(self, sheet_name="", xyxy=""):
		"""
		*입력값없이 사용가능*
		선택한 자료중에서 고유한 자료만을 골라내는 것이다
		"""
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		temp_datas = self.read_range_value(sheet_name, xyxy)

		set_a = set([])
		for x in range(x1, x2 + 1):
			for y in range(y1, y2 + 1):
				current_data = str(self.read_cell_value(sheet_name, [x, y]))
				set_a.add(current_data)

		list_1 = list(set_a)
		list_1 = list_1.sort()
		len_set = len(set_a)
		num = 0
		for x in range(x1, x2 + 1):
			for y in range(y1, y2 + 1):
				if num <= len_set:
					self.write_cell_value("", [x,y], list_1[num])
					num = num + 1

	def delete_panthom_rangname(self):
		"""
		*입력값없이 사용가능*
		엑셀의 이름영역중에서 연결이 끊긴것을 삭제하는 것이다
		"""
		aaa = self.xlApp.Names
		cnt = self.xlApp.Names.Count
		print("총 갯수는", cnt)
		for num in range(1, cnt+1):
			print(num)
			aaa = self.xlApp.Names(num).Name
			print(self.xlApp.Names(num).Name)
			print(self.xlApp.Names(num).RefersTo)
			if aaa.find("!") < 0:
				self.xlApp.Names(aaa).Delete()

	def delete_range_color(self, sheet_name="", xyxy=""):
		"""
		*입력값없이 사용가능*
		영역의 모든 색을 지운다
		"""
		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		my_range = sheet.Range(sheet.Cells(x1, y1), sheet.Cells(x2, y2))

		my_range.Interior.Pattern = -4142
		my_range.Interior.TintAndShade = 0
		my_range.Interior.PatternTintAndShade = 0

	def delete_range_linecolor(self, sheet_name="", xyxy=""):
		"""
		*입력값없이 사용가능*
		영역에 선들의 그대로 있으나 색을 기본색으로 만드는 것이다
		"""
		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		my_range = sheet.Range(sheet.Cells(x1, y1), sheet.Cells(x2, y2))

		my_range.Interior.Pattern = 0
		my_range.Interior.PatternTintAndShade = 0

	def delete_range_line(self, sheet_name="", xyxy=""):
		"""
		*입력값없이 사용가능*
		영역의 모든선을 지운다
		"""
		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		my_range = sheet.Range(sheet.Cells(x1, y1), sheet.Cells(x2, y2))

		for each in [5, 6, 7, 8, 9, 10, 11, 12]:
			my_range.Borders(each).LineStyle = -4142

	def delete_range_link(self, sheet_name="", xyxy=""):
		"""
		*입력값없이 사용가능*
		영역의 모든 인터넷 링크를 지운다
		"""
		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		my_range = sheet.Range(sheet.Cells(x1, y1), sheet.Cells(x2, y2))
		my_range.Hyperlinks.Delete()

	def delete_range_value(self, sheet_name="", xyxy=""):
		"""
		range의 입력방법은 [row1, col1, row2, col2]이다
		선택한 영역안의 모든 값을 지운다
		"""
		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		my_range = sheet.Range(sheet.Cells(x1, y1), sheet.Cells(x2, y2))
		my_range.ClearContents()

	def delete_rangename(self, range_name="입력필요"):
		"""
		입력한 영역의 이름을 삭제, name은 workbook에서 가능
		"""
		result = self.xlBook.Names(range_name).Delete()
		return result

	def delete_range_empty_x(self, sheet_name="", xyxy=""):
		"""
		*입력값없이 사용가능*
		선택한영역에서 x줄의 값이 없으면 x줄을 삭제한다
		"""
		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		print(x1, y1, x2, y2)


		#WorksheetFunction.CountA(Range("D:D"))

		for x in range(x2, x1, -1):
			#chr_address = self.change_num_char(x)
			changed_address = str(x) + ":"+str(x)
			print(x, changed_address)
			num = self.xlApp.WorksheetFunction.CountA(sheet.Range(changed_address))
			#Columns(1).EntireColumn.Delete
			if num ==0:
				print("빈셀의번호", x)
				self.delete_xxline(sheet_name, x)

	def delete_range_empty_y(self, sheet_name="", xyxy=""):
		"""
		*입력값없이 사용가능*
		선택한영역에서 x줄의 값이 없으면 y줄을 삭제한다
		"""
		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		#print(x1, y1, x2, y2)
		for y in range(y2, y1, -1):
			y_new = self.change_num_char(y)
			changed_address = str(y_new) + ":"+str(y_new)
			#print(y, changed_address)
			num = self.xlApp.WorksheetFunction.CountA(sheet.Range(changed_address))
			#Columns(1).EntireColumn.Delete
			if num ==0:
				#print("빈셀의번호", y)
				self.delete_yyline(sheet_name, y)

	def delete_range_bystep(self, sheet_name="", xyxy="", input_list="입력필요"):
		"""
		선택한 영역중 여러부분이 같을 때 그 열을 삭제하는것
		입력값 : 1,3,4 (이 3개의 자료가 모두 같은것만 삭제하기)

		코드 : 1과 3과 4의 값을 모두 특수문자를 사용하여 연결한후 이것을 사전의 키로 만들어서
		      비교하여 선택한다
			  각개개는 틀리지만 합쳤을때 같아지는 형태가 있을수 있어 특수문자를 포함한다
			  예 : 123, 45 과 12, 345
		"""

		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)


		base_data_1 = self.read_range_value(sheet_name="", xyxy="")
		base_data_2 = base_data_1
		same_num = len(input_list)

		del_list = []

		for x in range(x1, x2 + 1):
			line_data = base_data_1[x]
			for x_2 in range(x + 1, x2 + 1):
				count = 0
				com_one_line = base_data_1[x_2]
				for one_num in input_list:
					if line_data[one_num] == com_one_line[one_num]:
						count = count + 1
				if count == same_num:
					del_list.append(x_2)
					sheet.Range(sheet.Cells(x1 + x, y1), sheet.Cells(x1 + x, y2)).ClearContents()

	def delete_range_samevalue_continious(self, sheet_name="", xyxy=""):
		"""
		*입력값없이 사용가능*
		선택한 영역중 세로로 연속된 같은자료만 삭제
		밑에서부터 올라가면서 찾는다
		"""
		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)


		for y in range(y1, y2 + 1):
			for x in range(x2, x1, -1):
				base_value = self.read_cell_value(sheet_name, [x, y])
				up_value = self.read_cell_value(sheet_name, [x - 1, y])
				if base_value == up_value:
					self.write_cell_value(sheet_name, [x, y], "")

	def delete_range_samevalue(self, sheet_name="", xyxy=""):
		"""
		*입력값없이 사용가능*
		선택한 영역안의 고유한 첫번째 것은 그대로 두고
		나머지부터 같은것은 삭제한다
		"""
		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)

		set_a = set([])
		for x in range(x1, x2 + 1):
			for y in range(y1, y2 + 1):
				value = self.read_cell_value(sheet_name, [x, y])
				if value =="" or value == None:
					pass
				else:
					len_old = len(set_a)
					set_a.add(value)
					len_new = len(set_a)
					if len_old == len_new:
						self.write_cell_value(sheet_name, [x, y], "")

	def delete_range_trim(self, sheet_name="", xyxy=""):
		"""
		*입력값없이 사용가능*
		왼쪽끝과 오른쪽 끝의 공백을 삭제하는 것
		"""
		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)

		for x in range(x1, x2 + 1):
			for y in range(y1, y2 + 1):
				cell_value = self.read_cell_value(sheet_name, [x, y])
				changed_data = str(cell_value).strip()
				if cell_value == changed_data or cell_value == None:
					pass
				else:
					self.write_cell_value(sheet_name, [x, y], changed_data)
					self.paint_cell_color(sheet_name, [x, y], 16)

	def delete_range_ltrim(self, sheet_name="", xyxy=""):
		"""
		*입력값없이 사용가능*
		왼쪽끝의 공백을 삭제하는 것
		"""
		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)

		for x in range(x1, x2 + 1):
			for y in range(y1, y2 + 1):
				cell_value = self.read_cell_value(sheet_name, [x, y])
				changed_data = str(cell_value).lstrip()
				if cell_value == changed_data or cell_value == None or type(cell_value) == type(123):
					pass
				else:
					self.write_cell_value(sheet_name, [x, y], changed_data)
					self.paint_cell_color(sheet_name, [x, y], 16)

	def delete_range_rtrim(self, sheet_name="", xyxy=""):
		"""
		*입력값없이 사용가능*
		왼쪽끝의 공백을 삭제하는 것
		"""
		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)

		for x in range(x1, x2 + 1):
			for y in range(y1, y2 + 1):
				cell_value = self.read_cell_value(sheet_name, [x, y])
				changed_data = str(cell_value).rstrip()
				if cell_value == changed_data or cell_value == None or type(cell_value) == type(123):
					pass
				else:
					self.write_cell_value(sheet_name, [x, y], changed_data)
					self.paint_cell_color(sheet_name, [x, y], "red++")

	def delete_yline_value_bystep(self, sheet_name="", xyxy="", step_no="입력필요"):
		"""
		삭제 : 선택자료중 n번째 세로줄의 자료를 값만 삭제하는것
		일하다보면 3번째 줄만 삭제하고싶은경우가 있다, 이럴때 사용하는 것이다
		"""
		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)

		mok, namuji = divmod(y2-y1+1, int(step_no))
		#print(mok, namuji)
		end_no = y2-namuji
		start_no = y1

		for y in range(end_no, start_no, -1):
			if divmod(y, int(step_no))[1] ==0:
				#print("맞는것==>",x)
				self.delete_range_value(sheet_name, [x1, y, x2, y])

	def delete_xline_value_bystep(self, sheet_name="", xyxy="", step_no="입력필요"):
		"""
		삭제 : 선택자료중 n번째 세로줄의 자료를 값만 삭제하는것
		일하다보면 3번째 줄만 삭제하고싶은경우가 있다, 이럴때 사용하는 것이다
		"""
		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)

		mok, namuji = divmod(x2-x1+1, int(step_no))
		#print(mok, namuji)
		end_no = x2-namuji
		start_no = x1

		for x in range(end_no, start_no, -1):
			if divmod(x, int(step_no))[1] ==0:
				#print("맞는것==>",x)
				self.delete_range_value(sheet_name, [x, y1, x, y2])

	def delete_yline_bystep(self, sheet_name="", xyxy="", step_no="입력필요"):
		"""
		삭제 : 2 ==> 기존의 2번째 마다 삭제 (1,2,3,4,5,6,7 => 1,3,5,7)
		삽입 : 2 ==> 2번째에 새로운것 추가 (1,2,3,4,5,6,7 => 1,2,2,3,4,4,5,6,6,7)
		"""
		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)

		mok, namuji = divmod(y2-y1+1, int(step_no))
		#print(mok, namuji)
		end_no = y2-namuji
		start_no = y1

		for y in range(end_no, start_no, -1):
			if divmod(y, int(step_no))[1] ==0:
				#print("맞는것==>",y)
				#self.delete_range_value(sheet_name, [x1, y, x2, y])
				self.delete_yyline(sheet_name, [y,y])

	def delete_xline_bystep(self, sheet_name="", xyxy="", step_no="입력필요"):
		"""
		삭제 : 2 ==> 기존의 2번째 마다 삭제 (1,2,3,4,5,6,7 => 1,3,5,7)
		삽입 : 2 ==> 2번째에 새로운것 추가 (1,2,3,4,5,6,7 => 1,2,2,3,4,4,5,6,6,7)
		"""
		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)

		mok, namuji = divmod(x2-x1+1, int(step_no))
		#print(mok, namuji)
		end_no = x2-namuji
		start_no = x1

		for x in range(end_no, start_no, -1):
			if divmod(x, int(step_no))[1] ==0:
				#print("맞는것==>",x)
				self.delete_xxline(sheet_name, [x,x])

	def delete_shape(self, sheet_name="", shape_name="입력필요"):
		"""
		그림 하나를 지우는 것이다
		"""
		sheet = self.check_sheet_name(sheet_name)
		sheet.Shapes(shape_name).Delete()

	def delete_shape_all(self, sheet_name=""):
		"""
		특정 시트안의 그림을 다 지우는 것이다
		"""
		sheet = self.check_sheet_name(sheet_name)
		drawings_no = sheet.Shapes.Count
		if drawings_no > 0:
			for aa in range(drawings_no, 0, -1):
				# Range를 앞에서부터하니 삭제하자마자 번호가 다시 매겨져서, 뒤에서부터 삭제하니 잘된다
				sheet.Shapes(aa).Delete()
		return drawings_no

	def delete_sheet(self, sheet_name=""):
		"""
		입력한 시트를 삭제하기
		"""
		try:
			sheet = self.check_sheet_name(sheet_name)
			self.xlApp.DisplayAlerts = False
			sheet.Delete()
			self.xlApp.DisplayAlerts = True
		except:
			pass

	def delete_sheet_value_all(self, sheet_name=""):
		"""
		*입력값없이 사용가능*
		시트안의 모든 값을 삭제한다
		"""
		sheet = self.check_sheet_name(sheet_name)
		sheet.Cells.ClearContents()

	def delete_usedrange_value(self, sheet_name=""):
		"""
		usedrange 영역의 값을 지우는것 이다
		"""
		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.read_usedrange_address(sheet_name)
		my_range = sheet.Range(sheet.Cells(x1, y1), sheet.Cells(x2, y2))
		my_range.ClearContents()

	def delete_xxline(self, sheet_name="", xx="입력필요"):
		"""
		가로의 여러줄을 삭제하기
		입력형태는 2, [2,3]의 두가지가 가능하다
		"""
		sheet = self.check_sheet_name(sheet_name)
		new_xx = self.check_xx_address(xx)
		sheet.Rows(str(new_xx[0]) + ':' + str(new_xx[1])).Delete()

	def delete_xxline_value(self, sheet_name="", xx="입력필요"):
		"""
		세로의 여러줄을 값을 삭제
		"""
		sheet = self.check_sheet_name(sheet_name)
		xx = self.check_xx_address(xx)
		sheet.Columns(str(xx[0]) + ':' + str(xx[1])).ClearContents()

	def delete_yyline(self, sheet_name="", yy="입력필요"):
		"""
		delete_yyline(sheet_name, yy)
		세로줄을 삭제하기
		"""
		sheet = self.check_sheet_name(sheet_name)
		yy =self.check_yy_address(yy)
		sheet.Columns(str(yy[0]) + ':' + str(yy[1])).Delete(-4121)

	def delete_yyline_value(self, sheet_name="", yy="입력필요"):
		"""
		delete_yyline_value(sheet_name, yy)
		세로줄의 값만 삭제하기
		"""
		sheet = self.check_sheet_name(sheet_name)
		yy =self.check_yy_address(yy)
		sheet.Columns(str(yy[0]) + ':' + str(yy[1])).ClearContents()

	def df_write_to_excel(self, sheet_name="", df_obj="입력필요", xyxy = [1,1]):
		"""
		pandas의 dataframe의 자료를 커럼과 값을 기준으로 나누어서
		엑셀에 써넣는다
		"""
		sheet = self.check_sheet_name(sheet_name)
		col_list = df_obj.columns.values.tolist()
		value_list = df_obj.values.tolist()
		self.write_range_value(sheet_name, xyxy, [col_list])
		self.dump_range_value(sheet_name, [xyxy[0]+1, xyxy[1]], value_list)

	def paint_range_samevalue_rgbcolor(self, sheet_name="", xyxy=""):
		"""
		*입력값없이 사용가능*
		선택한 영역에서 2번이상 반복된것만 색칠하기
		"""
		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)


		set_a = set([])
		for x in range(x1, x2 + 1):
			for y in range(y1, y2 + 1):
				value = self.read_cell_value(sheet_name, [x, y])
				if value =="" or value == None:
					pass
				else:
					len_old = len(set_a)
					set_a.add(value)
					len_new = len(set_a)
					if len_old == len_new:
						self.paint_cell_color(sheet_name, [x, y], "red++")

	def check_color_style(self, input_data):
		"""
		들어온 자료를 기준으로 rgb색과 int로 변경해 준다
		"""
		if type(input_data) ==type([]):
			rgb = input_data
		elif type(input_data) ==type("string"):
			rgb = self.color.change_scolor_rgb(input_data)
		elif type(input_data) ==type(12):
			rgb = self.color.get_excel_rgb56(input_data)

		rgb_to_int = (int(rgb[2])) * (256 ** 2) + (int(rgb[1])) * 256 + int(rgb[0])
		result = [rgb, rgb_to_int]
		return result

	def dump_range_value(self, sheet_name="", xyxy="", input_datas="입력필요"):
		"""
		한꺼번에 값을 써넣을때 사용
		"""
		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)

		sheet.Range(sheet.Cells(x1, y1), sheet.Cells(x1 + len(input_datas)-1, y1 + len(input_datas[0])-1)).Value = input_datas

	def excel_fun_trim(self, input_data="입력필요"):
		"""
		함수중 rtrim을 사용하는 것이며 엑셀 함수의 사용을 보여주기 위하여 만든 것이다
		"""
		aaa = self.xlApp.WorksheetFunction.Trim(input_data)
		return aaa

	def fill_emptycell_uppercell(self, sheet_name="", xyxy=""):
		"""
		*입력값없이 사용가능*
		빈셀을 발견하면 바로위의 자료로 넣기
		채우기 : 빈셀 바로위의 것으로 채우기
		"""
		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)

		old_data = ""
		for y in range(y1, y2 + 1):
			for x in range(x1, x2 + 1):
				cell_value = self.read_cell_value(sheet_name, [x, y])
				if x == x1:
					# 만약 자료가 제일 처음이라면
					old_data = cell_value
				else:
					if cell_value == None:
						self.write_cell_value(sheet_name, [x, y], old_data)
					else:
						old_data = cell_value

	def fun_ltrim(self, input_data="입력필요"):
		"""
		함수중 ltrim을 사용하는 것이며 엑셀 함수의 사용을 보여주기 위하여 만든 것이다
		"""
		aaa = self.xlApp.WorksheetFunction.LTrim(input_data)
		return aaa

	def insert_xx(self, sheet_name="", x="입력필요"):
		"""
		가로열을 한줄삽입하기
		"""
		sheet = self.check_sheet_name(sheet_name)
		x1 = self.check_xy_address(x)
		x_no = self.change_char_num(str(x1[0]))
		sheet.Range(str(x_no) + ':' + str(x_no)).Insert()

	def insert_x_bystep(self, sheet_name="", xyxy="", step_no="입력필요"):
		"""
		n번째마다 열을 추가하는것
		새로운 가로열을 선택한 영역에 1개씩 추가하는것이다
		n번째마다는 n+1번째가 추가되는 것이다
		"""
		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)

		for x in range(x2 - x1 + 1, 0, -1):
			if divmod(x, step_no)[1] == 0:
				self.insert_xx(sheet_name, x+x1)

	def insert_y_bystep(self, sheet_name="", xyxy="", step_no="입력필요"):
		"""
		n번째마다 열을 추가하는것
		새로운 가로열을 선택한 영역에 1개씩 추가하는것이다
		"""
		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)

		for y in range(y2 - y1 + 1, 0, -1):
			if divmod(y, step_no)[1] == 0:
				self.insert_yy(sheet_name, y+y1)

	def insert_yy(self, sheet_name="", yy="입력필요"):
		"""
		insert_yy(self, sheet_name="", yy):
		세로행을 한줄삽입하기
		"""
		sheet = self.check_sheet_name(sheet_name)
		yy =self.check_yy_address(yy)
		sheet.Columns(str(yy[0]) + ':' + str(yy[1])).Insert()

	def insert_sheet_new(self, new_name="입력필요"):
		"""
		*입력값없이 사용가능*
		insert_sheet_new(self, new_name)
		시트하나 추가하기
		"""
		if new_name in self.read_sheet_name_all():
			new_name = ""
			self.show_messagebox("같은 이름이있어 다른이름으로 하나 추가합니다")
		
		if new_name == "":
			self.xlBook.Worksheets.Add()
		else:
			self.xlBook.Worksheets.Add()
			old_name = self.xlApp.ActiveSheet.Name
			self.xlBook.Worksheets(old_name).Name = new_name

	def intersect_range1_range2(self, rng1="입력필요", rng2="입력필요"):
		"""
		두개의 영역에서 교차하는 구간을 돌려준다
		만약 교차하는게 없으면 ""을 돌려준다
		"""
		range_1 = self.check_address_value(rng1)
		range_2 = self.check_address_value(rng2)

		x11, y11, x12, y12 = range_1
		x21, y21, x22, y22 = range_2

		if x11 == 0:
			x11 = 1
			x12 = 1048576
		if x21 == 0:
			x21 = 1
			x22 = 1048576
		if y11 == 0:
			y11 = 1
			y12 = 16384
		if y21 == 0:
			y21 = 1
			y22 = 16384

		new_range_x = [x11, x21, x12, x22]
		new_range_y = [y11, y21, y12, y22]

		new_range_x.sort()
		new_range_y.sort()

		if x11 <= new_range_x[1] and x12 >= new_range_x[2] and y11 <= new_range_y[1] and y12 >= new_range_y[1]:
			result = [new_range_x[1], new_range_y[1], new_range_x[2], new_range_y[2]]
		else:
			result = "교차점없음"
		return result

	def lock_sheet_with_password(self, sheet_name):
		"""
		암호걸어 놓은 시트 풀기
		암호를 처음부터 하나하나씩 넣어가면서 비교검색한다
		이것은 샘플용으로 시간이 많이 걸리지 않도록 숫자만하였으며 4개 단위의 묶음으로 하였다
		itertools.product는 문자열을 원하는 형태의 묶음으로 만들어 주는 모듈이다
		아래의 에제와 같이 10개의 숫자중 4개씩만 대입을 전부다해 보면 약 30분의 시간이 걸린다
		그러니 일반적인 컴퓨터로 8글자정도에 알파벳과 특수문자가 들어가 있다면 시간은 상상이상으로 걸리니
		감안하시고 적용하시기를 바랍니다
		"""
		source_letter = "1234567890"
		repeat_no = 4


		count = 0

		time_start = self.read_time_now()
		for a in itertools.product(source_letter, repeat=repeat_no):
			print(a)
			count += 1
			print(count)
			temp_pwd = ("".join(map(str, a)))
			try:
				self.set_sheet_unlock(sheet_name, temp_pwd)
				print("확인함==>", a)
			except:
				pass
			else:
				print("password is ==>", temp_pwd)
				break
		print(time_start)
		print(self.read_time_now())
		print(count)

	def move_rangevalue_linevalue(self, sheet_name="", xyxy=""):
		"""
		*입력값없이 사용가능*
		move_value_01(self, sheet_name="", xyxy=""):
		선택한영역의 자료를 세로의 한줄로 만드는것

		새로운 세로행을 만든후 그곳에 두열을 서로 하나씩 포개어서 값넣기
		a 1  ==> a
		b 2     1
		       b
		       2
		"""

		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)

		output_list = self.read_range_value(sheet_name, xyxy)
		make_one_list = self.util.list_change_2d_1d(output_list)
		self.insert_yy(sheet_name, y2+1)
		self.write_range_value_ydirection_only(sheet_name, [x1, y2+1], make_one_list)

	def move_range_ystep(self, sheet_name="", xyxy="", input_y="입력필요", step="입력필요"):
		"""
		가로의 자료를 설정한 갯수만큼 한줄로 오른쪽으로 이동
		"""
		new_x = 0
		new_y = input_y

		for x in range(xyxy[0], xyxy[2] + 1):
			for y in range(xyxy[1], xyxy[3] + 1):
				new_x = new_x + 1
				value = self.read_cell_value("", [x, y])
				if value == None:
					value = ""
				self.write_cell_value("", [new_x, new_y], value)
				print(value)

	def move_compare_2sheets(self):
		"""
		전체가 빈 가로열 삭제
		두개의 시트에서 기준시트와 똑같은 열로 다른 시트를 옮기는것이름으로

		1. 현재의 시트 이름을 알아온다
		2. 옮길 시트이름을 얻는다
		3. 기준시트의 사용된영역중 첫번째 열의 모든 내용을 읽어온다
		4. 옮길시트의 사용된영역중 첫번째 열의 모든 내용을 읽어온다
		5. 두개를 비교해서 몇번째로 이동을 할것인지 새로운 기준시트의 첫번째 열의 모든 내용을 읽어와서 하나씩 비교를 한다
		"""

		sheet_name_1 = self.read_activesheet_name()
		sheet_name_2 = self.read_messagebox_value()

		var_1 = self.read_range_usedrange(sheet_name_1)[2]
		var_2 = self.read_range_usedrange(sheet_name_2)[2]
		sheet_1_end_num = self.change_address_type(var_1)[1][2]
		sheet_2_end_num = self.change_address_type(var_1)[1][2]

		for y1 in range(1, sheet_1_end_num + 1):
			var_3 = self.read_cell_value(sheet_name_1, [1, y1])
			var_5 = 0
			for y2 in range(1, sheet_2_end_num):
				var_4 = self.read_cell_value(sheet_name_2, [1, y2])
				if var_3 == var_4 and var_5 == 0:
					self.insert_range_sero(sheet_name_2, y1)
					self.copy_range_sero(sheet_name_2, sheet_name_2, y2 + 1, y1)
					self.delete_range_sero(sheet_name_2, y2 + 1)
					var_5 = 1
			if var_5 == 0:
				self.insert_range_sero(sheet_name_2, y1)
				sheet_2_end_num = sheet_2_end_num + 1

	def move_degree_distance(self, degree="입력필요", distance="입력필요"):
		"""
		현재 위치 x,y에서 30도로 20만큼 떨어진 거리의 위치를 돌려주는 것
		"""
		degree = degree * 3.141592 / 180
		x = distance * math.cos(degree)
		y = distance * math.sin(degree)
		return [x, y]

	def move_range_bottom(self, sheet_name="", xyxy=""):
		"""
		*입력값없이 사용가능*
		선택한 위치에서 끝부분으로 이동하는것
		xlDown : - 4121, xlToLeft : - 4159, xlToRight : - 4161, xlUp : - 4162
		"""
		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)

		sheet.Cells(x1, y1).End(- 4121).Select()

	def move_range_top(self, sheet_name="", xyxy=""):
		"""
		*입력값없이 사용가능*
		선택한 위치에서 끝부분으로 이동하는것
		xlDown : - 4121, xlToLeft : - 4159, xlToRight : - 4161, xlUp : - 4162
		"""
		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)

		sheet.Cells(x1, y1).End(- 4162).Select()

	def move_range_leftend(self, sheet_name="", xyxy=""):
		"""
		*입력값없이 사용가능*
		선택한 위치에서 끝부분으로 이동하는것
		xlDown : - 4121, xlToLeft : - 4159, xlToRight : - 4161, xlUp : - 4162
		"""
		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)

		sheet.Cells(x1, y1).End(- 4159).Select()

	def move_range_rightend(self, sheet_name="", xyxy=""):
		"""
		*입력값없이 사용가능*
		선택한 위치에서 끝부분으로 이동하는것
		xlDown : - 4121, xlToLeft : - 4159, xlToRight : - 4161, xlUp : - 4162
		"""
		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)

		sheet.Cells(x1, y1).End(- 4161).Select()

	def move_value_without_empty_cell_01(self, sheet_name="", xyxy=""):
		"""
		*입력값없이 사용가능*
		선택한 영역에서 세로의 값중에서 빈셀을 만나면
		아래의 값중 있는것을 위로 올리기
		전체영역의 값을 읽어오고,
		하나씩 다시 쓴다
		"""

		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)

		read_data = self.read_range_value(sheet_name, xyxy)
		self.delete_range_value(sheet_name, xyxy)

		for y in range(y1, y2 + 1):
			new_x = x1
			for x in range(x1, x2 + 1):
				value = self.read_cell_value(sheet_name, [x, y])
				if value !="":
					self.write_cell_value(sheet_name, [new_x, y])
					new_x = new_x +1

	def move_x(self, sheet_list="입력필요", xx_list="입력필요"):
		"""
		세로의 값을 이동시킵니다
		"""
		sheet1 = self.check_sheet_name(sheet_list[0])
		sheet2 = self.check_sheet_name(sheet_list[1])

		xx0_1, xx0_2 = self.check_xy_address(xx_list[0])
		xx1_1, xx1_2 = self.check_xy_address(xx_list[1])

		xx0_1 = self.change_char_num(xx0_1)
		xx0_2 = self.change_char_num(xx0_2)
		xx1_1 = self.change_char_num(xx1_1)
		xx1_2 = self.change_char_num(xx1_2)

		sheet1.Select()
		sheet1.Rows(str(xx0_1) + ':' + str(xx0_2)).Select()
		sheet1.Rows(str(xx0_1) + ':' + str(xx0_2)).Copy()
		sheet2.Select()
		sheet2.Rows(str(xx1_1) + ':' + str(xx1_2)).Select()
		sheet2.Rows(str(xx1_1) + ':' + str(xx1_2)).Insert()

		if sheet1 == sheet2:
			if xx0_1 <= xx1_1:
				sheet1.Rows(str(xx0_1) + ':' + str(xx0_2)).Delete()
			else:
				new_xx0_1 = self.change_num_char(xx0_1 + xx1_2 - xx1_1)
				new_xx0_2 = self.change_num_char(xx0_2 + xx1_2 - xx1_1)
				sheet1.Rows(str(new_xx0_1) + ':' + str(new_xx0_2)).Delete()
		else:
			sheet1.Rows(str(xx0_1) + ':' + str(xx0_2)).Delete()

	def move_y(self, sheet_list="입력필요", yy_list="입력필요"):
		"""
		# 가로의 값을 이동시킵니다
		"""
		range_1 = self.check_range_yy(sheet_list[0], yy_list[0])
		range_2 = self.check_range_yy(sheet_list[1], yy_list[1])

		range_1.Select()
		range_1.Cut()

		range_2.Select()
		range_2.Insert()

	def paint_cell_color(self, sheet_name="", xyxy="", input_data="입력필요"):
		"""
		선택 셀에 색깔을 넣는다
		"""
		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		my_range = sheet.Range(sheet.Cells(x1, y1), sheet.Cells(x2, y2))
		rgb_to_int = self.check_color_style(input_data)[1]
		my_range.Interior.Color = rgb_to_int

	def paint_cell_fontcolor(self, sheet_name="", xyxy="", font_color="입력필요"):
		"""
		선택한 하나의 셀에 글씨체를 설정한다
		"""
		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		my_range = sheet.Range(sheet.Cells(x1, y1), sheet.Cells(x2, y2))

		result_rgb = self.check_color(font_color)
		my_range.Font.Color = self.rgb_to_hex(result_rgb)[3]

	def paint_range_rgbcolor(self, sheet_name="", xyxy="", input_data="입력필요"):
		"""
		paint_range_rgbcolor(sheet_name, xyxy, input_data)
		영역에 rgb 색깔을 입힌다
		엑셀에서의 색깔의 번호는 아래의 공식처럼 만들어 진다
		"""
		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		my_range = sheet.Range(sheet.Cells(x1, y1), sheet.Cells(x2, y2))

		rgb_to_int = (int(input_data[2])) * (256 ** 2) + (int(input_data[1])) * 256 + int(input_data[0])
		my_range.Interior.Color = rgb_to_int

	def paint_range_color(self, sheet_name="", xyxy="", color_value="입력필요"):
		"""
		영역에 색깔을 입힌다
		"""
		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		my_range = sheet.Range(sheet.Cells(x1, y1), sheet.Cells(x2, y2))

		input_data = self.color.get_rgb(color_value)

		rgb_to_int = (int(input_data[2])) * (256 ** 2) + (int(input_data[1])) * 256 + int(input_data[0])
		my_range.Interior.Color = rgb_to_int

	def paint_cell_rgb(self, sheet_name="", xyxy="", input_rgb="입력필요"):
		self.paint_cell_rgbcolor(sheet_name, xyxy, input_rgb)

	def paint_cell_rgbcolor(self, sheet_name="", xyxy="", input_rgb="입력필요"):
		"""
		paint_cell_rgbcolor(sheet_name, xyxy, input_rgb)
		"""
		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		my_range = sheet.Range(sheet.Cells(x1, y1), sheet.Cells(x2, y2))

		# RGB값을 색칠하는 방법
		rgb_to_int = (int(input_rgb[2])) * (256 ** 2) + (int(input_rgb[1])) * 256 + int(input_rgb[0])
		my_range.Interior.Color = rgb_to_int

	def paint_spacecell_color(self, sheet_name="", xyxy=""):
		"""
		*입력값없이 사용가능*
		빈셀처럼 보이는데 space문자가 들어가 있는것 찾기
		1. 선택한 영역의 셀을 하나씩 읽어와서 re모듈을 이용해서 공백만 있는지 확인한다
		"""
		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)

		for x in range(x1, x2 + 1):
			for y in range(y1, y2 + 1):
				cell_value = self.read_cell_value(sheet_name, [x, y])
				com = re.compile("^\s+")
				if cell_value != None:
					if com.search(cell_value):
						self.paint_cell_color(sheet_name, [x, y], 4)

	def paint_range_fontcolor(self, sheet_name="", xyxy="", font_color="입력필요"):
		"""
		paint_range_fontcolor(sheet_name, xyxy, font_color)
		영역에 글씨체를 설정
		"""
		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		my_range = sheet.Range(sheet.Cells(x1, y1), sheet.Cells(x2, y2))

		input_data = self.color.get_rgb(font_color)

		rgb_to_int = (int(input_data[2])) * (256 ** 2) + (int(input_data[1])) * 256 + int(input_data[0])
		my_range.Font.Color = rgb_to_int

	def paint_range_wellusedline(self, sheet_name="", xyxy=""):
		# 이 이름을 더 많이 내가 사용하는것같다
		self.paint_range_mystyle(sheet_name, xyxy)

	def paint_range_mystyle(self, sheet_name="", xyxy=""):
		"""
		*입력값없이 사용가능*
		paint_range_line_form1(sheet_name, xyxy)
		# 내가 자주사용하는 형태의 라인
		# [선의위치, 라인스타일, 굵기, 색깔]
		# 입력예 : [7,1,2,1], ["left","-","t0","bla"]
		# 선의위치 (5-대각선 오른쪽, 6-왼쪽대각선, 7:왼쪽, 8;위쪽, 9:아래쪽, 10:오른쪽, 11:안쪽세로, 12:안쪽가로)
		# 라인스타일 (1-실선, 2-점선, 3-가는점선, 6-굵은실선,
		# 굵기 (0-이중, 1-얇게, 2-굵게)
		# 색깔 (0-검정, 1-검정, 3-빨강),
		"""
		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)

		line_list_head = [
			["left", "basic", "t-2", "red"],
			["top", "basic", "t-2", "black"],
			["right", "basic", "t-2", "red"],
			["bottom", "basic", "t-2", "black"],
			["inside-h", "basic", "t-2", "black"],
			["inside-v", "basic", "t-2", "black"],
		]

		line_list_body = [
			["left", "basic", "basic", "black"],
			["top", "basic", "basic", "black"],
			["right", "basic", "basic", "black"],
			["bottom", "basic", "basic", "black"],
			["inside-h", "basic", "basic", "black"],
			["inside-v", "basic", "basic", "black"],
		]

		line_list_tail = [
			["left", "basic", "t0", "black"],
			["top", "basic", "t0", "red"],
			["right", "basic", "t0", "red"],
			["bottom", "basic", "basic", "red"],
			["inside-h", "basic", "basic", "red"],
			["inside-v", "basic", "basic", "red"],
		]

		print(line_list_head)
		range_head = [x1, y1, x1, y2]
		range_body = [x1 + 1, y1, x2 - 1, y2]
		range_tail = [x2, y1, x2, y2]

		for one in line_list_head:
			self.paint_range_line("", range_head, one)

		for one in line_list_body:
			self.paint_range_line("", range_body, one)

		for one in line_list_tail:
			self.paint_range_line("", range_tail, one)

	def paint_range_line(self, sheet_name="", xyxy="", input_list="입력필요"):
		"""
		# [선의위치, 라인스타일, 굵기, 색깔]
		# 입력예 : [7,1,2,1], ["left","-","t0","bla"]
		# 선의위치 (5-대각선 오른쪽, 6-왼쪽대각선, 7:왼쪽, 8;위쪽, 9:아래쪽, 10:오른쪽, 11:안쪽세로, 12:안쪽가로)
		# 라인스타일 (1-실선, 2-점선, 3-가는점선, 6-굵은실선,
		# 굵기 (0-이중, 1-얇게, 2-굵게)
		# 색깔 (0-검정, 1-검정, 3-빨강),
		"""

		line_type = self.common_data["excel_line_type"]
		line_style_dic = self.common_data["excel_line_style_dic"]
		color_index_dic = self.common_data["excel_color_index_by_color"]
		weight_dic = self.common_data["excel_weight_dic"]

		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		my_range = sheet.Range(sheet.Cells(x1, y1), sheet.Cells(x2, y2))

		my_range.Borders(line_type[input_list[0]]).Colorindex = color_index_dic[input_list[3]]
		my_range.Borders(line_type[input_list[0]]).Weight = weight_dic[input_list[2]]
		my_range.Borders(line_type[input_list[0]]).LineStyle = line_style_dic[input_list[1]]

	def paint_xline_minvalue(self, sheet_name="", xyxy=""):
		"""
		*입력값없이 사용가능*
		paint_xline_minvalue(self, sheet_name="", xyxy=""):
		가로열의 최소값에 색을 칠하는것이다
		# 읽어온 값중에서 열별로 최소값구한후 색칠 하기
		"""
		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)

		all_data = self.read_range_value(sheet_name, [x1, y1, x2, y2])

		if not (x1 == x2 and y1 == y2):
			for line_no in range(len(all_data)):
				line_data = all_data[line_no]
				filteredList = list(filter(lambda x: type(x) == type(1) or type(x) == type(1.0), line_data))
				if filteredList == []:
					pass
				else:
					max_value = min(filteredList)
					x_location = x1 + line_no
					for no in range(len(line_data)):
						y_location = y1 + no
						if (line_data[no]) == max_value:
							self.paint_cell_color(sheet_name, [x_location, y_location], 3)
		else:
			print("Please re-check selection area")

	def paint_range_color_bywords(self, sheet_name="", xyxy=""):
		"""
		# 선택한 영역의 각셀에 아래의 글자가 모두 들어있는 셀에 초록색으로 배는경색 칠하기
		# 1. 원하자료를 inputbox를 이용하여,를 사용하여 받는다
		# 2. split함수를 이용하여 리스트로 만들어
		# 3. 전부 만족한것을 for문으로 만들어 확인한후 색칠을 한다
		"""
		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)

		bbb = self.read_messagebox_value("Please input text : in, to, his, with")

		basic_list = []
		for one_data in bbb.split(","):
			basic_list.append(one_data.strip())
		total_no = len(basic_list)

		for x in range(x1, x2 + 1):
			for y in range(y1, y2 + 1):
				cell_value = str(self.read_cell_value(sheet_name, [x, y]))
				temp_int = 0
				for one_word in basic_list:
					if re.match('(.*)' + one_word + '(.*)', cell_value):
						temp_int = temp_int + 1
				if temp_int == total_no:
					self.paint_cell_color(sheet_name, [x, y], 4)

	def paint_range_max_num_1(self, sheet_name="", xyxy=""):
		"""
		*입력값없이 사용가능*
		# 읽어온 값중에서 최대값구하기
		"""
		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)

		all_data = self.read_range_value(sheet_name, [x1, y1, x2, y2])

		print(all_data)
		if not (x1 == x2 and y1 == y2):
			for line_no in range(len(all_data)):
				line_data = all_data[line_no]
				filteredList = list(filter(lambda x: type(x) == type(1) or type(x) == type(1.0), line_data))
				if filteredList == []:
					pass
				else:
					max_value = max(filteredList)
					x_location = x1 + line_no
					for no in range(len(line_data)):
						y_location = y1 + no
						if (line_data[no]) == max_value:
							self.paint_cell_color(sheet_name, [x_location, y_location], 16)
		else:
			print("Please re-check selection area")

	def paint_range_specific_text(self, sheet_name="", xyxy=""):
		"""
		"""
		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)

		selection_range = x1, y1, x2, y2
		datas = list(self.read_range_value(sheet_name, selection_range))

		temp = []
		result = []
		min_value = []

		print(datas)

		input_text = self.read_messagebox_value()

		for data_xx in datas:
			temp_list = []
			temp_num = 0
			for data_x in data_xx:
				if str(input_text) in str(data_x) and data_x != None:
					self.set_range_color(sheet_name, [x1, y1 + temp_num, x1, y1 + temp_num], 6)
				temp_num = temp_num + 1
			x1 = x1 + 1

	def print_letter_cover(self, ):
		"""
		봉투인쇄
		"""

		# 기본적인 자료 설정
		data_from = [["sheet1", [1, 2]], ["sheet1", [1, 4]], ["sheet1", [1, 6]], ["sheet1", [1, 8]]]
		data_to = [["sheet2", [1, 2]], ["sheet2", [2, 2]], ["sheet2", [3, 2]], ["sheet2", [2, 3]]]

		no_start = 1
		no_end = 200
		step = 5

		# 실행되는 구간
		for no in range(no_start, no_end):
			for one in range(len(data_from)):
				value = self.read_cell_value(data_from[one][0], data_from[one][1])
				self.write_cell_value(data_to[one][0], [data_to[one][1][0] + (step * no), data_to[one][1][1]], value)

	def print_preview(self, sheet_name=""):
		"""
		미리보기기능입니다
		"""
		sheet = self.check_sheet_name(sheet_name)
		sheet.PrintPreview()

	def read_activecell_address(self):
		"""
		현재 activecell의 주소값을 읽는다
		돌려주는 값 [x, y]
		"""
		xyxy = self.check_address_value(self.xlApp.ActiveCell.Address)
		return xyxy

	def read_activecell_value(self):
		"""
		현재 activecell의 값을 읽는다
		"""
		return self.xlApp.ActiveCell.Value

	def read_activesheet_name(self):
		"""
		현재의 활성화된 시트의 이름을 돌려준다
		"""
		return self.xlApp.ActiveSheet.Name

	def read_cell_value(self, sheet_name="", xyxy=""):
		"""
		값을 일정한 영역에서 갖고온다
		만약 영역을 두개만 주면 처음과 끝의 영역을 받은것으로 간주해서 알아서 처리하도록 변경하였다
		"""
		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		result = sheet.Cells(x1, y1).Value
		if result == None:
			result = ""
		return result

	def read_cell_address(self):
		"""
		#이런 이름의 함수도 있으면 좋지 않을까 해서 만듦
		"""
		result = self.read_activecell_address()
		return result

	def read_cell_coord(self,sheet_name="", xyxy=""):
		"""
		#셀의 픽셀 좌표를 갖고온다
		"""
		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		my_range = sheet.Range(sheet.Cells(x1, y1), sheet.Cells(x2, y2))

		rng_x_coord = my_range.Left
		rng_y_coord = my_range.Top
		rng_width = my_range.Width
		rng_height = my_range.Height
		return [rng_x_coord,rng_y_coord, rng_width,rng_height]

	def read_cell_color(self, sheet_name="", xyxy=""):
		"""
		셀의 색을 읽어온다
		"""
		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		my_range = sheet.Range(sheet.Cells(x1, y1), sheet.Cells(x2, y2))

		result = my_range.Interior.Color
		return result

	def read_cell_memo(self, sheet_name="", xyxy=""):
		"""
		메모를 읽어오는 것
		"""
		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		my_range = sheet.Range(sheet.Cells(x1, y1), sheet.Cells(x2, y2))

		result = my_range.Comment.Text()
		return result

	def read_continousrange_value(self, sheet_name="", xyxy=""):
		"""
		# 현재선택된 셀을 기준으로 연속된 영역을 가지고 오는 것입니다
		"""
		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)

		row = xyxy
		col = xyxy

		sheet = self.xlBook.Worksheets(sheet_name)
		bottom = row # 아래의 행을 찾는다
		while sheet.Cells(bottom + 1, col).Value not in [None, '']:
			bottom = bottom + 1
		right = col # 오른쪽 열
		while sheet.Cells(row, right + 1).Value not in [None, '']:
			right = right + 1
		return sheet.Range(sheet.Cells(row, col), sheet.Cells(bottom, right)).Value

	def read_currentregion_address(self, sheet_name="", xy=""):
		"""
		이것은 현재의 셀에서 공백과 공백열로 둘러싸인 활성셀영역을 돌려준다
		"""
		result = self.check_address_value(self.xlApp.ActiveCell.CurrentRegion.Address)
		return result

	def read_general_value(self):
		"""
		몇가지 엑셀에서 자주사용하는 것들정의
		엑셀의 사용자, 현재의 경로, 화일이름, 현재시트의 이름
		"""
		result = []
		result.append(self.xlApp.ActiveWorkbook.Name)
		result.append(self.xlApp.Username)
		result.append(self.xlApp.ActiveWorkbook.ActiveSheet.Name)
		return result

	def read_inputbox_value(self, title="Please Input Value"):
		"""
		inputbox로 입력값을 받는다
		"""
		temp_result = self.xlApp.Application.InputBox(title)
		return temp_result

	def read_range_address(self):
		"""
		현재 영역의 주소값을 읽어온다
		"""
		temp_address = self.xlApp.Selection.Address
		result = self.check_address_value(temp_address)
		return result

	def read_range_value(self, sheet_name="", xyxy=""):
		"""
		값을 일정한 영역에서 갖고온다
		만약 영역을 두개만 주면 처음과 끝의 영역을 받은것으로 간주해서 알아서 처리하도록 변경하였다
		"""
		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		my_range = sheet.Range(sheet.Cells(x1, y1), sheet.Cells(x2, y2))

		temp_result = my_range.Value
		result = []
		if 1 < len(temp_result):
			for one_data in temp_result:
				result.append(list(one_data))
		else:
			result = temp_result
		return result

	def read_rangename_address(self, sheet_name="", range_name="입력필요"):
		"""
		read_rangename_address(sheet_name, range_name)
		이름영역의 주소값을 돌려준다
		"""
		sheet = self.check_sheet_name(sheet_name)
		temp = sheet.Range(range_name).Address
		result = self.check_address_value(temp)
		return result

	def read_rangename_all(self):
		"""
		*입력값없이 사용가능*
		현재 시트의 이름을 전부 돌려준다
		[번호, 영역이름, 영역주소]
		"""
		names_count = self.xlBook.Names.Count
		result = []
		if names_count > 0:
			for aaa in range(1, names_count + 1):
				name_name = self.xlBook.Names(aaa).Name
				name_range = self.xlBook.Names(aaa)
				result.append([aaa, str(name_name), str(name_range)])
		return result

	def read_selection_address(self):
		"""
		현재선택된 영역의 주소값을 돌려준다
		"""
		result = ""
		temp_address = self.xlApp.Selection.Address
		print(temp_address)
		temp_list = temp_address.split(",")
		if len(temp_list) == 1:
			result = self.check_address_value(temp_address)
		if len(temp_list) > 1:
			result = []
			for one_address in temp_list:
				result.append(self.check_address_value(one_address))
		return result

	def read_selection_value(self, sheet_name="", xyxy=""):
		"""
		값을 일정한 영역에서 갖고온다
		만약 영역을 두개만 주면 처음과 끝의 영역을 받은것으로 간주해서 알아서 처리하도록 변경하였다
		"""
		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		my_range = sheet.Range(sheet.Cells(x1, y1), sheet.Cells(x2, y2))

		result = my_range.Value
		return result

	def read_shape_name(self, sheet_name="", shape_no="입력필요"):
		"""
		read_shape_name(sheet_name, shape_no)
		"""
		sheet = self.check_sheet_name(sheet_name)
		result = sheet.Shapes(shape_no).Name

		return result

	def read_sheet_count(self):
		"""
		시트의 갯수를 돌려준다
		"""
		return self.xlBook.Worksheets.Count

	def read_sheet_name_all(self):
		"""
		현재 워크북의 모든 시트알아내기
		"""
		temp_list = []
		for var_02 in range(1, self.read_sheet_count() + 1):
			temp_list.append(self.xlBook.Worksheets(var_02).Name)
		return temp_list

	def read_usedrange_address(self, sheet_name=""):
		"""
		# 이것은 usedrange를 돌려주는 것이다. 값은 리스트이며 처음은
		# usedrange의 시작셀 ,두번째는 마지막셀값이며 세번째는 전체영역을 돌려주는 것이다
		"""
		sheet = self.check_sheet_name(sheet_name)
		result = self.check_address_value(sheet.UsedRange.address)
		return result

	def read_username(self):
		"""
		사용자 이름을 읽어온다
		"""
		return self.xlApp.Username

	def read_workbook_fullname(self):
		"""
		application의 이름과 전체경로를 돌려준다
		"""
		return self.xlBook.FullName

	def read_workbook_name(self):
		"""
		application의 이름을 돌려준다
		"""
		return self.xlBook.Name

	def read_workbook_path(self):
		"""
		application의 경로를 돌려준다
		"""
		return self.xlBook.Path

	def read_xx_value(self, sheet_name="", xx="입력필요"):
		"""
		가로줄들의 전체의 값을 읽어온다
		"""
		sheet = self.xlBook.Worksheets(sheet_name)
		return sheet.Range(sheet.Cells(xx[0], 1), sheet.Cells(xx[1], 1)).EntireRow.Value

	def read_yy_value(self, sheet_name="", yy="입력필요"):
		"""
		세로줄들의 전체값을 갖고온다
		"""
		sheet = self.xlBook.Worksheets(sheet_name)
		return sheet.Range(sheet.Cells(1, yy[0]), sheet.Cells(1, yy[1])).EntireColumn.Value

	def replace_range_word_many(self, sheet_name="", xyxy="", input_list="입력필요"):
		"""
		선택한 영역의 한번에 여러단어 바꾸기
		이것은 메세지로 입력받기는 어려워 실제 코드에 바꿀 문자들을 입력바랍니다
		words=[["가나","다라"],["짜장면","자장면"],	["효꽈","효과"],]
		"""
		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)

		for x in range(x1, x2 + 1):
			for y in range(y1, y2 + 1):
				cell_value = str(self.read_cell_value(sheet_name, [x, y]))
				for one_list in input_list:
					cell_value = cell_value.replace(one_list[0], one_list[1])
				self.write_cell_value(sheet_name, [x, y + 1], cell_value)

	def save(self, newfilename="입력필요"):
		"""
		엑셀화일을 저장하는 것이다
		별도의 지정이 없으면 기존의 화일이름으로 저장합니다
		"""
		if newfilename == "":
			self.xlBook.Save()
		else:
			print(newfilename)
			self.xlBook.SaveAs(newfilename)

	def screen_update_off(self):
		"""
		스크린 update를 멈추는것
		"""
		self.xlApp.ScreenUpdating = False

	def screen_update_on(self):
		"""
		스크린 update를 다시시작한다
		"""
		self.xlApp.ScreenUpdating = True

	def select_cell(self, sheet_name="", xyxy=""):
		"""
		하나의 셀을 선택한다
		"""
		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		my_range = sheet.Range(sheet.Cells(x1, y1), sheet.Cells(x2, y2))
		my_range.Select()

	def select_range(self, sheet_name="", xyxy=""):
		"""
		영역을 선택한다
		"""
		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		my_range = sheet.Range(sheet.Cells(x1, y1), sheet.Cells(x2, y2))
		my_range.Select()

	def select_sheet(self, sheet_name=""):
		"""
		시트를 활성화 시킨다
		"""
		self.xlBook.Worksheets(sheet_name).Select()

	def set_cell_bold(self, sheet_name="", xyxy=""):
		"""
		셀안의 값을 진하게 만든다
		"""
		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		my_range = sheet.Range(sheet.Cells(x1, y1), sheet.Cells(x2, y2))

		my_range.Font.Bold = True

	def set_cell_font_rgb(self, sheet_name="", xyxy="", rgb="입력필요"):
		"""
		영역에 글씨의 색상을 설정한다
		"""
		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		my_range = sheet.Range(sheet.Cells(x1, y1), sheet.Cells(x2, y2))

		my_range.Font.Color = int(rgb[0])+int(rgb[1])*256+int(rgb[2])*65536

	def set_column_numberproperty(self, sheet_name="", num_col="입력필요", style="입력필요"):
		"""
		각 열을 기준으로 셀의 속성을 설정하는 것이다
		"""
		sheet = self.xlBook.Worksheets(sheet_name)
		if style == 1: # 날짜의 설정
			sheet.Columns(num_col).NumberFormatLocal = "mm/dd/yy"
		elif style == 2: # 숫자의 설정
			sheet.Columns(num_col).NumberFormatLocal = "_-* #,##0.00_-;-* #,##0.00_-;_-* '-'_-;_-@_-"
		elif style == 3: # 문자의 설정
			sheet.Columns(num_col).NumberFormatLocal = "@"

	def set_formula(self, sheet_name="", xyxy="", input_formular="입력필요"):
		"""
		예 : sheet.Cells(5, 2).Formula = "=Now()"
		"""
		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		my_range = sheet.Range(sheet.Cells(x1, y1), sheet.Cells(x2, y2))

		my_range.Formula = str(input_formular)

	def set_fullscreen(self, fullscreen=1):
		"""
		전체화면으로 보기
		"""
		self.xlApp.DisplayFullScreen = fullscreen

	def set_gridline_off(self):
		"""
		*입력값없이 사용가능*
		그리드 라인을 없앤다
		"""
		self.xlApp.ActiveWindow.DisplayGridlines = 0

	def set_gridline_on(self):
		"""
		*입력값없이 사용가능*
		그리드 라인을 나타낸다
		"""
		self.xlApp.ActiveWindow.DisplayGridlines = 1

	def set_range_font(self, sheet_name="", xyxy="", font="입력필요"):
		"""
		영역에 글씨체를 설정한다
		"""
		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		my_range = sheet.Range(sheet.Cells(x1, y1), sheet.Cells(x2, y2))

		my_range.Font.Name = font

	def set_range_fontsize(self, sheet_name="", xyxy="", size="입력필요"):
		"""
		영역에 글씨크기를 설정한다
		"""
		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		my_range = sheet.Range(sheet.Cells(x1, y1), sheet.Cells(x2, y2))

		my_range.Font.Size = int(size)

	def set_range_formula(self, sheet_name="", xyxy="", input_data="입력필요"):
		"""
		영역에 수식을 넣는것
		"""
		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		my_range = sheet.Range(sheet.Cells(x1, y1), sheet.Cells(x2, y2))

		my_range.Formula = "=Now()"
		my_range.Value = input_data

	def set_range_merge(self, sheet_name="", xyxy=""):
		"""
		*입력값없이 사용가능*
		셀들을 병합하는 것
		"""
		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		my_range = sheet.Range(sheet.Cells(x1, y1), sheet.Cells(x2, y2))
		my_range.Merge(0)

	def set_range_numberformat(self, sheet_name="", xyxy="", numberformat="입력필요"):
		"""
		영역에 숫자형식을 지정하는 것이다
		"""
		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		my_range = sheet.Range(sheet.Cells(x1, y1), sheet.Cells(x2, y2))
		my_range.NumberFormat = numberformat

	def set_range_unmerge(self, sheet_name="", xyxy=""):
		"""
		*입력값없이 사용가능*
		영역안의 병합된 것을 푸는 것이다
		"""
		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		my_range = sheet.Range(sheet.Cells(x1, y1), sheet.Cells(x2, y2))
		my_range.UnMerge()

	def set_range_name(self, sheet_name="", xyxy="", name="입력필요"):
		"""
		영역에 이름으로 설정하는 기능
		"""
		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		my_range = sheet.Range(sheet.Cells(x1, y1), sheet.Cells(x2, y2))

		self.xlBook.Names.Add(name, my_range)

	def set_range_autofilter(self, sheet_name="", column1="입력필요", column2=None):
		"""
		엑셀의 자동필터 기능을 추가한 것입니다
		"""
		sheet = self.check_sheet_name(sheet_name)
		if column2 == None:
			column2 = column1
		a = str(column1) + ':' + str(column2)
		sheet.Columns(a).Select()
		sheet.Range(a).AutoFilter(1)

	def set_range_autofit(self, sheet_name="", xyxy=""):
		"""
		자동 열맞춤을 실행
		"""
		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)

		new_y1 = self.change_num_char(y1)
		new_y2 = self.change_num_char(y2)

		if xyxy == "":
			sheet.EntireColumn.AutoFit()
		else:
			sheet.Columns(str(new_y1) + ':' + str(new_y2)).AutoFit()

	def set_range_bold(self, sheet_name="", xyxy=""):
		"""
		영역안의 글씨체를 진하게 만든다
		"""
		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		my_range = sheet.Range(sheet.Cells(x1, y1), sheet.Cells(x2, y2))

		my_range.Font.Bold = True

	def set_range_xx(self, sheet_name="", xx="입력필요"):
		"""
		입력값 : [2,4]
		결과  = x열 2~3까지의 모든셀을 영역을 돌려준다
		"""
		result = self.check_range_xx(sheet_name, xx)
		return result

	def set_range_yy(self, sheet_name="", yy="입력필요"):
		"""
		입력값 : [2,4]
		결과  = y열 2~3까지의 모든셀을 영역을 돌려준다
		"""
		result = self.check_range_xx(sheet_name, yy="입력필요")
		return result

	def set_sheet_lock(self, sheet_name="", password="1234"):
		"""
		시트 잠그기
		"""
		sheet = self.check_sheet_name(sheet_name)
		sheet.protect(password)

	def set_sheet_unlock(self, sheet_name="", password="1234"):
		"""
		시트 잠그기 해제
		"""
		sheet = self.check_sheet_name(sheet_name)
		sheet.Unprotect(password)

	def set_visible(self, value=1):
		"""
		실행되어있는 엑셀을 화면에 보이지 않도록 설정합니다
		기본설정은 보이는 것으로 되너 있읍니다
		"""

		self.xlApp.Visible = value

	def set_xx_height(self, sheet_name="", xx="입력필요", height=13.5):
		"""
		가로줄의 높이를 설정
		"""
		my_range = self.check_range_xx(sheet_name, xx)
		my_range.RowHeight = height

	def set_xx_numberproperty(self, sheet_name="", x0="입력필요", style="입력필요"):
		"""
		각 열을 기준으로 셀의 속성을 설정하는 것이다
		"""
		sheet = self.check_sheet_name(sheet_name)
		x1 = self.check_xy_address(x0)
		x = self.change_char_num(x1)
		if style == 1: # 날짜의 설정
			sheet.Columns(x).NumberFormatLocal = "mm/dd/" \
												 ""
		elif style == 2: # 숫자의 설정
			sheet.Columns(x).NumberFormatLocal = "_-* #,##0.00_-;-* #,##0.00_-;_-* '-'_-;_-@_-"
		elif style == 3: # 문자의 설정
			sheet.Columns(x).NumberFormatLocal = "@"

	def set_yy_width(self, sheet_name="", yy="입력필요", width=13.5):
		"""
		가로열의 높이를 설정하는 것이다
		"""
		my_range = self.check_range_yy(sheet_name, yy)
		my_range.ColumnWidth =width

	def show_inputbox(self, title="Please Input Value"):
		"""
		inputbox로 입력값을 받는다
		"""
		temp_result = self.xlApp.Application.InputBox(title)
		return temp_result

	def show_messagebox(self, input_text="입력필요", input_title="pcell"):
		"""
		메세지를 나타낸다
		"""
		win32gui.MessageBox(0, input_text, input_title, 0)

	def test(self, input_text="입력필요"):
		"""
		메세지를 나타낸다
		"""
		win32gui.MessageBox(0, input_text, "테스트 입니다", 0)

	def split_as_special_string(self, input_text="입력필요"):
		"""
		선택한 1줄의 영역에서 원하는 문자나 글자를 기준으로 분리할때
		2개의 세로행을 추가해서 결과값을 쓴다
		"""
		sheet_name = self.read_activesheet_name()
		rng_select = self.read_selection_address()
		rng_used = self.read_usedrange_address()
		[x1, y1, x2, y2] = self.intersect_range1_range2(rng_select, rng_used)

		self.insert_yy("", y1 + 1)
		self.insert_yy("", y1 + 1)
		result = []
		length = 2

		# 자료를 분리하여 리스트에 집어 넣는다
		for x in range(x1, x2 + 1):
			for y in range(y1, y2 + 1):
				cell_value = str(self.read_cell_value(sheet_name, [x, y]))
				list_data = cell_value.split(input_text)
				result.append(list_data)

		# 집어넣은 자료를 다시 새로운 세로줄에 넣는다
		for x_no in range(len(result)):
			if len(result[x_no]) > length:
				for a in range(len(result[x_no]) - length):
					self.insert_yy("", y1 + length)
				length = len(result[x_no])
			for y_no in range(len(result[x_no])):
				self.write_cell_value(sheet_name, [x1 + x_no, y1 + y_no + 1], result[x_no][y_no])

	def trans_list(self, input_list2d="입력필요"):
		"""
		2차원자료를 행과열을 바꿔서 만드는것
		단, 길이가 같아야 한다
		"""
		checked_input_list2d = self.change_list_samelength(input_list2d)
		result = [list(x) for x in zip(*checked_input_list2d)]
		return result

	def trans_range_value(self, sheet_name="", xyxy="", values_d=""):
		"""
		선택한 영역의 값의 행렬을 바꿔서 새로운 시트를 만들어 [1,1]에 쓰기
		"""
		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)

		# 튜플로 되어있는 값을 리스트로 바꾸기
		values_l = []
		for one_data in values_d:
			values_l.append(list(one_data))

		# 리스트의 행과 열을 바꾸기
		result = numpy.transpose(values_d)
		return result

	def unique_range_value(self, sheet_name="", xyxy=""):
		"""
		선택한 영역에서 고유한값을 만들어서
		열 하나를 선택한후 나열하도록 한다
		"""
		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)


		data = self.read_range_value(sheet_name, xyxy)
		set1 = set([])
		for x in range(len(data)):
			for y in range(len(data[x])):
				set1.add(data[x][y])

		self.write_data_limitrange(sheet_name, list(set1))

	def write_activecell_value(self, xyxy="", value="입력필요"):
		"""
		write_activecell_value(xyxy, value)
		현재 활성화된 시트에 값을 넣는다
		"""
		self.xlApp.ActiveSheet.Cells(int(xyxy[0]), int(xyxy[1])).Value = str(value)

	def write_activerange_value(self, xyxy="", input_datas="입력필요"):
		"""
		현재시트에 값을 한번에 넣는 것
		"""
		x1,y1,x2,y2 = xyxy
		self.xlApp.ActiveSheet.Range(self.xlApp.ActiveSheet.Cells(x1, y1), self.xlApp.ActiveSheet.Cells(x1 + len(input_datas)-1, y1 + len(input_datas[0])-1)).Value = input_datas

	def write_cell_memo(self, sheet_name="", xyxy="", text="입력필요"):
		"""
		셀에 메모를 넣는 것
		"""
		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		my_range = sheet.Range(sheet.Cells(x1, y1), sheet.Cells(x2, y2))
		my_range.AddComment(text)

	def write_cell_value(self, sheet_name="", xyxy="", value="입력필요"):
		"""
		값을 셀에 넣는다.
		write_cell(시트이름, 행번호, 열번호, 넣을값)
		"""
		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)

		sheet.Cells(int(x1), int(y1)).Value = str(value)

	def write_emptycell_uppercell(self, sheet_name="", xyxy=""):
		self.fill_emptycell_uppercell(sheet_name, xyxy)

	def write_range_value(self, sheet_name="", xyxy="", input_datas="입력필요"):
		"""
		영역에 값을 써 넣는 것이다
		이것은 각셀을 하나씩 쓰는 것이다
		입력값과 영역이 맞지 않으면 입력값의 갯수를 더 우선함
		"""
		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)

		for x in range(len(input_datas)):
			for y in range(len(input_datas[x])):
				sheet.Cells(x1 + x, y1 + y).Value = input_datas[x][y]

	def write_range_value_linebase(self, sheet_name="", xyxy="", input_datas="입력필요"):
		"""
		영역에 값을 써 넣는 것이다
		이것은 각셀을 하나씩 쓰는 것이다
		입력값과 영역이 맞지 않으면 입력값의 갯수를 더 우선함
		"""
		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)

		for x in range(len(input_datas)):
			sheet.Range(sheet.Cells(x1, y1),
				sheet.Cells(x1 + len(input_datas) - 1, y1 + len(input_datas[0]) - 1)).Value = input_datas[x]

	def write_range_nansu(self, sheet_name="", xyxy="", input_data="입력필요"):
		"""
		write_range_nansu(sheet_name, xyxy, input_data)
		선택한 영역에 불규칙한 난수 발생하기
		난수는 선택한 영역에서 하나씩만 나오며
		영역이 더 크면, 다시 난수를 발생시켜서 추가로 입력한다
		"""
		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)

		no_start, no_end = input_data.split(",")
		no_start = int(no_start.strip())
		no_end = int(no_end.strip())
		basic_data = list(range(no_start, no_end + 1))
		random.shuffle(basic_data)
		temp_no = 0

		for x in range(x1, x2 + 1):
			for y in range(y1, y2 + 1):
				self.write_cell_value(sheet_name, [x, y], basic_data[temp_no])
				if temp_no >= no_end - no_start:
					random.shuffle(basic_data)
					temp_no = 0
				else:
					temp_no = temp_no + 1

	def write_range_value_trans(self, sheet_name="", xyxy="", input_list2d="입력필요"):
		"""
		읽어온 자료를 가로세로를 변환시킨다
		"""
		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		aaa = self.trans_list(input_list2d)

		for y in range(len(aaa)):
			sheet.Range(sheet.Cells(x1, y+y1), sheet.Cells(x2, y+y1)).Value = input_list2d[y]

	def write_range_value_ydirection_only(self, sheet_name="", xyxy="", input_list="입력필요"):
		"""
		1차원리스트의 자료를 가로로만 쓰는것
		"""
		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)

		if x2-x1 >= len(input_list):
			no_x = len(input_list)
		else:
			no_x = x2-x1

		for x in range(no_x):
			self.write_cell_value(sheet_name, [x1+x, y1],input_list[x])

	def __getattr__(self, name: str) -> int:
		#excel.activesheet처럼 함수가 아닌 클래스변수처럼 사용하는것
		result = ""
		if name == "activesheet":
			result = self.read_activesheet_name()
		if name == "activecell":
			result = self.read_activecell_value()
		return result

	def set_cell_numberformat (self, sheet_name="", xyxy="", type1="입력필요"):
		if type1=='general':
			result="#,##0.00_ "
		elif type1=='number':
			result="US$""#,##0.00"
		elif type1=='account':
			result="_-""US$""* #,##0.00_ ;_-""US$""* -#,##0.00 ;_-""US$""* ""-""??_ ;_-@_ "
		elif type1=='date':
			result="mm""/""dd""/""yy"
		elif type1=='datetime':
			result="yyyy""-""m""-""d h:mm AM/PM"
		elif type1=='percent':
			result="0.00%"
		elif type1=='bunsu':
			result="# ?/?"
		elif type1=='jisu':
			result="0.00E+00"
		elif type1=='text':
			result="@"
		elif type1=='etc':
			result="000-000"
		elif type1=='other':
			result="$#,##0.00_);[빨강]($#,##0.00)"

		sheet = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		my_range = sheet.Range(sheet.Cells(x1, y1), sheet.Cells(x2, y2))
		my_range.NumberFormat = result