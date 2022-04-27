import requests
import urllib3
urllib3.disable_warnings()

index = "CVE_2018_2894"
headers = {
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Content-Type": "text/xml",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36"
}


def start(ip, port):
    req_urls = [f"http://{ip}:{port}/ws_utc/begin.do", f"http://{ip}:{port}/ws_utc/config.do"]
    fragile = False
    for req_url in req_urls:
        try:
            req = requests.Session()
            if req.get(req_url, headers=headers).status_code == 200:
                fragile = True
        except Exception as ex:
                pass
    if fragile:
        print(f"[*] {ip}:{port} 存在weblogic ws_utc 任意文件上传漏洞,CVE编号[{index}]")
    else:
        print(f"[ ] {ip}:{port} 未检测到[{index}]漏洞")

