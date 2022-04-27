import requests
import urllib3

urllib3.disable_warnings()


def start(ip, port):
    req = requests.Session()
    live_url = f"http://{ip}:{port}/console/login/LoginForm.jsp"
    resp = req.get(url=live_url)
    if resp.status_code == 200:
        print(f"[*] Web logic 控制台地址是: {live_url}")
    else:
        print("目标默认控制台地址是关闭的.")


if __name__ == "__main__":
    start('10.100.30.141', 49163)
