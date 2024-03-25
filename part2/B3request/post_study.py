
import requests



# 以买家登录接口为例

def login_buyer():
    # 针对接口发起调用，需要知道接口的哪些信息？
    # 接口地址、请求头信息、请求参数、接口请求方式
    url = 'http://www.mtxshop.com:7002/passport/login'
    # 在swagger文档上这个接口有头信息
    headers = {
        "Authorization":""
    }

    # 表单参数
    data = {
        "username":"shamo",
        "password": "07d21aad0a7217d58111bc8ae421bc34",
        "captcha": "1512",
        "uuid": "asddsfsdfsdfsdfff",
    }
    # 发起接口调用，拿到响应结果
    resp = requests.post(url=url,data=data,headers=headers)
    # 获取响应状态码
    status_code = resp.status_code
    print(f'响应状态码是:{status_code}')
    # 获取响应body信息的字符串类型数据
    resp_text = resp.text
    print(f'响应body信息的字符串类型数据:{resp_text}')

    # 获取响应body信息的json类型数据，对应的就是python里的字典嵌套或者列表嵌套
    resp_json = resp.json()
    print(f'响应body信息的json类型数据:{resp_json}')


def post_json():
    # 针对接口发起调用，需要知道接口的哪些信息？
    # 接口地址、请求头信息、请求参数、接口请求方式
    url = 'http://82.156.74.26:9088/pinter/com/register'
    # json参数
    json = {
        "userName":"test",
        "password":"1234",
        "gender":1,
        "phoneNum":"110",
        "email":"beihe@163.com",
        "address":"Beijing"
    }
    # 发起接口调用，得到响应对象
    resp  =requests.post(url=url,json=json)
    # 获取响应状态码
    status_code = resp.status_code
    print(f'响应状态码是:{status_code}')
    # 获取响应body信息的字符串类型数据
    resp_text = resp.text
    print(f'响应body信息的字符串类型数据:{resp_text}')

    # 获取响应body信息的json类型数据，对应的就是python里的字典嵌套或者列表嵌套
    resp_json = resp.json()
    print(f'响应body信息的json类型数据:{resp_json}')

if __name__ == '__main__':
    login_buyer()
    post_json()

