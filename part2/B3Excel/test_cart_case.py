import pytest
import requests
import json
from config.const import url
import utils.mysql_utils as um
import utils.excel_utils as ue
#*
# 1.获取token
#2.参数化
#3.测试
# *#
@pytest.fixture()
def get_token(get_login_token):
    return get_login_token

@pytest.fixture()
def get_params():
    return ue.get_excel_case_data("购物车")

def test_excel_cart_add(get_token,get_params):
    params = get_params
    jwt_token = get_token
    # print(params)
    for request_data in params:
        case_id = request_data['编号']
        title = request_data['标题']
        interface_type = request_data['请求接口类别']
        uri = request_data['请求地址']
        method = request_data['请求方式']
        if_login = request_data['是否需要登录']
        input_data = request_data['输入数据']
        data_type = request_data['数据格式']
        expect = request_data['期望结果']

        if if_login == 1:
            headers = {
                "jwt_token":jwt_token
            }
            if method == "get":
                response = requests.get(url + uri,
                                        input_data,
                                        headers=headers)
                assert 200 == response.status_code
                assert expect == json.loads(response.text)['status']
            elif method == "post":
                if data_type == "form":
                    response = requests.post(url+uri,data=input_data,headers=headers)
                    assert 200 == response.status_code
                    assert expect == json.loads(response.text)['status']
                elif data_type == "json":
                    response = requests.post(url + uri, data=input_data, headers=headers)
                    assert 200 == response.status_code
                    assert expect == json.loads(response.text)['status']

        elif if_login == 0:
            if method == "get":
                response = requests.get(url + uri,
                                        input_data,
                                        )
                assert 200 == response.status_code
                assert expect == json.loads(response.text)['status']
            elif method == "post":
                if data_type == "form":
                    response = requests.post(url+uri,data=input_data)
                    assert 200 == response.status_code
                    assert expect == json.loads(response.text)['status']
                elif data_type == "json":
                    response = requests.post(url + uri, data=input_data)
                    assert 200 == response.status_code
                    assert expect == json.loads(response.text)['status']
