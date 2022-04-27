import requests
import re
import socket
import time
from POC import CheckLive
from POC import CVE_2014_4210
from POC import CVE_2016_0638
from POC import CVE_2016_3510
from POC import CVE_2017_3428
from POC import CVE_2017_3506
from POC import CVE_2017_10271
from POC import CVE_2018_2628
from POC import CVE_2018_2893
from POC import CVE_2018_2894
from POC import CVE_2018_3191
from POC import CVE_2019_2725
from POC import CVE_2019_2729
from POC import CVE_2019_2890
from POC import CVE_2020_14882

POC_LIST = ['CheckLive', 'CVE_2014_4210', 'CVE_2016_0638', 'CVE_2016_3510', 'CVE_2017_3428', 'CVE_2017_3506',
            'CVE_2017_10271', 'CVE_2018_2628', 'CVE_2018_2893', 'CVE_2018_2894', 'CVE_2018_3191', 'CVE_2019_2725',
            'CVE_2019_2729', 'CVE_2019_2890', 'CVE_2020_14882']


def start():
    ip = input("目标IP: ")
    port = int(input("目标端口: "))
    try:
        for poc in POC_LIST:
            eval(poc).start(ip, port)
    except ConnectionRefusedError:
        print("连接目标失败")


