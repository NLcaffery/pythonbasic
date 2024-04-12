#使用数据库结合fixture进行参数化
import json

import pytest
import requests
from utils.mysql_utils import get_mysql_case_data

#**
# 1.连接到数据库
# 2.获取到数据
# 3.进行断言
# ##
#parames是数据库返回的参数，
#所以我们借助一个工具方法得到数据库返回的参数
url = "http://111.231.103.117:8083"
@pytest.fixture(params=get_mysql_case_data("登录"))
def get_mysql_login_data(request):
    return request.param

#该方法是把上面传来的数据做一个解析,
def test_mysql_login1(get_mysql_login_data):
   # print(get_mysql_login_data)#打印出来是元组类型的数据
   # 按字段打印
   id = get_mysql_login_data[0]
   case = get_mysql_login_data[1]
   title = get_mysql_login_data[2]
   interface_type = get_mysql_login_data[3]
   method = get_mysql_login_data[5]
   uri = get_mysql_login_data[4]
   if_login = get_mysql_login_data[6]
   input_data = get_mysql_login_data[7]
   data_type = get_mysql_login_data[8]
   expect = get_mysql_login_data[9]

   # **
   # 在Python的单元测试框架中，assert 语句用于验证某个条件是否为真。
   # 如果条件为真（即表达式的结果为 True），则测试继续执行；如果条件为假（即表达式的结果为 False），则测试会立即失败，
   # 并抛出一个 AssertionError 异常。
   #
   # 在这行代码中，response.status_code 是从HTTP响应对象中提取的状态码。
   # 如果这个状态码等于200，assert 语句就会通过，表示这个HTTP请求成功地返回了预期的响应。
   # 如果状态码不是200，assert 语句就会失败，测试也会因此失败，
   # 这通常意味着请求没有成功
   # *#

   if method == "get":
       response = requests.get(url + uri,json.loads(input_data))#json转格式
       assert 200 == response.status_code#response返回值
       # print("response",response)#<Response [200]>
       # print("response.status_code",response.status_code)#200
       # print("response.text",response.text)
       #{"status":10000,"msg":"SUCCESS","data":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX3JvbGUiOjIsInVzZXJfaWQiOjksInVzZXJfbmFtZSI6Imltb29jIiwiZXhwIjoxNzk5MzAzNzczfQ.nmKW1cwu4lttvXZBuR-n8hJgpHxPwiNHEPKwffr9jEE"}
       #**
       # 在本代码中，response.text
       # 是从HTTP响应对象 response 中提取的文本内容。
       # 当你使用 requests 库发送一个HTTP请求（如GET或POST请求）时，
       # 返回的响应对象 response 包含了许多关于该响应的信息，
       # 包括状态码（response.status_code）、
       # 头部信息（response.headers）
       # 以及响应的主体内容（response.text 或 response.content）。
       #
       # response.text 通常包含响应的主体内容，并且是以Unicode字符串的形式表示的。这意味着如果响应的内容是JSON、HTML、XML或其他文本格式，你可以直接通过 response.text 访问它。对于JSON格式的响应，你通常会先使用 json.loads(response.text) 将其解析成一个Python字典或列表，然后进一步处理。
       # *#
       assert int(expect) == json.loads(response.text)["status"]#期望返回的status字段值

   elif method == "post":
       if data_type == "form":
           response = requests.post(url+uri,data=json.loads(input_data))
       elif data_type == "json":
           response = requests.post(url + uri, json=json.loads(input_data))

       assert 200 == response.status_code
       assert int(expect) == json.loads(response.text)["status"]
