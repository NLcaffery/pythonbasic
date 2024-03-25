
import requests


def put():
    url = 'http://82.156.74.26:9088/pinter/com/phone'
    json = {"brand":"Huawei","color":"yellow","memorySize":"64G","cpuCore":"8核","price":"8848","desc":"全新上市"}

    # 发起接口调用，得到响应对象
    resp = requests.put(url=url, json=json)
    # 获取响应状态码
    status_code = resp.status_code
    print(f'响应状态码是:{status_code}')
    # 获取响应body信息的字符串类型数据
    resp_text = resp.text
    print(f'响应body信息的字符串类型数据:{resp_text}')

    # 获取响应body信息的json类型数据，对应的就是python里的字典嵌套或者列表嵌套
    resp_json = resp.json()
    print(f'响应body信息的json类型数据:{resp_json}')

def delete():
    url = 'http://82.156.74.26:9088/pinter/com/phone'
    json = {"brand":"Huawei","color":"yellow","memorySize":"64G","cpuCore":"8核","price":"8848","desc":"全新上市"}

    # 发起接口调用，得到响应对象
    resp = requests.delete(url=url, json=json)
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
    put()
    delete()