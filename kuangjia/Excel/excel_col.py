# -*- coding: utf-8 -*-
class global_var:
    id = "0"                   # 表格中的序列号
    request_name = "1"         # 模块名称
    url = "2"                  # 表格中的url
    run = "3"                  # 是否执行
    request_way = "4"          # 表格中的请求方式
    header = "5"               # 表格中的请求头
    case_depend = "6"          # 表格中的请求数据的依赖
    data_depend = "7"          # 表格中的请求数据的依赖
    field_depend = "8"         # 表格中的请求数据的依赖
    data = "9"                 # 表格中的请求参数
    expect = "10"               # 表格中的预期结果
    result = "11"               # 表格中的实际结果

def get_id():
    return global_var.id
def get_url():
    return global_var.url
def get_run():
    return global_var.run
def get_request_way():
    return global_var.request_way
def get_header():
    return global_var.header
def get_case_depend():
    return global_var.case_depend
def get_data_depend():
    return global_var.data_depend
def get_field_depend():
    return global_var.field_depend
def get_data():
    return global_var.data
def get_expect():
    return global_var.expect
def get_result():
    return global_var.result

