import sys
import Assets
import getopt

name = "Assets"
input_message = f"[{name} #]"


def assets_help():
    print("----------------------Assets----------------------")
    print("1、whois [域名/IP]查询")
    print("2、基于目标主机的NMAP扫描及简单HTTP资产发现")
    print("输入exit退出脚本")
    print("-----------------------END------------------------")


def start():
    assets_help()

    while True:
        option = input(input_message)
        if option == 'exit':
            break
        elif option == '1':
            Assets.Domain.start()
        elif option == '2':
            Assets.AssetsScan.start()
        else:
            print("无效的输入,请重新输入\n")
