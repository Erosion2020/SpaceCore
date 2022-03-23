import nmap
import socket
import urllib3

urllib3.disable_warnings()

whois_socket_buffered = 4096
whois_query = "whois.apnic.net"
whois_port = 43


# WEB服务扫描
def whois_scan(host, port, arguments):
    res = nmap.PortScanner()
    res.scan(host, port, arguments=arguments)
    for host in res.all_hosts():
        print("<-------------------------------解析host信息------------------------------->")
        print(host, ":", res[host].hostname())
        print("<-------------------------------开始尝试反查信息----------------------------->")
        socket_con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_con.connect((whois_query, whois_port))
        socket_con.send(bytes(f"{host}\r\n".encode("utf-8")))
        server_info = bytearray()
        while True:
            data = socket_con.recv(whois_socket_buffered)
            if not len(data):
                break
            server_info.extend(data)
        socket_con.close()
        print(bytes(server_info).decode("ASCII"))
    return


def start():
    host = input("输入主机IP地址或域名,如[edu.hetianlab.com]")
    port = input("输入端口范围,默认[22-8888]")
    if port == '':
        port = '22-8888'
    args = input("输入要新增的nmap参数,默认[ -sV -Pn ]") + ' -sV -Pn '
    whois_scan(host, port, args)
