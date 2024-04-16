import pytest
import requests
import json
import pandas as pd
# from ..config.const import excel_data


def get_excel_data_case(interface_type):
    data = pd.read_excel("./case_data/Excel_case.xlsx")#[6 rows x 9 columns]
    #需要访问读出的Excel数据中的一列
    #选出所有data['请求接口类别'] == interface_type，的列
    interface_type_data = data[data['请求接口类别'] == interface_type]
    final_data = []

    start_index = 0
    # print(interface_type_data.index)  给选出来的列生成索引
    for i in interface_type_data.index:#遍历选出的列
        inner_data = {}
        # print(interface_type_data.iloc[[0]]) 把选出来的列，从0开始索引列
        for d in interface_type_data.iloc[[start_index]]:
            inner_data[d] = interface_type_data[d][i]
        final_data.append(inner_data)
    return final_data
    #我觉得这样的函数需要，传入文件地址，输出文件的data_case
# excel_data = "../case_data/Excel_case.xlsx"
# x =  get_excel_data_case(excel_data,"登录")
# print(x)

#[{'编号': 'login-01', '标题': '正确的登录', '请求接口类别': '登录', '请求地址': '/loginWithJwt', '请求方式': 'get', '是否需要登录': 0, '输入数据': '{"userName":"imooc","password":"12345678"}', '数据格式': 'params', '期望结果': 10000}, {'编号': 'login-02', '标题': '错误的登录', '请求接口类别': '登录', '请求地址': '/loginWithJwt', '请求方式': 'get', '是否需要登录': 0, '输入数据': '{"userName":"imooc","password":"123456789"}', '数据格式': 'json', '期望结果': 10006}]
#[{'编号': 'login-01', '标题': '正确的登录', '请求接口类别': '登录', '请求地址': '/loginWithJwt', '请求方式': 'get', '是否需要登录': 0, '输入数据': '{"userName":"imooc","password":"12345678"}', '数据格式': 'params', '期望结果': 10000}, {'编号': 'login-01', '标题': '正确的登录', '请求接口类别': '登录', '请求地址': '/loginWithJwt', '请求方式': 'get', '是否需要登录': 0, '输入数据': '{"userName":"imooc","password":"12345678"}', '数据格式': 'params', '期望结果': 10000}]
