import json

import pytest
import requests
# from excel_utils import get_excel_case_data
from part2.B3Excel.utils import excel_utils as eu

url = "http://111.231.103.117:8083"
@pytest.mark.parametrize(['case_id',
                          'title',
                          'interface_type',
                          'uri',
                          'method',
                          'if_login',
                          'input_data',
                          'data_type',
                          'expect'],eu.get_excel_case_data("登录"))

def test_excel_data_login(case_id,
                          title,
                          interface_type,
                          uri,
                          method,
                          if_login,
                          input_data,
                          data_type,
                          expect):

    if method == "get":
        response = requests.get(url + uri, json.loads(input_data))  # json转格式
        assert 200 == response.status_code  # response返回值

        assert int(expect) == json.loads(response.text)["status"]  # 期望返回的status字段值

    elif method == "post":
        if data_type == "form":
            response = requests.post(url + uri, data=json.loads(input_data))
        elif data_type == "json":
            response = requests.post(url + uri, json=json.loads(input_data))

        assert 200 == response.status_code
        assert int(expect) == json.loads(response.text)["status"]