import requests


def get():
    #针对接口发起调用，需要知道哪些信息
    #接口地址，请求头信息，请求参数，接口请求方式
    url = 'https://www.baidu.com/'
    #这个地址用不了了

    #查询参数，将它定义成字典
    params={
        "paragort_type":"HELP"
    }
    # 发起接口调用，得到响应结果
    # resp是响应对象，包括了响应头信息、响应状态码、响应body体信息
    resp = requests.get(url=url, params=params)

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
    get()
