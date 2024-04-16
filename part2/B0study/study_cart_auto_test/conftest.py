#必须叫这个文件名
import pytest
import requests
import json
from config.const import url
@pytest.fixture(scope="session",autouse=True)
def get_login_token():
    login_uri = "/loginWithJwt"
    login_data = {
        "userName":"imooc",
        "password":"12345678",
    }
    login_response = requests.get(url + login_uri,
                                  login_data)
    data = json.loads(login_response.text)
    jwt_token = data['data']
    return jwt_token