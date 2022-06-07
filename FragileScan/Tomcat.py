import requests
import re
import socket
import time
from POC import TomcatConsole
from POC import CVE_2017_12615

POC_LIST = ['TomcatConsole', 'CVE_2017_12615']


def start():
    ip = input("目标IP: ")
    port = int(input("目标端口: "))
    try:
        for poc in POC_LIST:
            eval(poc).start(ip, port)
    except ConnectionRefusedError:
        print("连接目标失败")
