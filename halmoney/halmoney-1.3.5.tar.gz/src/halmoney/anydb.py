# -*- coding: utf-8 -*-
import os
import sqlite3
import pandas as pd
from halmoney import youtil
from halmoney import pcell
from halmoney import pynal

class anydb:
	def __init__(self):
		self.yt = youtil.youtil()
		self.nal = pynal.pynal()
		self.table_name = ""
		self.path = ""
		self.database_name = "temp_18760829"
		self.con = ""
		self.curs = ""
		self.table_name = ""

	def add_string_words(self, input_list, chain_word =" ,"):
		# 리스트 자료들을 중간문자를 추가하여 하나의 문자열로 만드는 것,
		# “aa, bbb, ccc” 이런 식으로 만드는 방법이다
		result = ""
		for one_word in input_list:
			result = result+ str(one_word) + str(chain_word)

		return result[:-len(chain_word)]

	def change_list_to_df(self, col_list, val_list2d):
		#print("컬럼이름이요", col_list)
		#print("값들입니다", val_list2d)
		df_obj = pd.DataFrame(data=val_list2d, columns=col_list)
		return df_obj

	def change_excel_to_df(self, excel_list):
		"""
		엑셀의 자료를 pcell의 read_range_value를 이용해서 읽어온 자료일때
		"""
		xl_col_list = excel_list[0]
		xl_data_list = excel_list[1:]
		df_obj = pd.DataFrame(data=xl_data_list, columns=xl_col_list)
		return df_obj

	def change_dic_to_df(self, input_dic):
		"""
		pandas에서 사전으로 dataframe를 만드는 방법은 여러기지 이다
		그중에, 여기서 공통적으로 사용할 부분은
		아래의 방식을 사용하길 하자 (series형태로 하는 것이다)
		data = {"calory": [123, 456, 789],
                "기간": [10, 40, 20]}
		index로 나타나는 번호는 주요하지 않으므로 사용하지 않는다
		이것은 series형태인 것이다
		"""
		df_obj = pd.DataFrame(data=input_dic)
		return df_obj

	def change_df_to_dic_list(self, input_df):
		"""
		dataframe를 사전이면서 값의형태가 list인것
		"""
		result = df_obj.to_dict('list')
		return result

	def change_df_to_dic_series(self, input_df):
		"""
		dataframe를 사전이면서 값의형태가 series인것
		"""
		result = df_obj.to_dict('series')
		return result

	def change_df_to_dic_records(self, input_df):
		"""
		dataframe를 사전이면서 값의형태가 recoreds인것
		"""
		result = df_obj.to_dict('records')
		return result

	def change_df_to_dic_index(self, input_df):
		"""
		dataframe를 사전이면서 값의형태가 index인것
		"""
		result = df_obj.to_dict('index')
		return result


	def change_df_to_excel(self, df_obj, xy = [1,1]):
		col_list = df_obj.columns.values.tolist()
		value_list = df_obj.values.tolist()
		excel=pcell.pcell()
		excel.add_sheet()
		excel.write_range_value("", xy, [col_list])
		excel.dump_range_value("", [xy[0]+1, xy[1]], value_list)




	def change_df_to_dic(self, df_obj):
		#df자료를 dic으로 만든 것이다
		#{'columns': ['a', 'b'],
		# 'data': [['red', 0.5], ['yellow', 0.25], ['blue', 0.125]],
		# 'index': [0, 1, 2]}
		result = df_obj.to_dict('split')
		return result

	def change_dfdic_to_list(self, df_dic):
		#df사전형식의 자료를 리스트로 만드는 것
		#{'index': [0, 1, 2], 'columns': ['kg', '날씨'], 'data': [[67, '맑음'], [89, '흐림'], [123, '비']]}
		col_list1d = df_dic["columns"]
		value_list2d = df_dic["data"]
		value_list2d.insert(0, col_list1d)
		return value_list2d

	def change_list_to_dfdic(self, input_list):
		#df사전형식의 자료를 리스트로 만드는 것
		#입력값 : [['kg', '날씨'], [67, '맑음'], [89, '흐림'], [123, '비']]
		#출력값 : {'columns': ['kg', '날씨'], 'data': [[67, '맑음'], [89, '흐림'], [123, '비']]}
		result = {}
		result['columns'] = input_list[0]
		result['data'] = input_list[1:]
		return result

	def change_dfdic_to_df(self, df_dic):
		#df사전형식의 자료를 리스트로 만드는 것
		col_list = df_dic['columns']
		val_list = df_dic['data']
		df_obj_1 = pd.DataFrame(data=val_list, columns=col_list)
		return df_obj_1

	def change_df_to_list(self, df_obj):
		#df자료를 리스트로 만든 것이다
		col_list1d = df_obj.keys().to_list()
		#col_list2d = self.yt.change_list_1d_2d(col_list1d)
		value_list2d = df_obj.values.tolist()
		value_list2d.insert(0, col_list1d)
		return value_list2d

	def change_df_to_sqlite(self, db_name, table_name, df_data):
		result = self.df_write_to_sqlite(db_name, table_name, df_data)
		return result

	def change_dic_to_sqlite(self, dic_data):
		result = self.sqlite_write_by_dic_data(self, dic_data)
		return result

	def change_sqlite_to_df(self, db_name, sqlite_tb_name):
		# sqlite를 df로 만드는것
		if self.con == "":
			self.con = sqlite3.connect(db_name, isolation_level=None)
		self.curs = self.con.cursor()
		sql = ("SELECT * From {}").format(sqlite_tb_name)
		query = self.curs.execute(sql)
		cols = [column[0] for column in query.description]
		df_obj = pd.DataFrame.from_records(data=query.fetchall(), columns=cols)
		return df_obj

	def change_list_to_sqlite(self, column_names, list_values):
		result = self.sqlite_write_list_data(column_names, list_values)
		return result

	def change_sqlite_to_list(self, db_name, sqlite_tb_name):
		# sqlite를 df로 만드는것
		# 출력 : [2차원리스트(제목), 2차원리스트(값들)]
		if self.con == "":
			self.con = sqlite3.connect(db_name, isolation_level=None)
		self.con.row_factory = sqlite3.Row
		self.curs = self.con.cursor()
		sql = "SELECT * From %s" % (sqlite_tb_name)
		query = self.curs.execute(sql)
		result = []
		cols = [column[0] for column in query.description]

		aaa = []
		for one in query.fetchall():
			aaa.append(list(one))
		result =[cols, aaa]
		#print(cols)
		return result

	def check_y_name(self, temp_title):
		# 각 제목으로 들어가는 글자에 대해서 변경해야 하는것을 변경하는 것이다
		for temp_01 in [[" ", "_"], ["(", "_"], [")", "_"], ["/", "_per_"], ["%", ""], ["'", ""], ['"', ""], ["$", ""],
		                ["__", "_"], ["__", "_"]]:
			temp_title = temp_title.replace(temp_01[0], temp_01[1])
		if temp_title[-1] == "_": temp_title = temp_title[:-2]
		return temp_title

	def df_append(self, df_obj_1, df_obj_2):
		# df_obj_1의 자료에 df_obj_2를 맨끝에 추가하는것
		df_obj_1 = pd.concat([df_obj_1, df_obj_2])
		return df_obj_1

	def df_check_range(self, input_list):
		#df의 자료를 갖고올때 사용할수있는 범위형태를 분석하는 것이다
		# 예 : ["3~4"]
		temp = []
		for one in input_list:
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

	def df_change_tolist(self, df_obj):
		# df자료를 커럼과 값을 기준으로 나누어서 결과를 돌려주는 것이다
		result = []
		col_list = df_obj.columns.values.tolist()
		value_list = df_obj.values.tolist()
		return [col_list, value_list]

	def df_delete_emptycolumn(self, df_obj):
		# dataframe의 빈열을 삭제
		# 제목이 있는 경우에만 해야 문제가 없을것이다
		nan_value = float("NaN")
		df_obj.replace(0, nan_value, inplace=True)
		df_obj.replace("", nan_value, inplace=True)
		df_obj.dropna(how="all", axis=1, inplace=True)
		return df_obj

	def df_insert_new(self, df_obj_1, df_obj_2):
		# df_obj_1의 자료에 df_obj_2를 맨끝에 추가하는것
		df_obj_1 = pd.concat([df_obj_1, df_obj_2])
		return df_obj_1

	def df_make_bylist(self, column_name, list2d):
		# df_obj_1의 자료에 df_obj_2를 맨끝에 추가하는것
		list2d =self.yt.change_list_1d_2d(list2d)
		df_obj_1 = pd.DataFrame(data=list2d, columns=column_name)
		return df_obj_1

	def df_make_bydic(self, input_dic):
		# df_obj_1의 자료에 df_obj_2를 맨끝에 추가하는것
		df_obj_1 = pd.DataFrame(input_dic)
		return df_obj_1

	def df_read_byno(self, df_obj, x, y):
		# pandas의 DataFrame의 자료의 일부를 쉽게 갖고오도록 만든것이다
		# 숫자번호로 pandas의 DataFrame의 일부를 불러오는 것이다
		# 단, 모든것을 문자로 넣어주어야 한다
		# x=["1:2", "1~2"] ===> 1, 2열
		# x=["1,2,3,4"] ===> 1,2,3,4열
		# x=[1,2,3,4]  ===> 1,2,3,4열
		# x=""또는 "all" ===> 전부
		x_list = self.df_check_range(x)
		y_list = self.df_check_range(y)
		exec("self.result = df_obj.iloc[{}, {}]".format(x_list, y_list))
		return self.result

	def df_read_byname(self, df_obj, x, y):
		# 열이나 행의 이름으로 pandas의 DataFrame의 일부를 불러오는 것이다
		# 이것은 리스트를 기본으로 사용한다
		# list_x=["가"~"다"] ===> "가"~"다"열
		# list_x=["가","나","다","4"] ===> 가,나,다, 4 열
		# x=""또는 "all" ===> 전부

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
		#print(temp)
		exec("self.result = df_obj.loc[{}, {}]".format(temp[0], temp[1]))
		return self.result

	def df_read_byxy(self, df_obj, xy=[0,0]):
		# 위치를 기준으로 값을 읽어오는 것이다
		# 숫자를 넣으면 된다
		result = df_obj.iat[int(xy[0]), int(xy[1])]
		return result

	def df_write_to_excel(self, df_obj, xy = [1,1]):
		# df자료를 커럼과 값을 기준으로 나누어서 결과를 돌려주는 것이다
		col_list = df_obj.columns.values.tolist()
		#print(col_list)
		value_list = df_obj.values.tolist()
		excel=pcell.pcell()
		excel.write_range_value("", xy, [col_list])
		excel.dump_range_value("", [xy[0]+1, xy[1]], value_list)

	def df_write_to_sqlite(self, db_name, table_name, df_data):
		# df자료를 sqlite에 새로운 테이블로 만들어서 넣는 것
		if self.con == "":
			db_name = self.sqlite_read_database_name_all()[0]
			self.con = sqlite3.connect(db_name, isolation_level=None)
		df_data.to_sql(table_name, self.con)

	def df_test_data(self):
		#가끔 코딩을 해보니, 테스트용데이터가 필요하더라구요
		dic_data ={"1번째열": {'Country': 'Russia', 'Capital': 'Moscow', 'Area(Sq.Miles)': 6601670, 'Population': 146171015},
		 "2번째열": {'Country': 'Canada', 'Capital': 'Ottawa', 'Area(Sq.Miles)': 3855100, 'Population': 38048738},
		 "3번째열": {'Country': 'China', 'Capital': 'Beijing', 'Area(Sq.Miles)': 3705407, 'Population': 1400050000},
		 "4번째열": {'Country': 'United States of America', 'Capital': 'Washington, D.C.', 'Area(Sq.Miles)': 3796742,'Population': 331449281},
		 "5번째열": {'Country': 'Brazil', 'Capital': 'Brasília', 'Area(Sq.Miles)': 3287956, 'Population': 210147125},
         "6번째열": {'Country': 'Russia', 'Capital': 'Moscow', 'Area(Sq.Miles)': 6601670,'Population': 146171015},
		 "7번째열": {'Country': 'Canada', 'Capital': 'Ottawa', 'Area(Sq.Miles)': 3855100,'Population': 38048738},
		 "8번째열": {'Country': 'China', 'Capital': 'Beijing', 'Area(Sq.Miles)': 3705407,'Population': 1400050000},
		 "9번째열": {'Country': 'United States of America', 'Capital': 'Washington, D.C.','Area(Sq.Miles)': 3796742,'Population': 331449281},
		 "10번째열": {'Country': 'Brazil', 'Capital': 'Brasília', 'Area(Sq.Miles)': 3287956,'Population': 210147125}
		           }
		df = pd.DataFrame(dic_data)
		return df

	def df_test_2(self):
		#가끔 코딩을 해보니, 테스트용데이터가 필요하더라구요
		# 간단하게 바꿔봄
		dic_data ={
		 "1번째열": {'A1': '러시아', 'Capital': 'Moscow', '면적': 6601670, '인구': 146171015},
		 "2번째열": {'A1': '카나다', 'Capital': 'Ottawa', '면적': 3855100, '인구': 38048738},
		 "3번째열": {'A1': '중국', 'Capital': 'Beijing', '면적': 3705407, '인구': 1400050000},
		 "4번째열": {'A1': '미국', 'Capital': 'Washington', '면적': 3796742,'인구': 331449281},
		 "5번째열": {'A1': '브라질', 'Capital': 'Brasília', '면적': 3287956, '인구': 210147125},
         "6번째열": {'A1': '러시아', 'Capital': 'Moscow', '면적': 6601670,'인구': 146171015},
		 "7번째열": {'A1': '카나다', 'Capital': 'Ottawa', '면적': 3855100,'인구': 38048738},
		 "8번째열": {'A1': '중국', 'Capital': 'Beijing', '면적': 3705407,'인구': 1400050000},
		 "9번째열": {'A1': '미국', 'Capital': 'Washington','면적': 3796742,'인구': 331449281},
		 "10번째열": {'A1': '브라질', 'Capital': 'Brasília', '면적': 3287956,'인구': 210147125}
		           }
		df = pd.DataFrame(dic_data)
		return df

	def sqlite_connect(self, database_name=""):
		#self.table_name = table_name
		#self.path = table_name
		self.database_name = database_name
		#기본적으로 test_db.db를 만든다
		# memory로 쓰면, sqlite3를 메모리에 넣도록 한다
		if self.database_name == "memory":
			self.con = sqlite3.connect(":memory:")

		#데이터베이스를 넣으면 화일로 만든다
		elif self.database_name == "" or self.database_name == "test":
			self.database_name = "test_db.db"
			self.check_databse(self.database_name)
			self.con = sqlite3.connect(self.database_name, isolation_level=None)
		else:
			self.con = sqlite3.connect(self.database_name, isolation_level=None)
		self.curs = self.con.cursor()

	def check_databse(self, db_name, path="."):
		#database는 파일의 형태이므로 폴더에서 화일이름들을 확인한다
		db_name_all = self.yt.read_filename_folder_all(path)
		if db_name in db_name_all:
			self.con = sqlite3.connect(self.database_name, isolation_level=None)
		else:
			self.con = sqlite3.connect("test_db.db", isolation_level=None)


	def sqlite_connect_with_table(self, table_name="", database_name=""):
		self.table_name = table_name
		self.path = table_name
		self.database_name = database_name
		#기본적으로 sqlite3를 메모리에 넣도록 한다
		if self.database_name == "" or self.database_name == "memory":
			self.con = sqlite3.connect(":memory:")
		#데이터베이스를 넣으면 화일로 만든다
		elif self.database_name == "test_db":
			self.database_name = "test_database_20140416"
			self.con = sqlite3.connect(self.database_name, isolation_level=None)
		else:
			self.con = sqlite3.connect(self.database_name, isolation_level=None)

		self.curs = self.con.cursor()
		if table_name == "":
			self.table_name = "temp_table"
			self.curs.execute("CREATE TABLE " + self.table_name + " (auto_no integer primary key AUTOINCREMENT)")
		elif table_name == "no_save":
			self.table_name = "no_save"
			self.curs.execute("DROP TABLE " + self.table_name)
			self.curs.execute("CREATE TABLE " + self.table_name + " (auto_no integer primary key AUTOINCREMENT)")
		elif table_name != "":
			self.curs.execute("select name from sqlite_master where type = 'table'; ")
			all_tables = self.curs.fetchall()
			#print(all_tables)
			found = "no"
			if all_tables:
				for one in all_tables:
					if table_name == one[0]:
						found = "yes"
			if found == "no" or not all_tables:
				self.curs.execute("CREATE TABLE " + self.table_name + " (auto_no integer primary key AUTOINCREMENT)")

	def sqlite_connect_in_memory(self, table_name=""):
		self.table_name = table_name
		self.path = table_name
		self.database_name == "temporary_database"
		self.con = sqlite3.connect(":memory:")
		self.con = sqlite3.connect(self.database_name, isolation_level=None)

		#self.curs = self.con.cursor()
		#self.table_name = "temp_table"
		#self.curs.execute("CREATE TABLE " + self.table_name + " (auto_no integer primary key AUTOINCREMENT)")

	def sqlite_save_memorydb_to_diskdb(self, database_name):
		"""memory에 저장된것을 화일로 저장하는것 """
		save_disk = sqlite3.connect(database_name)
		self.con.backup(save_disk)


	def sqlite_change_table_name(self, old_name, new_name):
		new_sql = "alter table %s rename to %s" % (old_name, new_name)
		#print(new_sql)
		self.run_sql_only(new_sql)

	def sqlite_change_y_name(self, table_name):
		# Column의 이름을 변경한다
		for column_data in self.column_names(table_name):
			column_data_new = column_data.replace(" ", "_")
			if not column_data_new == column_data:
				tem_2 = self.curs.execute(
					"alter table %s RENAME COLUMN ? to %s" % (table_name, column_data, column_data_new))

	def sqlite_delete_empty_y(self, table_name):
		# 테이블의 컬럼중에서 아무것도 없는 컬럼을 삭제하는 것이다
		for column_data in column_names(table_name):
			sql = ("select COUNT(*) from %s where %s is not null" % (table_name, column_data))
			self.curs.execute(sql)
			if tem_2 == self.curs.fetchall()[0][0]:
				sql = ("ALTER TABLE %s DROP COLUMN %s " % (table_name, column_data))
				#print("삭제---->", column_data)
				self.curs.execute(sql)

	def sqlite_delete_y(self, table_name, column_name):
		# 컬럼을 삭제한다
		sql = ("ALTER TABLE %s DROP COLUMN %s " % (table_name, column_name))
		self.curs.execute(sql)

	def sqlite_delete_yy(self, table_name, input_y_names):
		# 컬럼을 삭제한다
		for column_name in input_y_names:
			sql = ("ALTER TABLE %s DROP COLUMN %s " % (table_name, column_name))
			self.curs.execute(sql)

	def sqlite_delete_table(self, table_name):
		self.curs.execute("DROP TABLE " + table_name)

	def sqlite_new_y(self, new_col, column_type="TEXT"):
		# 새로운 y행을 만든느것
		# 기존의 테이블을 확인해서 없으면 컬럼을 넣는것
		# 컬름은 그냥 기본으로 text를 설정한다
		column_names = self.sqlite_read_table_colname_all()
		#for data1, data2 in [["'", ""], ["/", ""], ["\\", ""], [".", ""]]:
		#	column_name = column_name.replace(data1, data2)
		if not (new_col in column_names):
			self.curs.execute("alter table %s add column '%s' '%s'" % (self.table_name, new_col, column_type))

	def sqlite_new_table(self, new_table_name):
		# 새로운 테이블을 만든다
		tables = []
		self.curs.execute("select name from sqlite_master where type = 'table'; ")
		for one_table_name in self.curs.fetchall():
			tables.append(one_table_name[0])
		if not new_table_name in tables:
			self.curs.execute("CREATE TABLE " + new_table_name + " (Item text)")

	def sqlite_create_table_with_column(self, table_name, column_data_list):
		#어떤 형태의 자료가 입력이 되어도 테이블을 만드는 sql을 만드는 것이다
		#입력형태 1 : 테이블이름, [['번호1',"text"], ['번호2',"text"],['번호3',"text"],['번호4',"text"]]
		#입력형태 2 : 테이블이름, ['번호1','번호2','번호3','번호4']
		#입력형태 3 : 테이블이름, [['번호1',"text"], '번호2','번호3','번호4']

		sql_1 = "CREATE TABLE IF NOT EXISTS {}".format(table_name)
		sql_2 = sql_1 + " ("
		for one_list in column_data_list:
			if type(one_list) ==type([]):
				if len(one_list)==2:
					column_name = one_list[0]
					column_type = one_list[1]
				elif len(one_list)==1:
					column_name = one_list[0]
					column_type = "text"
			elif type(one_list) ==type("string"):
				column_name = one_list
				column_type = "text"
			sql_2 = sql_2 + "{} {}, ".format(column_name, column_type)
		sql_2 = sql_2[:-2] + ")"
		#print(sql_2)
		self.curs.execute(sql_2)
		return sql_2

	def sqlite_new_y_many(self, table_name, input_y_names):
		# 예: 테이블이름, ["이름1", "이름2"]
		# 새로운 컬럼을 만든다
		result = []
		for column_name in input_y_names:
			for data1, data2 in [["'", ""], ["/", ""], ["\\", ""], [".", ""]]:
				column_name = column_name.replace(data1, data2)
			self.curs.execute("alter table %s add column '%s' 'text'" % (table_name, column_name))
			result.append(column_name)
		return result

	def sqlite_read_database_name_all(self, path=".\\"):
		# 모든 database의 이름을 갖고온다
		# 모든이 붙은것은 맨뒤에 all을 붙인다
		result = []
		for fname in os.listdir(path):
			if fname[-3:] ==".db":
				result.append(fname)
		#print(result)
		return result

	def sqlite_read_table_name_all(self, database_name):
		# 해당하는 테이의 컬럼구조를 갖고온다
		con = sqlite3.connect(database_name, isolation_level=None)
		curs = con.cursor()
		curs.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")
		result = []
		for temp_2 in curs.fetchall():
			result.append(temp_2[0])
		#print(result)
		return result

	def sqlite_read_table_colname_all(self, table_name=""):
		# 해당하는 테이의 컬럼구조를 갖고온다
		if table_name =="":
			table_name = self.table_name
		self.curs.execute("PRAGMA table_info('%s')" % table_name)
		result = []
		for temp_2 in self.curs.fetchall():
			result.append(temp_2[1])
		return result

	def sqlite_read_table_data_all(self, table_name=""):
		# 모든 자료를 읽어온다
		if table_name =="":
			table_name = self.table_name
		self.curs.execute(("select * from {}").format(table_name))
		result = self.curs.fetchall()
		return result

	def sqlite_read_xx_byno(self, *input_list):
		# 불러오기 : st.rv_yy_no[1,2,3,4]...
		col_names = self.sqlite_read_table_colname_all()
		result = []
		for one in input_list:
			if "~" in str(one):
				aaa = str(one).split("~")
				start = int(aaa[0])
				end = int(aaa[1])
			elif ":" in str(one):
				aaa = str(one).split(":")
				start = int(aaa[0])
				end = int(aaa[1]) - 1
			else:
				start = 1
				end = int(one)

			limit_text = str(start) + ", " + str(end)
			sql = "SELECT * FROM {} ORDER BY auto_no limit {}".format(self.table_name, limit_text)
			#print(sql)
			self.curs.execute(sql)
			temp = self.curs.fetchall()
			result.extend(temp)
		self.con.commit()
		return result

	def sqlite_read_xy_byno(self, x, y):
		col_names = self.sqlite_read_table_colname_all()
		one_name = col_names[int(y)]
		limit_text = str(x) + ", " + str(x)
		sql = "SELECT {} FROM {} ORDER BY auto_no limit {}".format(one_name, self.table_name, limit_text)
		#print(sql)
		self.curs.execute(sql)
		result = self.curs.fetchall()
		return result[0][0]

	def sqlite_read_yy_byno(self, input_list, limit_no):
		# y행의 자료들을 불러오는것
		# 불러오기 : st.rv_yy_no[1,2,3,4]...
		col_names = self.sqlite_read_table_colname_all()
		temp_col = []
		for one in input_list:
			if "~" in str(one):
				aaa = str(one).split("~")
				start = int(aaa[0])
				end = int(aaa[1]) + 1
			elif ":" in str(one):
				aaa = str(one).split(":")
				start = int(aaa[0])
				end = int(aaa[1])
			else:
				start = int(one)
				end = int(one) + 1
			temp_col.extend(col_names[int(start):int(end)])
		#print(col_names, temp_col)
		result = self.sqlite_read_yy_byname(temp_col, limit_no)
		return result

	def sqlite_read_yy_name(self, yy_names="", condition="all"):
		# 문자는 컬럼이름으로, 숫자는 몇번째인것으로...
		if yy_names == "":
			sql_columns = "*"
		else:
			sql_columns = self.yt.add_string_words(yy_names, ", ")
		limit_text = "limit 10"
		sql = "SELECT {} FROM {} ORDER BY auto_no {}".format(sql_columns, self.table_name, limit_text)
		#print(sql)
		self.curs.execute(sql)
		result = self.curs.fetchall()
		return result

	def sqlite_read_yy_byname(self, yy_names="", condition="all"):
		#print(condition)
		# 문자는 컬럼이름으로, 숫자는 몇번째인것으로...
		if yy_names == "":
			sql_columns = "*"
		else:
			sql_columns = self.yt.add_string_words(yy_names, ", ")

		if condition=="all":
			lim_no = 100
		else:
			lim_no = condition
		limit_text = "limit {}".format(lim_no)
		sql = "SELECT {} FROM {} ORDER BY auto_no {}".format(sql_columns, self.table_name, limit_text)
		#print(sql)
		self.curs.execute(sql)
		result = self.curs.fetchall()
		return result

	def sqlite_run_sql(self, sql):
		result = []
		self.curs.execute(sql)
		result = self.curs.fetchall()
		self.con.commit()
		return result

	def sqlite_write_by_dic_data(self, dic_data):
		#사전의 키를 y이름으로 해서 값을 입력한다
		for one_col in list(dic_data[0].keys()):
			if not one_col in self.sqlite_read_table_colname_all():
				self.new_y(one_col)
		sql_columns = self.yt.add_string_words(list(dic_data[0].keys()), ", ")
		sql_values = "?," * len(list(dic_data[0].keys()))
		sql = "insert into %s (%s) values (%s)" % (self.table_name, sql_columns, sql_values[:-1])
		value_list = []
		for one_dic in dic_data:
			value_list.append(list(one_dic.values()))
		self.curs.executemany(sql, value_list)

	def sqlite_write_to_df(self, db_name, sqlite_tb_name):
		# sqlite를 df로 만드는것
		if self.con == "":
			self.con = sqlite3.connect(db_name, isolation_level=None)
		self.curs = self.con.cursor()
		sql = "SELECT * From %s" % (sqlite_tb_name)
		query = self.cur.execute(sql)
		cols = [column[0] for column in query.description]
		df_obj = pd.DataFrame.from_records(data=query.fetchall(), columns=cols)
		return result

	def sqlite_write_list_one_data(self, table_name, column_names, list_value):
		self.table_name = table_name
		#리스트의 형태로 넘어오는것중에 y이름과 값을 분리해서 얻는 것이다
		#for one_col in column_names:
		#	if not one_col in self.sqlite_read_table_colname_all():
		#		self.new_y(one_col)
		sql_columns = self.add_string_words(column_names, ", ")
		sql_values = "?," * len(list_value)
		sql = "insert into %s (%s) values (%s)" % (self.table_name, sql_columns, sql_values[:-1])
		#print(sql)
		self.curs.execute(sql, list_value)

	def sqlite_write_list_many_data(self, table_name,column_names, list_values):
		#리스트의 형태로 넘어오는것중에 y이름과 값을 분리해서 얻는 것이다
		self.table_name = table_name
		#for one_col in column_names:
		#	if not one_col in self.sqlite_read_table_colname_all():
		#		self.new_y(one_col)
		sql_columns = self.add_string_words(column_names, ", ")
		sql_values = "?," * len(list_values[0])
		sql = "insert into %s (%s) values (%s)" % (self.table_name, sql_columns, sql_values[:-1])
		#print(sql)
		self.curs.executemany(sql, list_values)