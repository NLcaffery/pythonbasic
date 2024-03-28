
from requests_study.mtxshop_apis import buy_now, login_buyer

# 模块级别前置
def setup_module():
    login_buyer()
    print('当前文件下所有用例开始之前，执行我')
def teardown_module():
    print('当前文件下所有用例执行完成后执行我')

# 函数级别的，在当前文件下有多少个函数用例就会执行多少次
def setup_function():
    print('当前文件下每条函数用例执行前，执行我')
def teardown_function():
    print('当前文件下每条函数用例执行完成后执行我')

def test_buy_now():
    # 调用立即购买接口封装的函数
    # login_buyer()
    resp = buy_now()
    # 断言状态码
    assert resp.status_code == 200

def test_buy_now_skuid_exception():
    # 调用立即购买接口封装的函数
    # login_buyer()
    resp = buy_now(sku_id=763263663)
    # 断言状态码
    assert resp.status_code == 500
    # 响应结果当做整体字符串做对比
    assert resp.text == '{"code":"004","message":"不合法"}'