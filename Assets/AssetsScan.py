import requests
import urllib3
import nmap

urllib3.disable_warnings()


def http_https_request(headers, req_url, port):
    try:
        print(f"侦测到目标主机端口{port}使用TCP协议 开始尝试WEB HTTP/HTTPS 应用解析")
        req = requests.Session()
        web_response = req.get(req_url, headers=headers, verify=False)
        print(f"响应状态码: {web_response.status_code}\t响应HTTP头信息:{web_response.headers}")
        print(f"")
        req.close()
    except Exception:
        print("尝试获取HTTP/HTTPS信息失败\n")


# 构建默认请求头
def default_request_headers(host):
    headers = {
        "Host": f"{host}",
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0',
        "Accept": "*/*",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1"
    }
    return headers


# WEB服务扫描
def http_assets_scan(host, port, arguments):
    protocol_dic = {'ssh': []}
    res = nmap.PortScanner()
    res.scan(host, port, arguments=arguments)
    req_header = default_request_headers(host)
    for port in res[host]['tcp']:
        print(f"<---------------------获取{port}端口信息--------------------->")
        print(f"port:{port} INFO:{res[host]['tcp'][port]}")
        if res[host]['tcp'][port]['name'] == 'http':
            req_url = f"https://{res[host].hostname()}:{port}/"
            http_https_request(headers=req_header, req_url=req_url, port=port)
        elif res[host]['tcp'][port]['name'] == 'ssh':
            protocol_dic['ssh'].append({'host': host, 'port': port})
    return protocol_dic


def start():
    host = input("输入主机IP地址或域名,如[edu.hetianlab.com]")
    port = input("输入端口范围,默认[22-8888]")
    if port == '':
        port = '22-8888'
    args = input("输入要新增的nmap参数,默认[ -sV -Pn ]") + ' -sV -Pn '
    http_assets_scan(host, port, args)

