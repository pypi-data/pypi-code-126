#  -*- coding: utf-8 -*-

import os, glob, sys
import sqlite3
class sqlite:
    def __init__(self, file_location):
        # databse가 있는 화일의 위치를 알려주면 시작이 된다
        self.con = sqlite3.connect(file_location)
        self.curs = self.con.cursor()
        self.path = file_location
        self.database_name = ""
        self.table_name = ""

    def manual (self):
        result = """
            이번의것은 sql을 관리하기위한 자료이다
            금번에는 sqlite를 사용하는 기준으로 만든다
        
        """
        return result

    def make_database (self, database_name):
        #새로운 데이터베이스를 만든다
        self.database_name = database_name
        new_sql = "CREATE DATABASE %s;" % (self.database_name)
        print(new_sql)

    def read_database_name_all (self, path):
        #모든 database의 이름을 갖고온다
        #모든이 붙은것은 맨뒤에 all을 붙인다
        result=[]
        for fname in os.listdir(path) :
            result.append(fname)
        return result

    def change_table_name (self, old_name, new_name):
        new_sql = "alter table %s rename to %s" % (old_name, new_name)
        print(new_sql)
        self.run_sql_only(new_sql)

    def read_table_name_all (self):
        #모든 Table의 이름을 갖고온다
        self.curs.execute("select name from sqlite_master where type = 'table'; ")
        return self.curs.fetchall()

    def add_table (self, new_table_name, columns):
        #새로운 테이블을 만든다
        tables = []
        self.curs.execute("select name from sqlite_master where type = 'table'; ")
        for one_table_name in self.curs.fetchall():
            tables.append(one_table_name[0])
        if not new_table_name in tables:
            self.curs.execute("CREATE TABLE " + new_table_name + " (Item text)")

    def add_column (self, table_name, column_name, column_type):
        #새로운 컬럼을 만든다
        for data1, data2 in [["'",""], ["/",""], ["\\",""],[".",""]]:
            column_name=column_name.replace(data1, data2)
        self.curs.execute("alter table %s add column '%s' '%s'" % (table_name, column_name, column_type))

    def add_column_all (self, table_name, input_column_names):
        #새로운 컬럼을 만든다
        result=[]
        for column_name in input_column_names:
            for data1, data2 in [["'",""], ["/",""], ["\\",""],[".",""]]:
                column_name=column_name.replace(data1, data2)
            self.curs.execute("alter table %s add column '%s' 'text'" % (table_name, column_name))
            result.append(column_name)
        return result

    def delete_column(self, table_name, column_name):
        #컬럼을 삭제한다
        sql = ("ALTER TABLE %s DROP COLUMN %s " %(table_name, column_name))
        self.curs.execute(sql)

    def delete_column_all (self, table_name, input_column_names):
        #컬럼을 삭제한다
        for column_name in input_column_names:
            sql = ("ALTER TABLE %s DROP COLUMN %s " %(table_name, column_name))
            self.curs.execute(sql)

    def read_column_name_all (self, table_name):
        #해당하는 테이의 컬럼구조를 갖고온다
        self.curs.execute("PRAGMA table_info('%s')" %table_name)
        result = []
        for temp_2 in self.curs.fetchall() :
            result.append(temp_2[1].lower())
            print(temp_2)
        return result

    def read_all_column_property (self, table_name):
        #해당하는 테이블의 컬럼의 모든 구조를 갖고온다
        self.curs.execute("PRAGMA table_info('%s')" %table_name)
        result = []
        for temp_2 in self.curs.fetchall() :
            result.append(temp_2)
        return result

    def write_data(self, table_name, column_names, column_value):
        sql_columns = ""
        sql_values = ""
        for column_data in column_names:
            sql_columns = sql_columns + column_data + ", "
            sql_values = "?," * len(column_names)
        sql = "insert into %s(%s) values (%s)" % (table_name, sql_columns[:-2], sql_values[:-1])
        if type(column_value[0]) == type([]):
            self.curs.executemany(sql, column_value)
        else:
            self.curs.execute(sql, column_value)
        self.con.commit()

    def read_table_data_all (self, table_name):
        #모든 자료를 읽어온다
        self.curs.execute(("select * from %s") %table_name)
        result = self.curs.fetchall()
        return result

    def read_table_data_from_to (self, table_name, offset= 0, row_count=100):
        #모든 자료를 읽어온다
        self.curs.execute(("select * from %s LIMIT %s, %s;") %(table_name,str(offset), str(row_count)))
        result = self.curs.fetchall()
        return result

    def change_waste_data (self, original_data):
        #특수문자를 제거하는것
        result=[]
        for one_data in original_data:
            temp=""
            for one in one_data:
                if str(one) in ' 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_':
                    temp = temp+str(one)
            result.append(temp)
        return result

    def check_title_name (self, temp_title):
        #각 제목으로 들어가는 글자에 대해서 변경해야 하는것을 변경하는 것이다
        for temp_01 in [[" ","_"],["(","_"],[")","_"],["/","_per_"],["%",""],["'",""],['"',""],["$",""],["__","_"],["__","_"]]:
            temp_title = temp_title.replace(temp_01[0],temp_01[1])
        if temp_title[-1] =="_" : temp_title=temp_title[:-2]
        return temp_title

    def check_column_name_all (self, table_name):
        #Column의 이름을 변경한다
        for column_data in self.column_names (table_name):
            column_data_new = column_data.replace(" ","_")
            if not column_data_new == column_data:
                tem_2= self.curs.execute("alter table %s RENAME COLUMN ? to %s" %(table_name, column_data, column_data_new))

    def check_unique_column (self, data1, data2):
        #고유한 컬럼만 골라낸다
        result = []
        columns = self.read_column_names(data1)
        update_data2 = self.change_waste_data (data2)
        for temp_3 in update_data2 :
            if not temp_3.lower() in columns:
                result.append(temp_3)
        return result

    def read_notnull_no (self, table_name):
        #각 컬럼의 빈것이아닌 자료가 들어가있는것의 갯수를 구한다
        for column_data in self.column_names (table_name):
            self.curs.execute("select COUNT(*) from sjpark where %s is not null" %column_data)
            tem_2= self.curs.fetchall()[0][0]

    def change_data (self, table_name, column1, column2):
         #값을 변경한다
        no=1
        self.curs.execute("select rowid, %s from %s where %s is not null" %(column1,table_name,  column1))
        for rowid_value in self.curs.fetchall():
            self.curs.execute("select %s from %s where rowid = %s" %(column2, table_name, rowid_value[0]))
            temp_result_2=self.curs.fetchall()
            new_value = temp_result_2[0][0]
            no=no+1
            try:
                if not temp_result_2[0][0]:
                    self.curs.execute("update %s set %s = '%s' where rowid = '%s'" %(table_name, column2, rowid_value[1].replace("'",""), rowid_value[0]))
                    self.curs.execute("update %s set %s = Null where rowid = %s" %(table_name, column1, rowid_value[0]))
                    self.con.commit()
            except:
                pass

    def delete_empty_column (self, table_name):
        #테이블의 컬럼중에서 아무것도 없는 컬럼을 삭제하는 것이다
        for column_data in self.column_names (table_name):
            sql = ("select COUNT(*) from %s where %s is not null" %(table_name, column_data))
            self.curs.execute(sql)
            if self.tem_2 == self.curs.fetchall()[0][0]:
                sql = ("ALTER TABLE %s DROP COLUMN %s " %(table_name, column_data))
                print ("삭제---->", column_data)
                self.curs.execute(sql)

    def delete_empty_data(self, table_name, column_name):
        #테이블의 내용중에 전체자료가 빈 행을 지우는 것
        self.curs.execute("SELECT "+column_name+" FROM "+table_name+" WHERE Qty IS NULL ;")

    def run_sql (self, sql):
        result=[]
        self.curs.execute(sql)
        col_name_list = [tuple[0] for tuple in self.curs.description]
        result= self.curs.fetchall()
        self.con.commit()
        return [col_name_list, result]

    def run_sql_only(self, sql):
        result = []
        self.curs.execute(sql)
        result = self.curs.fetchall()
        self.con.commit()
        return result

    # 각 컬럼의 빈것이아닌 자료가 들어가있는것의 갯수를 구한다
    def check_column_dat_no(self, table_name):
        for column_data in self.column_names(table_name):
            sql = ("select COUNT(*) from sjpark where %s is not null" % column_data)
            self.curs.execute(sql)
            tem_2 = self.curs.fetchall()[0][0]

    def make_sql_for_new_table(self, table_name, column_datas):
        # 새로운 테이블용 sql을 만든다
        for column_data in column_datas:
            column_data = column_data.replace("'", "")
            column_data = column_data.replace("/", "")
            column_data = column_data.replace("\\", "")
            column_data = column_data.replace(".", "")
            print (column_data)
            self.curs.execute("alter table %s add column '%s' 'text'" % (table_name, column_data))
            self.con.commit()
            self.result.append(column_data)
        print ("added")

    def data_convert (self, original_data):
        #영문과 숫자와 공백을 제거하고는 다 제거를 하는것
        result=[]
        for one_data in original_data:
            temp=""
            for one in one_data:
                if str(one) in ' 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_':
                    temp = temp+str(one)
            result.append(temp)
        return result