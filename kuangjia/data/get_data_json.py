# -*- coding: utf-8 -*-
import json

class data_values:
    def __init__(self):
        self.data = self.read_data()

    # 读取文件内的信息
    def read_data(self):
        with open("E:\pycharm\kuangjia\data\data.json") as file:
            data = json.load(file)
            return data

    def get_data(self,id):
        return self.data[id]

if __name__ == '__main__':
    fu = data_values()
    print(fu.get_data("login"))


