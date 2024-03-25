
import requests

session = requests.session()

global token
token = ''
# 以买家登录接口为例

def login_buyer(username='shamo',password='07d21aad0a7217d58111bc8ae421bc34'):
    # 针对接口发起调用，需要知道接口的哪些信息？
    # 接口地址、请求头信息、请求参数、接口请求方式
    url = 'http://www.mtxshop.com:7002/passport/login'
    # 在swagger文档上这个接口有头信息
    headers = {
        "Authorization":""
    }

    # 表单参数
    data = {
        "username":username,
        "password": password,
        "captcha": "1512",
        "uuid": "asddsfsdfsdfsdfff",
    }
    # 发起接口调用，拿到响应结果
    resp = session.post(url=url,data=data,headers=headers)
    # 获取响应状态码
    status_code = resp.status_code
    print(f'响应状态码是:{status_code}')
    # 获取响应body信息的字符串类型数据
    resp_text = resp.text
    print(f'响应body信息的字符串类型数据:{resp_text}')

    # 获取响应body信息的json类型数据，对应的就是python里的字典嵌套或者列表嵌套
    resp_json = resp.json()
    print(f'响应body信息的json类型数据:{resp_json}')
    # 提取access_token
    global token
    token = resp_json['access_token']

def buy_now(sku_id=541,num=1,activity=''):
    url = 'http://www.mtxshop.com:7002/trade/carts/buy'
    # 在swagger文档上这个接口有头信息
    headers = {
        "Authorization":token
    }
    data = {
        "sku_id":sku_id,
        "num":num,
        "activity_id":activity
    }
    # 发起接口调用，拿到响应结果
    resp = session.post(url=url,data=data,headers=headers)
    # 获取响应状态码
    status_code = resp.status_code
    print(f'响应状态码是:{status_code}')
    # 获取响应body信息的字符串类型数据
    resp_text = resp.text
    print(f'响应body信息的字符串类型数据:{resp_text}')
    return resp

    # 立即购买接口一旦成功，响应body信息是空的，不能使用resp.json()获取
    # 获取响应body信息的json类型数据，对应的就是python里的字典嵌套或者列表嵌套
    # resp_json = resp.json()
    # print(f'响应body信息的json类型数据:{resp_json}')

def add_cart(sku_id=541,num=1,activity=''):
    url = 'http://www.mtxshop.com:7002/trade/carts'
    # 在swagger文档上这个接口有头信息
    headers = {
        "Authorization":token
    }
    data = {
        "sku_id":sku_id,
        "num":num,
        "activity_id":activity
    }
    # 发起接口调用，拿到响应结果
    resp = session.post(url=url,data=data,headers=headers)
    # 获取响应状态码
    status_code = resp.status_code
    print(f'响应状态码是:{status_code}')
    # 获取响应body信息的字符串类型数据
    resp_text = resp.text
    print(f'响应body信息的字符串类型数据:{resp_text}')
    return resp