import FragileScan.WebLogic
from FragileScan import WebLogic

name = "FragileScan"
input_message = f"[{name} #]"


def assets_help():
    print("----------------------FragileScan----------------------")
    print("1、Web Logic 常见CVE漏洞扫描")
    print("输入exit退出脚本")
    print("-----------------------END------------------------")


def start():
    assets_help()

    while True:
        option = input(input_message)
        if option == 'exit':
            break
        elif option == '1':
            FragileScan.WebLogic.start()
        else:
            print("无效的输入,请重新输入\n")
            assets_help()
