#使用数据库结合fixture进行参数化
import pytest
import requests
from utils.mysql_utils import get_mysql_case_data

#**
# 1.连接到数据库
# 2.获取到数据
# 3.进行断言
# ##

@pytest.fixture(params=get_mysql_case_data("登录"))
def get_mysql_login_data(requests):
    return requests.param

def test_mysql_login1(get_mysql_login_data):
   print(get_mysql_login_data)