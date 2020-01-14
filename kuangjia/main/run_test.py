# -*- coding: utf-8 -*-
import sys
sys.path.append("E:\pycharm\kuangjia")
from kuangjia.base.demo import Runmain
from kuangjia.Excel.get_row import get_values

class RunTest:
    def __init__(self):
        self.Run_main = Runmain()
        self.value = get_values()

    # 程序执行获取信息进行执行,这里是获取行号
    def go_on_run(self):
        res = None
        rows_count = self.value.get_nrows()
        for i in range(1,rows_count):
            url = self.value.get_url(i)
            method = self.value.get_method(i)
            is_run = self.value.get_is_run(i)
            data = self.value.get_data(i)
            header = self.value.get_header(i)
            print('url:', url)
            print('method:', method)
            print('is_run:', is_run)
            print('data:', data)
            print('header:', header)
            if is_run:
                res = self.Run_main.run_set(url,method,data,header)
                print("*" * 60 + "分割线" + "*" * 60)
        return res

if __name__ == '__main__':
    fp = RunTest()
    print(fp.go_on_run())
