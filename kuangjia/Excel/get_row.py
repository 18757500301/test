# -*- coding: utf-8 -*-
from kuangjia.Excel.excel_row_col import OpenExcel
from kuangjia.Excel.excel_col import *
from kuangjia.data.get_data_json import data_values

class get_values:
    def __init__(self):
        self.open_table = OpenExcel()

    # 去获取Excel行数，就是我们的case总个数
    def get_nrows(self):
        return self.open_table.get_nrows()

    # 获取是否执行
    def get_is_run(self,row):
        res = None
        col = int(get_run())
        is_run = self.open_table.get_cell_value(row,col)
        if is_run == "yes":
            res = True
        else:
            res = False
        return res

    # 获取是否带有header请求头
    def get_header(self,row):
        col = int(get_header())
        header = self.open_table.get_cell_value(row,col)
        if header == "yes":
            return True
        else:
            return None

    # 获取请求方式
    def get_method(self,row):
        col = int(get_request_way())
        request = self.open_table.get_cell_value(row,col)
        return request

    # 获取url
    def get_url(self,row):
        col = int(get_url())
        url = self.open_table.get_cell_value(row,col)
        return url

    # 获取请求参数
    def get_data(self,row):
        col = int(get_data())
        data = self.open_table.get_cell_value(row,col)
        if data == "":
            return None
        return data

    # 通过关键字获取参数
    def get_data_for_json(self,row):
        data = data_values()
        data_json = data.get_data(self.get_data(row))
        return data_json

    # 获取预期结果
    def get_expcet(self,row):
        col = int(get_expect())
        expect = self.open_table.get_cell_value(row,col)
        if expect == "":
            return None
        return expect

