import requests
import urllib3

urllib3.disable_warnings()


def start(ip, port):
    req = requests.Session()
    manager_url = f"http://{ip}:{port}/manager/html"
    resp = req.get(url=manager_url, verify=False)
    if resp.status_code != 404:
        print(f"[*] Tomcat 后台地址是: {manager_url}")
    else:
        print("目标默认控制台地址是关闭的.")


if __name__ == "__main__":
    start("43.154.84.186", "8081")
