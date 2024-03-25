
import requests


# 使用session对象针对多个接口发起调用时，可以做到cookie的自动管理
# 在未来我们做接口自动化，统一的都会使用session发起接口调用，好处是我不用关系cookie了
session = requests.session()

def login():
    # 针对接口发起调用，需要知道接口的哪些信息？
    # 接口地址、请求头信息、请求参数、接口请求方式
    url = 'http://82.156.74.26:9088/pinter/bank/api/login'

    # 表单参数
    data = {
        "userName":"shamo",
        "password": "07d21aad0a7217d58111bc8ae421bc34"
    }
    # 发起接口调用，拿到响应结果
    resp = session.post(url=url,data=data)
    # 获取响应状态码
    status_code = resp.status_code
    print(f'响应状态码是:{status_code}')
    # 获取响应body信息的字符串类型数据
    resp_text = resp.text
    print(f'响应body信息的字符串类型数据:{resp_text}')

    # 获取响应body信息的json类型数据，对应的就是python里的字典嵌套或者列表嵌套
    resp_json = resp.json()
    print(f'响应body信息的json类型数据:{resp_json}')

def query():
    url = 'http://82.156.74.26:9088/pinter/bank/api/query'

    params = {
        "userName":"shamo"
    }
    # 发起接口调用，拿到响应结果
    resp = session.get(url=url,params=params)
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
    login()
    query()