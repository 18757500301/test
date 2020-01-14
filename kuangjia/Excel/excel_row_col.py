# -*- coding: utf-8 -*-
import xlrd

class OpenExcel:
    def __init__(self,file_name=None,file_id=None):
        if file_name:
            self.file_name = file_name
            self.file_id = file_id
        else:
            self.file_name = "E:\\test.xlsx"
            self.file_id = 0
            self.table = self.open_name()
            # 打开一个文件
    def open_name(self):
        name = xlrd.open_workbook(self.file_name)
        sheet_id = name.sheet_by_index(self.file_id)
        return sheet_id

    # 获取文件的总行数
    def get_nrows(self):
        return self.table.nrows

    # 获取文件内某个单元格的数据
    def get_cell_value(self,row,col):
        return self.table.cell_value(row,col)

