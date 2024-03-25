
import requests


def upload():
    url = 'http://www.mtxshop.com:7000/uploaders'
    # 文件参数
    files = {
        "file":('logo.png',open(file=r'C:\Users\lixio\Desktop\logo.png',mode='rb'),'image/png'),
        "scene":"goods"
    }
    resp = requests.post(url=url,files=files)
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
    upload()