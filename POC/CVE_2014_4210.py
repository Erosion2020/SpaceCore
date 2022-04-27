import requests
import urllib3

urllib3.disable_warnings()
index = "CVE_2014_4210"


def start(ip, port):
    fragile_url = f"http://{ip}:{port}/uddiexplorer/"
    header = {
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36"
    }
    req = requests.Session()
    resp = req.get(url=fragile_url, headers=header)
    if resp.status_code == 200:
        print(f"[*] {ip}:{port} 存在WebLogic UDDIExplorer SSRF 漏洞,CVE编号[{index}]")
    else:
        print(f"[ ] {ip}:{port} 未检测到[{index}]漏洞")


if __name__ == "__main__":
    start('10.100.30.141', 49163)
