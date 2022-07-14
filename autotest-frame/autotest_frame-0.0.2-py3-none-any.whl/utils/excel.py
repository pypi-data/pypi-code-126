# -*- coding:utf-8 -*-
import pandas as pd


class Excel(object):
    """读写excel"""

    def __init__(self, file_path):
        self.file_path = file_path  # 类的初始化，定义了file_path属性

    def read_one_sheet(self, sheet_name=0):
        """读取任一个sheet数据，sheet_name传sheet名称或下标0，1，2...，不传默认为0（第一个sheet）"""
        df = pd.read_excel(self.file_path, sheet_name=sheet_name)  # 数据读取到DataFrame中
        res = df.values.tolist()  # 转成list数据类型
        return res

    def read_all(self):
        """读取Excel所有的sheet"""
        sheet_names = pd.ExcelFile(self.file_path).sheet_names  # 读取Excel表中所有sheet的名称
        data_all = []
        for sheet_name in sheet_names:
            data_one = Excel.read_one_sheet(self, sheet_name=sheet_name)
            data_all = data_all + data_one
        return data_all

    def read_row_index(self, start_row_index: int, end_row_index: int, sheet_name=0):
        """
        index：0开始，首行取不到，左闭右开：[start_row_index,end_row_index)
        start_row_index: 开始行
        end_row_index: 结束行
        """
        df = pd.read_excel(self.file_path, sheet_name=sheet_name)
        res = df.values[start_row_index: end_row_index].tolist()
        return res

    def read_col_index(self, col_index: int, sheet_name=0):
        """
        index：0开始
        usecols如果传入的是列表，下标为0，就取它第0列的数据
        """
        df = pd.read_excel(self.file_path, usecols=[col_index], sheet_name=sheet_name)
        # res = df.values.tolist()  # [[1], [2], [3]]
        res = [i[0] for i in df.values.tolist()]  # 读单独一列时需要时可转换[1, 2, 3]
        return res

    def read_col_name(self, col_name: str, sheet_name=0):
        df = pd.read_excel(self.file_path, sheet_name=sheet_name)
        res = df[col_name].values.tolist()
        return res

    def write_list_sheet(self, sheet_name, data, *args):
        """
        将列表数据存入Excel
        sheet_name: 表名称
        data: 需要写入的数据,必须为嵌套列表[[]]
        *args: 保存多余变量，保存方式为元组。(1, 2, 3...),元组取值通过下标
        """
        # 通过*args拿到表头
        header = []
        for i in args:
            header.append(str(i))
        df = pd.DataFrame(data, columns=header)
        # index 为FALSE 表示没有第一列数字为索引
        df.to_excel(self.file_path, sheet_name=sheet_name, index=False)

    def write_sheet(self, data: dict, sheet_name='sheet1', column_width=20):
        """
        data：{
            '标题列1': ['张三', '李四'],
            '标题列2': [80, 90]
        }
        """

        df = pd.DataFrame(data)
        writer = pd.ExcelWriter(self.file_path)  # 构造ExcelWriter对象作为to_excel持续写入
        df.to_excel(writer, sheet_name=sheet_name, index=False)
        """设置列宽"""
        # sheet = writer.sheets.get(sheet_name)
        # for index in range(len(df)):
        #     # print(index, value)
        #     for i in range(len(df.columns)):
        #         sheet.set_column(index + 1, i, column_width)
        writer.save()

    def write_sheets(self, sheet_dict: dict, column_width=20):
        """
        sheet_dict: {
            'sheet1_name': {'标题列1': ['张三', '李四'], '标题列2': [80, 90]},
            'sheet2_name': {'标题列3': ['王五', '郑六'], '标题列4': [100, 110]}
        }
        """
        writer = pd.ExcelWriter(self.file_path)
        for sheet_name, sheet_data in sheet_dict.items():
            df = pd.DataFrame(sheet_data)
            df.to_excel(writer, sheet_name=sheet_name, index=False)
            """设置列宽"""
            # sheet = writer.sheets.get(sheet_name)
            # for index in range(len(df)):
            #     for i in range(len(df.columns)):
            #         sheet.set_column(index + 1, i, column_width)
        writer.save()

    def get_sheet_names(self):
        return list(pd.read_excel(self.file_path, sheet_name=None))  # list()一个dict可以拿到它的键


class CSV(object):
    """读写csv"""

    def __init__(self, file_path):
        self.file_path = file_path

    def read_all(self):
        df = pd.read_csv(self.file_path)
        res = df.values.tolist()
        print(res)
        return res

    def read_row_index(self, row_index: int):
        """
        index: 从1开始
        """
        df = pd.read_csv(self.file_path)
        res = df.values[row_index - 1].tolist()
        print(res)
        return res

    def read_col_index(self, col_index: int):
        """
        index：从1开始
        """
        df = pd.read_csv(self.file_path, usecols=[col_index - 1])
        res = [r[0] for r in df.values.tolist()]
        print(res)
        return res

    def read_col_name(self, col_name: str):
        df = pd.read_csv(self.file_path, usecols=[col_name])
        res = [r[0] for r in df.values.tolist()]
        print(res)
        return res

    def write(self, data: dict, sheet_name='sheet1', column_width=20):
        """
        数据格式：{
            '标题列1': ['张三', '李四'],
            '标题列2': [80, 90]
        }
        """
        df = pd.DataFrame(data)
        df.to_csv(self.file_path, index=False)


if __name__ == '__main__':
    # r = Excel(file_path='D:/python/test_data.xls').read_one_sheet()
    # r = Excel(file_path='D:/python/test_data.xls').read_all()
    # r = Excel(file_path='D:/python/test_data.xls').read_row_index(0, 2)
    # r = Excel(file_path='D:/python/test_data.xls').read_col_index(0)
    data1 = {
            '标题列1': ['张三', '李四'],
            '标题列2': [80, 90]
        }
    sheet_dict1 = {
        'sheet1_name': {'标题列1': ['张三', '李四'], '标题列2': [80, 90]},
        'sheet2_name': {'标题列3': ['王五', '郑六'], '标题列4': [100, 110]}
    }
    Excel('D:/python/225.xlsx').write(data1, '1')
    Excel('D:/python/226.xlsx').write_sheets(sheet_dict1)
    # print(type(r))
    # print(len(r))
    # print(r)
