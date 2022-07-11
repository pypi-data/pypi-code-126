# -*- coding: utf-8 -*-
import shutil
import zipfile
import win32com.client
import os
import re
import pickle
import time
import string
import inspect
import pyperclip
import pandas as pd
import glob
import paho.mqtt.client as mqtt
import pyautogui
import chardet

from PIL import ImageFont
from konlpy.tag import *
from os import listdir
from os.path import isfile, join
from screeninfo import get_monitors

from halmoney import pcell
from halmoney import basic_data

class youtil:

	def __init__(self):
		basic = basic_data.basic_data()
		self.common_data = basic.basic_data()
		self.manual = {}

	def append_df1_df2(self, df_obj_1, df_obj_2):
		"""
		dataframe의 끝에 dataframe로 만든 것을 맨끝에 추가하는것
		"""
		df_obj_1 = pd.concat([df_obj_1, df_obj_2])
		return df_obj_1

	def change_df_tolist(self, df_obj):
		"""
		df자료를 커럼과 값을 기준으로 나누어서 결과를 돌려주는 것이다
		"""
		result = []
		col_list = df_obj.columns.values.tolist()
		value_list = df_obj.values.tolist()
		return [col_list, value_list]

	def change_foldername(self, old_path, new_path):
		"""
		폴더이름 변경
		"""
		os.rename(old_path, new_path)

	def change_list_1d_2d(self, input_data):
		"""
		1차원의 리스트가 오면 2차원으로 만들어주는 것
		"""
		result = []
		if len(input_data) > 0:
			if type(input_data[0]) != type([]):
				for one in input_data:
					result.append([one, ])
		return result

	def change_list2d_list1d(self, input_data):
		"""
		항목 : ['항목1', '기본값1', '설명', {'입력형태1':'설명1', '입력형태2':'설명1',.... }]
		결과 ['항목1', '기본값1', '설명', '입력형태1:설명1', '입력형태2:설명1',.... }]
		위 형태의 자료를 한줄로 만들기위해 자료를 변경한다
		"""
		result = []
		for one_data in input_data:
			if type(one_data) == type({}):
				for key in list(one_data.Keys()):
					value = str(key)+" : "+str(one_data[key])
					result.append(value)
			elif type(one_data) == type(()) or type(one_data) == type([]) or type(one_data) == type(set()):
				for value in one_data:
					result.append(value)
			else:
				result.append(one_data)
		return result

	def change_list2d_samelen(self, input_data):
		"""
		길이가 다른 2dlist의 내부 값들을 길이가 같게 만들어주는 것이다
		가변적인 2차원배열을 최대크기로 모두 같이 만들어 준다
		"""
		result = []
		max_len = max(len(row) for row in input_data)
		for list_x in input_data:
			temp = list_x
			for no in range(len(list_x), max_len):
				temp.append("")
			result.append(temp)
		return result

	def chage_list1d_text_withword(self, input_list, chain_word =" ,"):
		"""
		리스트 자료들을 중간문자를 추가하여 하나의 문자열로 만드는 것,
		“aa, bbb, ccc” 이런 식으로 만드는 방법이다
		"""
		result = ""
		for one_word in input_list:
			result = result+ str(one_word) + str(chain_word)

		return result[:-len(chain_word)]

	def change_file_ecoding_type(self, path, file_name, original_type="EUC-KR", new_type="UTF-8", new_file_name=""):
		"""
		#텍스트가 안 읽혀져서 확인해보니 인코딩이 달라서 안되어져서
		#이것으로 전체를 변경하기위해 만듦
		"""
		full_path = path + "\\" + file_name
		full_path_changed = path + "\\" + new_file_name + file_name
		try:
			aaa = open(full_path, 'rb')
			result = chardet.detect(aaa.read())
			#print(result['encoding'], file_name)
			aaa.close()

			if result['encoding'] == original_type:
				#print("화일의 인코딩은 ======> {}, 화일이름은 {} 입니다".format(original_type, file_name))
				aaa = open(full_path, "r", encoding=original_type)
				file_read = aaa.readlines()
				aaa.close()

				new_file = open(full_path_changed, mode='w', encoding=new_type)
				for one in file_read:
					new_file.write(one)
				new_file.close()
		except:
			print("화일이 읽히지 않아요=====>", file_name)

		path = "C:\Python39-32\Lib\site-packages\myez_xl\myez_xl_test_codes"
		file_lists = os.listdir(path)
		for one_file in file_lists:
			self.change_file_ecoding_type(path, one_file, "EUC-KR", "UTF-8", "_changed")

	def change_value_cap (self, datas, argue=1):
		"""
		대소문자를 변경하는 것입니다
		이것은 단일 리스트만 가능하게 만들었다,  리스트안에 리스트가있는것은 불가능하다 (2004년 5월 2일 변경)
		기본은 대문자로 바꾸는 것이다
		"""
		results=[]
		for data in datas:
			#print (data)
			if argue == 0: result = str(data).lower() #모두 소문자로
			if argue == 1: result = str(data).upper() #모두 대문자로
			if argue == 2: result = str(data).capitalize() #첫글자만 대문자
			if argue == 3: result = str(data).swapcase() #대소문자 변경
			results.append(result)
		return results

	def change_value_lower (self, data):
		"""
		모든 리스트의 자료를 소문자로 만드는것이다
		"""
		for a in range(len(data)):
			data[a] =str(data[a]).lower()
		return data

	def split_list_bystep(self, input_list1d, step_no):
		"""
		12개의 리스트를
		입력 : [ [1,2,3,4,5,6,7,8,9,10,11,12], 4]를 받으면
			총 4개의 묶읆으로 순서를 섞어서 만들어 주는것
			[1,5,9,  2,6,10,  3,7,11,  4,8,12] 로 만들어 주는것
		"""
		total_no = len(input_list1d)
		repeat_no = step_no
		group_no = divmod(len(input_list1d), int(step_no))[0]
		namuji = total_no - repeat_no * group_no
		result = []
		#print(total_no, namuji)
		for y in range(step_no):
			for x in range(group_no + 1):
				new_no = x * step_no + y
				if new_no > total_no - 1:
					break
				else:
					#print(y, x, new_no)
					result.append(input_list1d[int(new_no)])
		return result

	def change_filename(self, old_path, new_path):
		"""
		화일이름 변경
		"""
		old_path = self.check_filepath(old_path)
		new_path = self.check_filepath(new_path)
		os.rename(old_path, new_path)

	def check_df_range(self, input_df):
		"""
		df의 영역을 나타내는 방법을 df에 맞도록 변경하는 것이다
		"""
		temp = []
		for one in input_df:
			if ":" in one:
				pass
			elif "~" in one:
				one = one.replace("~", ":")
			elif "all" in one:
				one = one.replace("all", ":")
			else:
				changed_one=one.split(",")
				temp_1 = []
				for item in changed_one:
					temp_1.append(int(item))
				one = temp_1
			temp.append(one)
		return temp

	def check_outlook_email_test_01(self, ):
		"""
		아웃룩익스프레스 테스트 하는것
		"""
		outlook = win32com.client.Dispatch("Outlook.Application")
		namespace = outlook.GetNamespace("MAPI")

		input_folder = namespace.GetDefaultFolder(6)
		#print("폴더이름 ==> ", input_folder.Name)

		for i in input_folder.items:
			print(i.subject)
			print(str(i.Sender) + "\t: " + i.SenderEmailAddress)

		print("전체 메일 개수 :" + str(input_folder.items.count))
		print("읽지않은 메일 개수 :" + str(input_folder.UnReadItemCount))
		print("읽은 메일 개수 :" + str(input_folder.items.count - input_folder.UnReadItemCount))

		print(namespace.Folders[0].Name)
		print(namespace.Folders[1].Name)
		print(namespace.Folders[2].Name)

		root_folder = namespace.Folders.Item(1)
		for folder in root_folder.Folders:
			print("폴더이름 ==> ", folder.Name)
			print("갯수 ==> ", folder.items.count)

		outlook = win32com.client.Dispatch("Outlook.Application")
		namespace = outlook.GetNamespace("MAPI")
		root_folder = namespace.Folders.Item(1)
		subfolder = root_folder.Folders['All'].Folders['Main Folder'].Folders['Subfolder']
		messages = subfolder.Items

	def check_filepath(self, file):
		"""
		입력자료가 폴더를 갖고있지 않으면 현재 폴더를 포함해서 돌려준다
		"""
		if len(file.split(".")) > 1:
			result = file
		else:
			cur_dir = self.system_read_current_path()
			result = cur_dir + "\\" + file
		return result

	def change_inputdata_list2d(self, input_data):
		"""
		입렫된 자료를 2차원으로 만드는 것
		입력자료는 리스트나 듀플이어야 한다
		"""
		if type(input_data[0]) == type([]) or type(input_data[0]) == type(()):
			#2차원의 자료이므로 입력값 그대로를 돌려준다
			result = input_data
		else:
			#1차원의 자료라는 뜻으로, 이것을 2차원으로 만들어 주는 것이다
			result = []
			for one in input_data:
				result.append([one])
		return result

	def click_mouse_button(self, click_type="click", input_clicks=1, input_interval=0.25):
		"""
		click_mouse_button
		"""
		if click_type == "click":
			pyautogui.click()
		elif click_type \
				== "doubleclick":
			pyautogui.doubleClick()
		else:
			pyautogui.click(button=click_type, clicks=input_clicks, interval=input_interval)

	def click_mouse(self, ):
		"""
		마우스 왼쪽 한번 클릭하기
		"""
		pyautogui.click()

	def compare_list_two_value(self, raw_data,req_number,project_name,vendor_name,nal):
		"""
		위아래 비교
		회사에서 사용하는 inq용 화일은 두줄로 구성이 된다
		한줄은 client가 요청한 스팩이며
		나머지 한줄은 vendor가 deviation사항으로 만든 스팩이다
		이두가지의 스팩을 하나로 만드는 것이다
		즉, 두줄에서 아래의 글씨가 있고 그것이 0, None가 아니면 위의것과 치환되는 것이다
		그런후 이위의 자료들만 따로 모아서 돌려주는 것이다
		"""
		self.data=list(raw_data)
		self.data_set=[]
		self.data_set_final=[]

		for self.a in range(0,len(self.data),2):
			for self.b in range(len(self.data[1])):
				if not(self.data[self.a+1][self.b]==self.data[self.a][self.b]) and self.data[self.a+1][self.b]!= None and self.data[self.a+1][self.b]!= 0:
					self.data_set.append(self.data[self.a+1][self.b])
				else:
					self.data_set.append(self.data[self.a][self.b])
			self.data_set.append(req_number)
			self.data_set.append(project_name)
			self.data_set.append(vendor_name)
			self.data_set.append(nal)
			self.data_set_final.append(self.data_set)
			self.data_set=[]
		return self.data_set_final

	def connect_mqtt(self, client, userdata, flags, rc):
		"""
		connect_mqtt
		"""
		if rc == 0:
			print("connected OK")
		else:
			print("Bad connection Returned code=", rc)

	def copy_folder(self, old_path, new_path):
		"""
		폴더복사
		"""
		shutil.copy(old_path, new_path)

	def copy_file(self, old_path, new_path, meta=""):
		"""
		화일복사
		"""
		old_path = self.check_filepath(old_path)
		new_path = self.check_filepath(new_path)
		if meta == "":
			shutil.copy(old_path, new_path)
		else:
			shutil.copy2(old_path, new_path)

	def copy_clipboard(self, input_text):
		"""
		클립보드에 입력된 내용을 복사를 하는 것이다
		"""
		self.manual["clipboard_copy"] = {
			"분류1" : "복사",
			"설명":"클립보드에 텍스트를 복사",
			"입력요소" : "input_text(텍스트)",
			"기타설명":""
		}
		pyperclip.copy(input_text)

	def delete_specialletter(self, input_text):
		"""
		특수문자를 제거하는것
		"""
		for one in input_text:
			if str(one) in ' 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_':
				temp = temp + str(one)
		result = temp
		return result

	def delete_list1d_data_bystep(self, input_list, step, start=0):
		"""
		원하는 순서째의 자료를 ""으로 만드는것
		"""
		flag_no = 0
		for num in range(start, len(input_list)):
			flag_no = flag_no + 1
			if flag_no == step:
				input_list[num] = ""
				flag_no = 0
		return input_list

	def doubleclick_mouse(self, ):
		"""
		마우스 왼쪽 더블 클릭하기
		"""
		pyautogui.doubleClick()

	def delete_df_emptycolumn(self, df_obj):
		"""
		dataframe의 빈열을 삭제
		제목이 있는 경우에만 해야 문제가 없을것이다
		"""
		nan_value = float("NaN")
		df_obj.replace(0, nan_value, inplace=True)
		df_obj.replace("", nan_value, inplace=True)
		df_obj.dropna(how="all", axis=1, inplace=True)
		return df_obj

	def delete_file(self, old_path):
		"""
		화일삭제
		"""
		old_path = self.check_filepath(old_path)
		os.remove(old_path)

	def draw_triangle(self, xyxy, per=100, reverse=1, size=100):
		"""
		직각삼각형
		정삼각형에서 오른쪽이나 왼쪽으로 얼마나 더 간것인지
		100이나 -100이면 직삼각형이다
		사각형은 왼쪽위에서 오른쪽 아래로 만들어 진다
		"""
		x1, y1, x2, y2 = xyxy
		width = x2 - x1
		height = y2 - y1
		lt = [x1, y1]  # left top
		lb = [x2, y1]  # left bottom
		rt = [x1, y2]  # right top
		rb = [x2, y2]  # right bottom
		tm = [x1, int(y1 + width / 2)]  # 윗쪽의 중간
		lm = [int(x1 + height / 2), y1]  # 윗쪽의 중간
		rm = [int(x1 + height / 2), y1]  # 윗쪽의 중간
		bm = [x2, int(y1 + width / 2)]  # 윗쪽의 중간
		center = [int(x1 + width / 2), int(y1 + height / 2)]

		result = [lb, rb, rt]
		return result

	def delete_folder(self, old_dir, empty="no"):
		"""
		폴더삭제
		폴더안에 자료가 있어도 삭제
		"""
		if empty =="no":
			shutil.rmtree(old_dir)
		else:
			os.rmdir(old_dir)

	def file_delete_emptyline_over2(self, file_name):
		"""
		화일을 읽어 내려가다가 2줄이상의 띄어쓰기가 된것을 하나만 남기는것
		텍스트로 저장된것을 사용하다가 필요해서 만듦
		"""
		f = open(file_name, 'r', encoding='UTF8')
		lines = f.readlines()
		num = 0
		result = ""
		for one_line in lines:
			if one_line =="\n":
				num=num+1
				if num == 1:
					result = result + str(one_line)
				elif num > 1:
					#print("2줄발견")
					pass
			else:
				num = 0
				result = result + str(one_line)
		return result

	def get_diagonal_xy(self, xyxy=[5, 9, 12, 21]):
		"""
		좌표와 대각선의 방향을 입력받으면, 대각선에 해당하는 셀을 돌려주는것
		좌표를 낮은것 부터 정렬하기이한것 [3, 4, 1, 2] => [1, 2, 3, 4]
		"""
		result = []
		if xyxy[0] > xyxy[2]:
			x1, y1, x2, y2 = xyxy[2], xyxy[3], xyxy[0], xyxy[1]
		else:
			x1, y1, x2, y2 = xyxy

		x_height = abs(x2 - x1) + 1
		y_width = abs(y2 - y1) + 1
		step = x_height / y_width
		temp = 0

		if x1 <= x2 and y1 <= y2:
			# \형태의 대각선
			for y in range(1, y_width + 1):
				x = y * step
				if int(x) >= 1:
					final_x = int(x) + x1 - 1
					final_y = int(y) + y1 - 1
					if temp != final_x:
						result.append([final_x, final_y])
						temp = final_x
		else:
			for y in range(y_width, 0, -1):
				x = x_height - y * step

				final_x = int(x) + x1
				final_y = int(y) + y1 - y_width
				temp_no = int(x)

				if temp != final_x:
					temp = final_x
					result.append([final_x, final_y])
		return result

	def get_list2d_maxsize(self, list_2d_data):
		"""
		2차원 배열의 제일 큰 갯수를 확인한다
		#an_array = [[1, 2], [3, 4, 5]]
		#print("2차배열 요소의 최대 갯수는 ==>", check_list_maxsize(an_array))
		"""
		max_length = max(len(row) for row in list_2d_data)
		return max_length

	def insert_1000comma(self, input_num):
		"""
		입력된 숫자를 1000단위로 콤마를 넣는것
		"""
		temp = str(input_num).split(".")
		total_len = len(temp[0])
		result = ""
		for num in range(total_len):
			one_num = temp[0][- num - 1]
			if num % 3 == 2:
				result = "," + one_num + result
			else:
				result = one_num + result
		if len(temp) > 1:
			result = result + "." + str(temp[1])
		return result

	def insert_value_list_bystep(self, input_list, insert_value, step):
		"""
		기존자료에 n번째마다 자료를 추가하는 기능
		raw_data = ['qweqw','qweqweqw','rterert','gdgdfgd',23,534534,'박상진']
		added_data = "new_data"
		step=3, 각 3번째 마다 자료를 추가한다면
		"""
		var_1, var_2 = divmod(len(input_list), int(step))
		for num in range(var_1, 0, -1):
			input_list.insert(num * int(step) - var_2 + 1, insert_value)
		return input_list

	def insert_df_new(self, df_obj_1, df_obj_2):
		"""
		df_obj_1의 자료에 df_obj_2를 맨끝에 추가하는것
		"""
		df_obj_1 = pd.concat([df_obj_1, df_obj_2])
		return df_obj_1

	def keyboard_type_letter(self, input_text, input_interval=""):
		"""
		암호나 글자를 입력하는 데 사용하는것이다
		이것은 대부분 마우스를 원하는 위치에 옮기고, 클릭을 한번한후에 사용하는것이 대부분이다
		그저 글자를 타이핑 치는 것이다
		"""
		time.sleep(1)
		pyperclip.copy(input_text)
		pyautogui.hotkey("ctrl", "v")

	def keyboard_type_keypad(self, action='enter', times=1, input_interval=0.1):
		"""
		pyautogui.press('enter', presses=3, interval=3) # enter 키를 3초에 한번씩 세번 입력합니다.
		"""
		pyautogui.press(action, presses=times, interval=input_interval)

	def keyboard_type_hotkey(self, input_keys=['ctrl', 'c']):
		"""
		pyautogui.hotkey('ctrl', 'c')  # ctrl-c to copy
		"""
		text = ""
		for one in input_keys:
			text = text + "'" + str(one) + "',"
		pyautogui.hotkey(text[:-1])

	def keyboard_type_action(self, action, key):
		"""
		pyautogui.keyDown('ctrl')  # ctrl 키를 누른 상태를 유지합니다.
		pyautogui.press('c')  # c key를 입력합니다.
		pyautogui.keyUp('ctrl')  # ctrl 키를 뗍니다.
		"""
		if action == "keydown":
			pyautogui.keyDown(key)
		if action == "keyup":
			pyautogui.keyUp(key)
		if action == "press":
			pyautogui.press(key)

	def move_mouse_xy_fromcurrent(self, x1, y1):
		"""
		move_mouse_xy
		현재있는 위치를 기준으로 이동
		"""
		pyautogui.move(x1, y1)
		print(x1, y1)

	def move_mouse_xy(self, x1, y1):
		"""
		move_mouse_xy
		현재있는 위치를 기준으로 이동
		"""
		pyautogui.moveTo(x1, y1)
		print(x1, y1)


	def make_zip_file(self, zip_name_path, new_path_all):
		"""
		화일들을 zip으로 압축하는것
		"""
		with zipfile.ZipFile(zip_name_path, 'w', compression=zipfile.ZIP_DEFLATED) as new_zip:
			for one in new_path_all:
				new_zip.write(one)
		new_zip.close()

	def move_file(self, old_file, new_file):
		"""
		화일을 이동시키는것
		"""
		old_file = self.check_filepath(old_file)
		shutil.move(old_file, new_file)

	def move_folder(self, old_dir, new_dir):
		"""
		폴더를 이동시키는것
		"""
		shutil.move(old_dir, new_dir)

	def make_folder(self, old_dir):
		"""
		폴더 만들기
		"""
		os.mkdir(old_dir)

	def paste_clipboard(self,):
		"""
		클립보드에 복사된 내용을 현재 활성화된 프로그램에 붙여넣기를 하는 것이다
		"""
		self.manual["clipboard_paste"] = {
			"분류1" : "복사",
			"설명":"클립보드에 저장된 텍스트를 붙여넣습니다",
			"입력요소" : "",
			"기타설명":"이것은 ctrl+v를 이용해도 같다"
		}

		result = pyperclip.paste()
		return result

	def ppt_make_ppt_table_from_xl_data(self, ):
		"""
		엑셀의 테이블 자료가 잘 복사가 않되는것 같아서, 아예 하나를 만들어 보았다
		엑셀의 선택한 영역의 테이블 자료를 자동으로 파워포인트의 테이블 형식으로 만드는 것이다
		"""
		excel = pcell.pcell("")
		activesheet_name = excel.read_activesheet_name()
		[x1, y1, x2, y2] = excel.read_select_address()
		print([x1, y1, x2, y2])

		Application = win32com.client.Dispatch("Powerpoint.Application")
		Application.Visible = True
		active_ppt = Application.Activepresentation
		slide_no = active_ppt.Slides.Count + 1

		new_slide = active_ppt.Slides.Add(slide_no, 12)
		new_table = active_ppt.Slides(slide_no).Shapes.AddTable(x2 - x1 + 1, y2 - y1 + 1)
		shape_no = active_ppt.Slides(slide_no).Shapes.Count

		for y in range(y1, y2 + 1):
			for x in range(x1, x2 + 1):
				value = excel.read_cell_value(activesheet_name, [x, y])
				active_ppt.Slides(slide_no).Shapes(shape_no).Table.Cell(x - x1 + 1,
				                                                        y - y1 + 1).Shape.TextFrame.TextRange.Text = value

	def save_file_by_pickle(self, input_data="", path_n_name=""):
		"""
		피클로 객체를 저장하는것
		"""
		if ":" in path_n_name:
			full_file_name = path_n_name
		else:
			full_file_name = "./"+path_n_name
		with open(str(full_file_name)+".pickle", "wb") as fr:
			pickle.dump(input_data, fr)

	def read_df_byno(self, df_obj, x, y):
		"""
		숫자번호로 pandas의 dataframe의 일부를 불러오는 것
		단, 모든것을 문자로 넣어주어야 한다
		x=["1:2", "1~2"] ===> 1, 2열
		x=["1,2,3,4"] ===> 1,2,3,4열
		x=[1,2,3,4]  ===> 1,2,3,4열
		x=""또는 "all" ===> 전부
		"""

		x_list = self.check_df_range(x)
		y_list = self.check_df_range(y)
		exec("self.result = df_obj.iloc[{}, {}]".format(x_list, y_list))
		return self.result

	def read_df_byname(self, df_obj, x, y):
		"""
		열이나 행의 이름으로 pandas의 dataframe의 일부를 불러오는 것이다
		이것은 리스트를 기본으로 사용한다
		list_x=["가"~"다"] ===> "가"~"다"열
		list_x=["가","나","다","4"] ===> 가,나,다, 4 열
		x=""또는 "all" ===> 전부
		"""

		temp = []
		for one in [x,y]:
			if ":" in one[0]:
				changed_one = one[0]
			elif "~" in one[0]:
				ed_one = one[0].split("~")
				changed_one = "'"+str(ed_one[0])+"'"+":"+"'"+str(ed_one[1])+"'"

			elif "all" in one[0]:
				changed_one = one[0].replace("all", ":")
			else:
				changed_one=one
			temp.append(changed_one)
		#이것중에 self를 사용하지 않으면 오류가 발생한다
		print(temp)
		exec("self.result = df_obj.loc[{}, {}]".format(temp[0], temp[1]))
		return self.result

	def read_df_byxy(self, df_obj, xy=[0,0]):
		"""
		위치를 기준으로 값을 읽어오는 것이다
		숫자를 넣으면 된다
		"""
		result = df_obj.iat[int(xy[0]), int(xy[1])]
		return result

	def read_monitorsss_properties(self):
		#연결된 모니터들의 속성을 알려준다
		result = {}
		sub_result = {}
		num = 0
		for m in get_monitors():
			num = num + 1
			#print(m)
			sub_result["x"] = m.x
			sub_result["y"] = m.y
			sub_result["height_mm"] = m.height_mm
			sub_result["width_mm"] = m.width_mm
			sub_result["height"] = m.height
			sub_result["width"] = m.width
			sub_result["primary"] = m.is_primary
			sub_result["name"] = m.name
			name = "monitor" + str(num)
			result[name] = sub_result
		return result

	def read_filename_in_folder(self, directory):
		"""
		폴더이름은 제외한다
		"""
		result = [f for f in listdir(directory) if isfile(join(directory, f))]

		return result

	def read_filename_in_folder_all(self, directory):
		"""
		#tree에서 폴더를 클릭하면 안의 화일을 익어오는것
		"""
		result = []
		file_list = os.listdir(directory)
		#print("file_list: {}".format(directory))

		file_list = glob.glob(directory)
		file_list_py = [file for file in file_list if file.endswith("")]

		filenames = os.listdir(directory)
		for filename in filenames:
			full_filename = os.path.join(directory, filename)
			#print("화일 명====>", full_filename)
			result.append(filename)
		return result

	def read_mouse_xy(self, ):
		"""
		현재의 마우스의 위치 읽어오기
		"""
		xy = pyautogui.position()
		return (xy.x, xy.y)

	def read_object_methodname_help(self, obgect):
		"""
		read_object_methodname_help
		"""
		result = {}
		for one in dir(obgect):
			temp = []
			if not one.startswith('__'):
				try:
					temp.append(one)
					#print(one)
					temp.append(getattr(obgect, one).__doc__)
					#print(getattr(obgect, one).__doc__)
				except:
					pass
			result[one] = temp
		return result

	def get_object_methodname_all(self, object):
		"""
		원하는 객체를 넣으면, 객체의 함수와 각 함수의 인자를 사전형식으로 돌려준다
		"""
		result = self.read_object_method_argument_from_object(object)
		return result


	def read_object_method_argument_from_object(self, object):
		"""
		원하는 객체를 넣으면, 객체의 함수와 각 함수의 인자를 사전형식으로 돌려준다
		"""
		result ={}
		for obj_method in dir(object):
			try:
				method_data = inspect.signature(getattr(object, obj_method))
				dic_fun_var = {}
				if not obj_method.startswith("_"):
					for one in method_data.parameters:
						value_default = method_data.parameters[one].default
						value_data = str(method_data.parameters[one])

						if value_default  == inspect._empty:
							dic_fun_var[value_data] = None
						else:
							value_key, value_value = value_data.split("=")
							if value_value == "''" or value_value == '""':
								value_value = ''
							value_value = str(value_value).replace("'", "")
							#print(value_data, "키값==>", value_key, "입력값==>", value_value)
							dic_fun_var[str(value_key)] = value_value
						result[obj_method] = dic_fun_var
			except:
				pass
		#print(result)
		return result

	def read_pickle_file(self, path_n_name=""):
		"""
		pickle로 자료를 만든것을 읽어오는 것이다
		"""
		with open(path_n_name, "rb") as fr:
			result = pickle.load(fr)
		return result

	def read_pickle_filename_infolder(self, directory="./", filter = "pickle"):
		"""
		pickle로 만든 자료를 저장하는것
		"""
		result = []
		all_files = os.listdir(directory)
		if filter == "*" or filter == "":
			filter = ""
			result = all_files
		else:
			filter = "." + filter
			for x in all_files:
				if x.endswith(filter):
					result.append(x)
		return result

	def receive_mqtt_data(self, topic='halmoney/data001'):
		"""
		mqtt의 서버에서 자료받기
		"""
		self.topic = topic
		client = mqtt.Client()
		client.on_connect = self.on_connect
		client.on_disconnect = self.on_disconnect
		client.on_subscribe = self.on_subscribe
		client.on_message = self.on_message

		client.connect(self.broker, self.port, 60)
		client.subscribe(self.topic, 1)
		client.loop_forever()

	def replace_word(self, input_text, before_text, after_text):
		"""
		폰트와 글자를 주면, 필셀의 크기를 돌려준다
		"""
		result = input_text.replace(before_text, after_text)
		return result

	def split_file_bydef(self, file_name, base_text = "def"):
		"""
		화일안의 def를 기준으로 문서를 분리하는것
		같은 함수의 코드를 찾기위해 def로 나누는것
		맨앞의 시작글자에 따라서 나눌수도 있다
		"""
		temp_list = []
		result = []
		# 화일을 읽어온다
		f = open(file_name, 'r', encoding='UTF8')
		lines = f.readlines()
		original = lines
		#빈 줄을 제거한다
		lines = list(map(lambda s: s.strip(), lines))
		start_no = 0
		for no in range(len(lines)):
			line = lines[no]

			#각줄의 공백을 제거한다
			one_line = line.strip()
			#혹시 잇을수있는 줄바꿈을 제거한다
			one_line = one_line.replace("\n", "")
			#맨앞에서 def가 발견이되면 여태저장한것을 최종result리스트에 저장 하고 새로이 시작한다
			if one_line[0:(len(base_text)+1)] == base_text and temp_list != []:
				print("처음은 ===> ", start_no)
				print("끝은 ===> ", no)
				result.append(temp_list, start_no, no)
				start_no = no
				temp_list = []
			#빈행이나 주석으로된 열을 제외한다
			if one_line != "" and one_line[0] != "#":
				temp_list.append(one_line)
		f.close()
		return result

	def sort_list_byindex (self, input_list, index_no=0):
		"""
		입력 :  리스트자료
		리스트자료를 몇번째 순서를 기준으로 정렬하는것
		aa = [[111, 'abc'], [222, 222],['333', 333], ['777', 'sjpark'], ['aaa', 123],['zzz', 'sang'], ['jjj', 987], ['ppp', 'park']]
		value=sort_list(리스트자료, 정렬기준번호)
		"""
		result_before = [(i[index_no], i) for i in input_list]
		result_before.sort()
		result = [i[1] for i in result_before]
		return result

	def sort_list2d_1(self, input_list, sort_index=1):
		"""
		input_list의 기준에 따라서, 2차원의 자료를 기준으로 정렬하는것이다
		index는 2차원을 정리하는 기준을 정하는 것이다
		"""
		input_list.sort(key=lambda x: x[sort_index])
		return input_list

	def sort_list2d(self, input_set, sort_index=[0]):
		"""
		집합자료를 정렬하는것
		사용법 : [자료, [1,-2,3]]
		자료를 1,2,3순으로 정렬을 하는데, 2번째는 역순으로 정렬
		"""
		temp=""
		for one in sort_index:
			# 역순으로 정렬할게 있는지 확인하는것
			if "-" in str(one):
				temp = temp + ("-x[%s], " %(str(abs(one))))
			else:
				temp = temp + ("x[%s], " %(str(one)))
		# lamda형식으로 만들어서 sorted의 key로 사용
		str_lambda = ("lambda x :(%s)" %temp[:-2])
		#print(str_lambda)
		result = sorted(input_set, key = eval(str_lambda))
		return result

	def select_list1d_unique_y(self, data1, data2):
		"""
		고유한 컬럼만 골라낸다
		"""
		result = []
		columns = self.read_y_names(data1)
		update_data2 = self.change_waste_data(data2)
		for temp_3 in update_data2:
			if not temp_3.lower() in columns:
				result.append(temp_3)
		return result

	def select_list_unique_value(self, input_datas, status=0):
		"""
		중복된 리스트의 자료를 없애는 것이다. 같은것중에서 하나만 남기고 나머지는 []으로 고친다
		"""
		if status == 0:
			result = []
			# 계속해서 pop으로 하나씩 없애므로 하나도 없으면 그만 실행한다
			while len(input_datas) != 0:
				gijun = input_datas.pop()
				sjpark = 0
				result.append(gijun)
				for number in range(len(input_datas)):
					if input_datas[int(number)] == []:  # 빈자료일때는 그냥 통과한다
						pass
					if input_datas[int(number)] == gijun:  # 자료가 같은것이 있으면 []으로 변경한다
						sjpark = sjpark + 1
						input_datas[int(number)] = []
		else:
			# 중복된것중에서 아무것도없는 []마저 없애는 것이다. 위의 only_one을 이용하여 사용한다
			# 같은것중에서 하나만 남기고 나머지는 []으로 고친다
			# 이것은 연속된 자료만 기준으로 삭제를 하는 것입니다
			# 만약 연속이 되지않은 같은자료는 삭제가 되지를 않읍니다
			result = list(self.select_list_unique_value(input_datas))
			for a in range(len(result) - 1, 0, -1):
				if result[a] == []:
					del result[int(a)]
		return result

	def system_change_encodeing_type_001_success(self, ):
		"""
		기본적인 시스템에서의 인코딩을 읽어온다
		"""
		system_in_basic_incoding = sys.stdin.encoding
		system_out_basic_incoding = sys.stdout.encoding
		print("시스템의 기본적인 입력시의 인코딩 ====> ", system_in_basic_incoding)
		print("시스템의 기본적인 출력시의 인코딩 ====> ", system_out_basic_incoding)

	def system_read_current_path(self, path=""):
		"""
		현재의 경로를 돌려주는것
		"""
		result = os.getcwd()
		return result

	def split_value_bystep(self, input_text, number):
		"""
		문자열을 몇개씩 숫자만큼 분리하기
		['123456'] => ['12','34','56']
		"""
		result = []
		for i in range(0, len(input_text), number):
			result.append("".join(input_text[i:i + number]))
		return result

	def split_num_char(self, raw_data):
		"""
		문자와숫자를 분리해서 리스트로 돌려주는 것이다
		123wer -> ['123','wer']
		"""
		temp=""
		int_temp=""
		result = []
		datas=str(raw_data)
		for num in range(len(datas)):
			if num==0:
				temp=str(datas[num])
			else:
				try:
					fore_var=int(datas[num])
					fore_var_status="integer"
				except:
					fore_var=datas[num]
					fore_var_status="string"
				try:
					back_var=int(datas[num-1])
					back_var_status="integer"
				except:
					back_var=datas[num-1]
					back_var_status="string"

				if fore_var_status==back_var_status:
					temp=temp+datas[num]
				else:
					result.append(temp)
					temp=datas[num]
		if len(temp)>0:
			result.append(temp)
		return result

	def start_mqtt(self, broker= "broker.hivemq.com", port=1883, qos = 0):
		"""
		start_mqtt
		"""
		self.broker = broker
		self.port = port
		self.qos = qos

	def send_mqtt_data(self, input_text="no message", topic='halmoney/data001'):
		"""
		send_mqtt_data
		"""
		self.topic = topic
		client = mqtt.Client()
		# 새로운 클라이언트 생성

		# 콜백 함수 설정 on_connect(브로커에 접속), on_disconnect(브로커에 접속중료), on_publish(메세지 발행)
		client.on_connect = self.on_connect
		client.on_disconnect = self.on_disconnect
		client.on_publish = self.on_publish
		client.connect(self.broker, self.port)
		client.loop_start()

		client.publish(self.topic, str(input_text), self.qos)
		client.loop_stop()
		client.disconnect()

	def split_value_num(self, input_text):
		"""
		단어중에 나와있는 숫자만 분리하는기능
		"""
		re_compile = re.compile(r"([0-9]+)")
		result = re_compile.findall(input_text)
		new_result = []
		for dim1_data in result:
			for dim2_data in dim1_data:
				new_result.append(dim2_data)
		return new_result

	def split_value_eng(self, input_text):
		"""
		단어중에 나와있는 영어만 분리하는기능
		"""
		re_compile = re.compile(r"([a-zA-Z]+)")
		result = re_compile.findall(input_text)
		new_result = []
		for dim1_data in result:
			for dim2_data in dim1_data:
				new_result.append(dim2_data)
		return new_result

	def sort_list_data(self, input_data):
		"""
		aa = [[111, 'abc'], [222, 222],['333', 333], ['777', 'sjpark'], ['aaa', 123],['zzz', 'sang'], ['jjj', 987], ['ppp', 'park']]
		정렬하는 방법입니다
		"""
		result = []
		for one_data in input_data:
			for one in one_data:
				result.append(one.sort())
		return result

	def split_korean_jamo(self, one_text):
		"""
		한글자의 한글을 자음과 모음으로 구분해 주는것
		"""

		first_letter = ["ㄱ", "ㄲ", "ㄴ", "ㄷ", "ㄸ", "ㄹ", "ㅁ", "ㅂ", "ㅃ", "ㅅ", "ㅆ", "ㅇ", "ㅈ", "ㅉ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ"]
		# 19 글자
		second_letter = ["ㅏ", "ㅐ", "ㅑ", "ㅒ", "ㅓ", "ㅔ", "ㅕ", "ㅖ", "ㅗ", "ㅘ", "ㅙ", "ㅚ", "ㅛ", "ㅜ", "ㅝ", "ㅞ", "ㅟ", "ㅠ", "ㅡ", "ㅢ", "ㅣ"]  # 21 글자
		third_letter = ["", "ㄱ", "ㄲ", "ㄳ", "ㄴ", "ㄵ", "ㄶ", "ㄷ", "ㄹ", "ㄺ", "ㄻ", "ㄼ", "ㄽ", "ㄾ", "ㄿ", "ㅀ", "ㅁ", "ㅂ", "ㅄ", "ㅅ", "ㅆ", "ㅇ", "ㅈ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ"]  # 28 글자, 없는것 포함
		one_byte_data = one_text.encode("utf-8")

		new_no_1 = (int(one_byte_data[0])-234)*64*64
		new_no_2 = (int(one_byte_data[1])-128)*64
		new_no_3 = (int(one_byte_data[2])-128)

		value = new_no_1 + new_no_2 + new_no_3 -3072

		temp_num_1 = divmod(value, 588) #초성이 몇번째 자리인지를 알아내는것
		temp_num_2 = divmod(divmod(value, 588)[1], 28) #중성과 종성의 자릿수를 알아내는것것

		chosung = first_letter[divmod(value, 588)[0]] #초성
		joongsung = second_letter[divmod(divmod(value, 588)[1], 28)[0]] #중성
		jongsung = third_letter[divmod(divmod(value, 588)[1], 28)[1]] #종성

		return [chosung, joongsung, jongsung ]

	def split_korean_part(self, input_text):
		"""
		문장을 갖고와서 단어별로 품사를 나누는 것이다
		"""
		komoran = Komoran(userdic="C:\\Python38-32/sjpark_dic.txt")

		input_text = input_text.replace("\n", ", ")
		input_text = input_text.replace(" ", ", ")
		input_text = input_text.strip()

		result = komoran.pos(input_text)
		return result

	def trans_list2d_xy_yx (self, input_list):
		"""
		리스트값의 x,y를 바꾸는것
		"""
		result = zip(*input_list)
		return result

	def value_calc_pixel_size(self, input_text, font_size, font_name):
		"""
		폰트와 글자를 주면, 필셀의 크기를 돌려준다
		"""
		font = ImageFont.truetype(font_name, font_size)
		size = font.getsize(input_text)
		return size

	def value_cal_text_pixel(self, input_text, target_pixel, font_name="malgun.ttf", font_size=12, fill_char=" "):
		"""
		원하는 길이만큼 텍스트를 근처의 픽셀값으로 만드는것
		원래자료에 붙이는 문자의 픽셀값
		"""
		fill_px = self.value_calc_pixel_size(fill_char, font_size, font_name)[0]
		total_length =0
		for one_text in input_text:
			#한글자씩 필셀값을 계산해서 다 더한다
			one_length = self.value_calc_pixel_size(fill_char, font_size, font_name)[0]
			total_length = total_length + one_length

		# 원하는 길이만큼 부족한 것을 몇번 넣을지 게산하는것
		times = round((target_pixel - total_length)/fill_px)
		result = input_text + " "*times

		#최종적으로 넣은 텍스트의 길이를 한번더 구하는것
		length = self.value_calc_pixel_size(result, font_size, font_name)[0]

		#[최종변경문자, 총 길이, 몇번을 넣은건지]
		return [result, length, times]

	def value_split_성공한것_한글_품사로_나누기(self, input_text):
		"""
		문장을 갖고와서 단어별로 품사를 나누는 것이다
		"""
		komoran = Komoran(userdic="C:\\Python38-32/sjpark_dic.txt")

		input_text = input_text.replace("\n", ", ")
		input_text = input_text.replace(" ", ", ")
		input_text = input_text.strip()

		split_value = komoran.pos(input_text)
		print(split_value)

		#Save pickle
		with open("data.pickle", "wb") as fw:
			pickle.dump(split_value, fw)





	#==========================변경불가한 특별한 함수이름들
	def on_subscribe(self, client, userdata, mid, granted_qos):
		"""
		on_subscribe
		"""
		print("subscribed: " + str(mid) + " " + str(granted_qos))

	def on_disconnect(self, client, userdata, flags, rc=0):
		"""
		on_disconnect
		"""
		print(str(rc))

	def on_publish(self, client, userdata, mid):
		"""
		on_publish
		"""
		print("In on_pub callback mid= ", mid)

	def on_connect(self, client, userdata, flags, rc):
		"""
		on_connect
		"""
		if rc == 0:
			print("connected OK")
		else:
			print("Bad connection Returned code=", rc)

	def on_message(self, client, userdata, msg):
		"""
		on_message
		"""
		print(str(msg.payload.decode("utf-8")))