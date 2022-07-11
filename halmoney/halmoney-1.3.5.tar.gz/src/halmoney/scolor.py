# -*- coding: utf-8 -*-
import re
from halmoney import basic_data

"""
이것은 모든 외부로 들어오고 나가는 것은 전부 RGB형태로 이루어지도록 만든다
색을 변경하고 관리하는 모듈이며
색의 변화를 잘 사용이 가능하도록 하기위한 것이다

# 기본 입력 예 : "빨강", "빨강55", "red55", "0155"
# 기본색 ==> 12색 + (하양, 검정, 회색),
# 큰변화 ==> 1~9단계, 작은변화 ==> 1~9단계
# 기본함수 : get_color_rgb("red55"),  get_rgb_3input(색, 큰변화, 작은변화)
# 모든색의 표현이나 결과는 rgb로 돌려준다
"""

class scolor:

	def __init__(self):
		basic = basic_data.basic_data()
		self.common_data = basic.basic_data()
		self.tone = {}


	def change_rgb_12hsl(self, rgb):
		"""
		rgb색을 요하네스 이텐의 12가지 색으로 12가지 색으로 바꾸는것
		"""
		result = []
		h, s, l = self.change_rgb_hsl(rgb)
		style_list = self.common_data["list_colorstyle_eng"]
		for list_value in style_list:
			result.append([h, list_value[0], list_value[1]])
		return result

	def change_hsl_rgb(self, hsl_list):
		"""
		hsl을 rgb로 바꾸는 것이다
		"""
		h, s, l = hsl_list
		h = float(h / 360)
		s = float(s / 100)
		l = float(l / 100)

		if s == 0:
			R = l * 255
			G = l * 255
			B = l * 255

		if l < 0.5:
			temp1 = l * (1 + s)
		else:
			temp1 = l + s - l * s

		temp2 = 2 * l - temp1

		#h = h / 360

		tempR = h + 0.333
		tempG = h
		tempB = h - 0.333

		if tempR < 0: tempR = tempR + 1
		if tempR > 1: tempR = tempR - 1
		if tempG < 0: tempG = tempG + 1
		if tempG > 1: tempG = tempG - 1
		if tempB < 0: tempB = tempB + 1
		if tempB > 1: tempB = tempB - 1

		if 6 * tempR < 1:
			R = temp2 + (temp1 - temp2) * 6 * tempR
		else:
			if 2 * tempR < 1:
				R = temp1
			else:
				if 3 * tempR < 2:
					R = temp2 + (temp1 - temp2) * (0.666 - tempR) * 6
				else:
					R = temp2

		if 6 * tempG < 1:
			G = temp2 + (temp1 - temp2) * 6 * tempG
		else:
			if 2 * tempG < 1:
				G = temp1
			else:
				if 3 * tempG < 2:
					G = temp2 + (temp1 - temp2) * (0.666 - tempG) * 6
				else:
					G = temp2
		if 6 * tempB < 1:
			B = temp2 + (temp1 - temp2) * 6 * tempB
		else:
			if 2 * tempB < 1:
				B = temp1
			else:
				if 3 * tempB < 2:
					B = temp2 + (temp1 - temp2) * (0.666 - tempB) * 6
				else:
					B = temp2
		R = int(abs(round(R * 255,0)))
		G = int(abs(round(G * 255,0)))
		B = int(abs(round(B * 255,0)))

		rgb_to_int = (int(B)) * (256 ** 2) + (int(G)) * 256 + int(R)
		return [R, G, B]

	def change_hsl_com(self, hsl):
		"""
		mode : 1
		보색 : Complementary
		"""
		h, s, l = hsl

		new_h_1 = h + 180
		if new_h_1 >= 360:
			new_h_1 = 360 - new_h_1

		result_rgb = self.change_hsl_rgb([new_h_1, s, l])
		return result_rgb

	def change_hsl_2nearcom(self, hsl, h_step=36):
		"""
		mode : 14
		근접보색조합 : 보색의 근처색
		분열보색조합 : Split Complementary
		근접보색조합이라고도 한다. 보색의 강한 인상이 부담스러울때 보색의 근처에 있는 색을 사용
		"""
		h, s, l = hsl

		new_h_1 = divmod(h - h_step + 180, 360)[1]
		new_h_3 = divmod(h + h_step + 180, 360)[1]

		hsl_1 = [new_h_1, s, l]
		hsl_3 = [new_h_3, s, l]
		result_rgb = self.change_hsl_rgb_multi([hsl_1, hsl, hsl_3])
		return result_rgb

	def change_hsl_bo_3tri(self, hsl):
		"""
		mode :
		등간격 3색조합 : triad
		활동적인 인상과 이미지를 보인다
		"""
		h, s, l = hsl

		new_h_1 = divmod(h + 120, 360)[1]
		new_h_3 = divmod(h + 240, 360)[1]

		hsl_1 = [new_h_1, s, l]
		hsl_3 = [new_h_3, s, l]

		result_rgb = self.change_hsl_rgb_multi([hsl_1, hsl, hsl_3])
		return result_rgb

	def change_rgb_hex(self, rgb):
		"""
		엑셀의 Cells(1, i).Interior.Color는 hex값을 사용한다
		"""
		r, g, b = rgb[2], rgb[1], rgb[0]
		#result = "#{:02x}{:02x}{:02x}".format(int(rgb[0]), int(rgb[1]), int(rgb[2]))
		result = f"#{int(round(r)):02x}{int(round(g)):02x}{int(round(b)):02x}"
		return result

	def change_rgb_int(self, rgb_list):
		"""
		rgb인 값을 color에서 인식이 가능한 값으로 변경하는 것이다
		엑셀에서는 rgb랑 이 정수를 사용하여 색을 지정한다
		"""
		result = (int(rgb_list[2])) * (256 ** 2) + (int(rgb_list[1])) * 256 + int(rgb_list[0])
		return result

	def change_rgb_hsl (self, rgb_list):
		"""
		rgb를 hsl로 바꾸는 것이다
		입력은 0~255사이의 값
		"""
		r,g,b = rgb_list
		r = float(r / 255)
		g = float(g / 255)
		b = float(b / 255)
		max1 = max(r, g, b)
		min1 = min(r, g, b)
		l = (max1 + min1) / 2

		if max1 == min1:
			s = 0
		elif l < 0.5:
			s = (max1 - min1) / (max1 + min1)
		else:
			s = (max1 - min1) / (2 - max1 - min1)

		if s ==0:
			h = 0
		elif r >= max(g, b):
			h = (g - b) / (max1 - min1)
		elif g >= max(r, b):
				h = 2+ (b - r) / (max1 - min1)
		else:
				h = 4+ (r - g) / (max1 - min1)
		h = h *60
		if h > 360 : h = h -360
		if h < 0 : h = 360 -h

		return [int(h), int(s*100), int(l*100)]

	def change_colorname_rgb (self, input_scolor):
		result = self.change_scolor_rgb(input_scolor)
		return result

	def change_scolor_rgb (self, input_scolor):
		"""
		입력형식 : scolor형식, 12, red45, red
		결과 : [R, G, B]
		입력된 자료를 기준으로 rgb값을 돌려주는것 (숫자만이냐, 색이름, color_step)
		"""
		[number_only, color_name, color_step] = self.check_scolor_value(input_scolor)

		if number_only != "":
			#만약 숫자만 입력을 햇다면, 엑셀 번호로 생각하는것
			r_no, g_no, b_no = self.common_data["list_56rgb_forexcel"][int(number_only)]
		else:
			#색을 번호로 변경하는것
			print(color_name)
			color_index = self.common_data["dic_color_index"][color_name]

			if color_name =="whi" or color_name =="bla" or color_name =="gra":
				#만약 색이 흰색, 검정, 회색일경우는 h,s는 0으로 한다
				l_code_dic = {"bla": 0, "gra": 50, "whi": 100}
				h_code = 0
				s_code = 0
				l_code = int(l_code_dic[color_name]) + int(color_step)
			elif color_name and color_step == 0:
				# 기본색 인경우
				h_code, s_code, l_code = self.common_data["list_basic_12hsl"][color_index]
			else:
				# 기타 다른 경우
				h_code = self.common_data["dic_colorname_hnum"][color_name]
				s_code = 100
				l_code = int(color_step)

			if int(l_code) > 100 : l_code = 100
			if int(l_code) < 0 : l_code = 0

		result = self.change_hsl_rgb([h_code, s_code, l_code])
		final_rgb = [result[0], result[1], result[2]]

		return final_rgb

	def change_scolor_hsl (self, input_scolor):
		"""
		입력형식 : scolor형식, 12, red45, red
		결과 : [R, G, B]
		입력된 자료를 기준으로 rgb값을 돌려주는것 (숫자만이냐, 색이름, color_step)
		"""
		[number_only, color_name, color_step] = self.check_scolor_value(input_scolor)

		if number_only != "":
			#만약 숫자만 입력을 햇다면, 엑셀 번호로 생각하는것
			r_no, g_no, b_no = self.common_data["list_56rgb_forexcel"][int(number_only)]
		else:
			#색을 번호로 변경하는것
			color_index = self.common_data["dic_color_index"][color_name]

			if color_name =="whi" or color_name =="bla" or color_name =="gra":
				#만약 색이 흰색, 검정, 회색일경우는 h,s는 0으로 한다
				l_code_dic = {"bla": 0, "gra": 50, "whi": 100}
				h_code = 0
				s_code = 0
				l_code = int(l_code_dic[color_name]) + int(color_step)
			elif color_name and color_step == 0:
				# 기본색 인경우
				h_code, s_code, l_code = self.common_data["list_basic_12hsl"][color_index]
			else:
				# 기타 다른 경우
				h_code = self.common_data["list_basic_12h"][color_name]
				s_code = 100
				l_code = int(color_step)

			if int(l_code) > 100 : l_code = 100
			if int(l_code) < 0 : l_code = 0

		result = [h_code, s_code, l_code]

		return result

	def change_hsl_bystep (self, input_hsl, s_step="++", l_step="++"):
		"""
		bystep : 계단과 같이 일정 량을 한번에 올리거나 내리는 것
		입력형식 : hsl값을 올리거나 내리는 것
		입력 : [[36, 50, 50], "++", "--"]
		약 5씩이동하도록 만든다
		"""
		step_no = 5 #5단위씩 변경하도록 하였다
		h, s, l = input_hsl
		if s_step == "":
			pass
		elif s_step[0] == "+":
			s = s + len(s_step)*step_no
			if s < 0: s=0
		elif s_step[0] == "-":
			s = s - len(s_step)*step_no
			if s >100: s=100

		if l_step == "":
			pass
		elif l_step[0] == "+":
			l = l + len(l_step)*step_no
			if l < 0: l=0
		elif l_step[0] == "-":
			l = l - len(l_step)*step_no
			if l >100: l=100

		result = [h, s, l]
		return result

	def change_scolor_bystyle (self, input_scolor="red45", color_style="파스텔", style_step = 5):
		"""
		입력된 기본 값을 스타일에 맞도록 바꾸는것
		스타일을 강하게 할것인지 아닌것인지를 보는것
		color_style : pccs의 12가지 사용가능, 숫자로 사용가능, +-의 형태로도 사용가능
		입력예 : 기본색상, 적용스타일, 변화정도,
		        ("red45, 파스텔, 3)
		변화정도는 5를 기준으로 1~9까지임
		"""

		basic_rgb = self.check_color_rgb(input_scolor)

		basic_hsl = self.change_rgb_hsl(basic_rgb)
		step_1 = self.common_data["dic_num_slstep"][str(style_step)]
		step_2 = self.common_data["dic_num_slstep_small"][color_style]

		h = int(basic_hsl[0])
		s = int(basic_hsl[1]) + int(step_1[1]) + int(step_2[1])
		l = int(basic_hsl[2]) + int(step_1[2]) + int(step_2[2])

		changed_rgb = self.change_hsl_rgb([h,s,l])
		return changed_rgb

	def change_hsl_bystyle (self, input_hsl, color_style, small_change = 5):
		"""
		입력된 기본 값을 스타일에 맞도록 바꾸는것
		스타일을 강하게 할것인지 아닌 것인지를 보는것
		입력예 : 기본색상, 적용스타일, 변화정도, "red45, 파스텔, 3
		변화정도는 5를 기준으로 1~9까지임
		"""

		basic_hsl = input_hsl
		#파스테을 넣으면 기본 hsl을 돌려주는 것이다
		temp = self.common_data["dic_check_colorstyle"][color_style]
		step_1 = self.common_data["dic_num_slstep"][str(temp)]
		step_2 = self.common_data["dic_num_slstep_small"][str(small_change)]

		h = int(basic_hsl[0])
		s = int(step_1[0]) + int(step_2[0])
		l = int(step_1[1]) + int(step_2[1])

		if h > 360 : h = 360 - h
		if s > 100 : s = 100
		if l > 100 : l = 100
		if s < 0 : s = 0
		if l < 0 : l = 0

		r, g, b = self.change_hsl_rgb([h,s,l])

		return [int(r), int(g), int(b)]

	def check_scolor_value(self, input_scolor):
		"""
		입력값을 확인하는 것이다
		입력값 : "red++"
		출력값 : ["숫자만","색이름","변화정도"] ==> ["","red","60"]
		"""
		l_no_gap = 0
		number_only = ""
		color_name =""
		color_no = 0

		#색을 나타내는 글자를 추출해서,
		# 기본색이름으로 변경하는 것이다
		re_com1 = re.compile("[a-zA-Z가-힣]+")
		color_str = re_com1.findall(input_scolor)
		if color_str != []:
			color_name = self.common_data["dic_check_colorname"][color_str[0]]

		# 새롭게 정의해 보자
		#숫자로 정도를 표기한것인지를 알기위하여 숫자를 추출한다
		re_com2 = re.compile("[0-9]+")
		no_str = re_com2.findall(input_scolor)
		if no_str != []:
			color_no = int(no_str[0])
			if str(no_str[0]) == str(input_scolor):
					number_only = color_no
		#+나-를 추출하기위한 코드이다
		re_com3 = re.compile("[+]+")
		color_plus = re_com3.findall(input_scolor)
		if color_plus != []:
			color_no = 50 + 5 * len(color_plus[0])

		re_com4 = re.compile("[-]+")
		color_minus = re_com4.findall(input_scolor)
		if color_minus != []:
			color_no = 50 - 5 * len(color_minus[0])

		result = [number_only, color_name, color_no]
		return result

	def check_colorname(self, input_scolor):
		"""
		입력값을 확인하는 것이다
		입력값 : "red"
		출력값 : ["숫자만","색이름","변화정도"] ==> ["","red","60"]
		"""
		print(input_scolor)
		color_name = self.common_data["dic_check_colorname"][input_scolor]
		color_h_no = self.common_data["list_basic_12h"][color_name]
		return color_h_no

	def get_pastel_rgblist (self):
		"""
		자료가 있는 색들의 배경색으로 사용하면 좋은 색들
		"""
		color_set = self.common_data["list_basic_12hsl"][:-4]
		result = []
		print(color_set)
		for color_hsl in color_set:
			rgb = self.change_style_byhsl(color_hsl, "pastel", 4)
			result.append(rgb)
		return result

	def get_rgb_wbg (self, color_name, big_no, small_no):
		"""
		white, black, gray에대한 부분은 다시 정리해서 적용하도록 한다
		print("white, black, gray ===>", color_name, big_no, small_no)
		"""
		basic_rgb = 0
		rgb_diff = (5 - int(big_no)) * 25 + (5 - int(small_no)) * 3
		if color_name =="whi":
			basic_rgb = 255 + rgb_diff
			if basic_rgb >= 255: basic_rgb =255
		elif color_name =="gra":
			basic_rgb = 128 + rgb_diff
		elif color_name =="whi":
			basic_rgb = rgb_diff
			if basic_rgb <= 0: basic_rgb = 0
		return [basic_rgb, basic_rgb, basic_rgb]

	def get_rgb_near_10colors (self, input_color = "red", step = 10):
		"""
		하나의 색을 지정하면 10가지의 단계로 색을 돌려주는 것이다
		"""
		result =[]
		for no in range(0,100,int(100/step)):
			temp = self.check_color_rgb(input_color+str(no))
			result.append(temp)
		return result

	def get_rgblist_byno(self, input_no=12):
		"""
		360도로 나누어진 색을 입력숫자에 맞도록 나누어서 만드는 것
		기본은 12가지 색
		"""
		result = []
		for one in range(0, 360, 10):
			temp=[one, 100, 50]
			rgb = self.change_hsl_rgb(temp)
			result.append(rgb)
		return result[input_no-1]

	def get_faber_colorset(self, start_color=11, code = 5):
		"""
		파버 비덴의의 색체 조화론을 코드로 만든것이다
		한가지 색에대하 ㄴ조화를 다룬것
		"""
		# White(100-0) - Tone(10-50) - Color(0-0) : 색이 밝고 화사
		# Color(0-0) - Shade(0-75) - Black(0-100) : 색이 섬세하고 풍부
		# White(100-0) - GrayGray(25-75) - Black(0-100) : 무채색의 조화
		# Tint(25-0) - Tone(10-50) - Shade(0-75) 의 조화가 가장 감동적이며 세련됨
		# White(100-0) - Color(0-0) - Black(0-100) 는 기본적인 구조로 전체적으로 조화로움
		# Tint(25-0) - Tone(10-50) - Shade(0-75) - Gray(25-75) 의 조화는 빨강, 주황, 노랑, 초록, 파랑, 보라와 모두 조화를 이룬다
		h_list = self.common_data["list_basic_12h"]
		sl_faber = self.common_data["list_faber_sl"]

		h_no = self.check_colorname(start_color)
		result = []
		temp_hsl = sl_faber[code]
		for one_sl in temp_hsl:
			rgb = self.change_hsl_rgb([h_no, one_sl[0], one_sl[1]])
			result.append(rgb)
		return result

	def get_johannes_colorset(self, start_color=11, num_color = 4, stongness = 5):
		"""
		요하네스 이텐의 색체 조화론을 코드로 만든것이다
		"""
		# start_color : 처음 시작하는 색 번호, 총 색은 12색으로 한다
		# num_color : 표현할 색의 갯수(2, 3, 4, 6만 사용가능)
		# stongness : 색의 농도를 나타내는 것, 검정에서 하양까지의 11단계를 나타낸것, 중간이 5이다
		h_list = self.common_data["list_basic_12h"]
		sl_list = self.common_data["list_basic_11sl"]
		hsl_johannes = self.common_data["list_johannes_hsl"]
		color_set = [[], [], [0, 6], [0, 5, 9], [0, 4, 7, 10], [0, 3, 5, 8, 10], [0, 3, 5, 7, 9, 11]]

		h_no = self.check_colorname(start_color)
		new_color_set = []
		for temp in color_set[num_color]:
			new_color_set.append((temp + int(h_no / 30)) % 12)

		result = []
		for no in new_color_set:
			temp_hsl = hsl_johannes[no][stongness]
			rgb = self.change_hsl_rgb(temp_hsl)
			result.append(rgb)
		return result

	def get_pccs_colorset(self, rgb):
		"""
		pccs : 일본색체연구서가 빌표한 12가지 색으로 구분한것
		어떤 입력된 색의 기본적인 PCSS 12색을 돌려준다
		pccs톤, rgb로 넘어온 색을 pcss톤 12개로 만들어서 돌려준다
		"""
		result = []
		h, s, l = self.change_rgb_hsl(rgb)
		result4 = self.common_data["list_colorstyle_eng"]
		for one in result4:
			result.append([h, one[0], one[1]])
		return result

	def get_colormode(self, mode):
		mode_dic = {
			"저명도": "001", "중명도": "005", "고명도": "009", "저채도+저명도 = 단색조합": "011", "중명도+부드러움": "105",
			"고명도+부드러움": "109", "저채도": "199", "인접색조화-강": "500",
			"저명도+약간 어두움": "505", "명도차가 큰 배색 + 색상을 근접 보섹": "509",
			"중채도": "510", "고채도": "599", "고명도 +부드러움": "900",
			"보색": "bo", "보색근처2색": "2bo", "보색을 3개로나눈것": "3bo",
			"001": "001", "005": "005", "009": "009", "011": "011", "105": "105",
			"109": "109", "199": "199", "500": "500", "505": "505", "509": "509",
			"510": "510", "599": "599", "900": "900", "bo1": "bo1", "bo2": "bo2", "bo3": "bo3",
			}
		result = mode_dic[mode]
		return result

	def mix_two_rgb(self, rgb1, rgb2):
		"""
		2개의 rgb를 섞는것
		결과값 : RGB
		"""
		r1, g1, b1 = rgb1
		r2, g2, b2 = rgb2
		result = [int(r1*r2/255),int(g1*g2/255), int(b1*b2/255)]
		return result


	###############################################################
	# data로 시작하는 함수는 입력값이 없이 어떤 자료의 형태를 갖고오는 것이다

	def data_pccs_colorname(self):
		"""
		pccs : 일본색체연구서가 빌표한 12가지 색으로 구분한것
		어떤 입력된 색의 기본적인 PCSS 12색을 돌려준다
		pccs톤, rgb로 넘어온 색을 pcss톤 12개로 만들어서 돌려준다
		"""
		result = self.common_data["list_colorname_pccs"]
		return result

	def data_other_colorstyle(self):
		result = ["보색", "근접보색", "등간격3색조합", "인접색조화", "고채도배색", "저채도배색", "고명도배색", "고명도배색_약간부드러운이미지", "중명도배색", "저중명도배색",
		          "명도차가큰배색_색상을근접보색", "채도차가큰배색"]
		return result

	def data_basic_14rgb (self):
		"""
		기본적으로 자장된 자료에서 갖고오는 것이다
		많이 사용하는 다른 색들을 사용하기 위해
		테두리, 폰트색이나 단색으로 나타낼때 사용하면 좋다
		"""
		result = self.common_data["list_basic_12rgb"][0:13]
		return result

	def data_basic_12hsl (self):
		"""
		360도의 색을 30도씩 12개로 구분한 hsl분류표
		"""
		result = self.common_data["list_basic_12hsl"]
		return result

	def data_basic_36hsl (self):
		"""
		기본적인 hsl로된 36색을 갖고온다
		빨간색을 0으로하여 시작한다
		결과값 : hsl
		"""
		result = []
		for one in range(0, 360, 10):
			temp=[one, 100, 50]
			result.append(temp)
		return result

	def data_colorname_eng_all(self):
		"""
		기본 13가지 색의 리스트 : 영어
		"""
		result = list(self.common_data["list_colorname_eng"])
		return result

	def data_colorname_kor_all(self):
		"""
		기본 13가지 색의 리스트 : 한글
		"""
		result = self.common_data["list_colorname_kor"]
		return result

	def data_excel_56rgb(self):
		"""
		엑셀 기본 rgb 색 : 56색
		"""
		result = self.common_data["list_56rgb_forexcel"]
		return result

	def data_excel_46rgb(self):
		"""
		색 갯수 : 46색
		엑셀의 56색중에서 같은것을 삭제하고, 하양과 검정을 뒤로 넘기고 어두운 부분을 뒤로 좀 옮긴것
		"""
		result = self.common_data["list_46rgb_forexcel"]
		return result


