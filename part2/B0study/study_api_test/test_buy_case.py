import pytest

from utils.study_utils import get_mysql_case_data
@pytest.fixture(params=get_mysql_case_data("购物车"))

def get_mysql_buycar_data(request):
    return request.param

def test_mysql_buycar_data1(get_mysql_buycar_data):
    print(get_mysql_buycar_data)
