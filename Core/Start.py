import sys

import Assets
import Blasting.Start
import Impact.Start

name = "SpaceCore"
input_message = f"[{name} #]"


# 帮助菜单
def menu():
    print("---------------------------Space Core----------------------------")
    print("1、信息收集")
    print("2、漏洞利用")
    print("3、字典爆破")
    print("输入exit退出脚本/输入help查看帮助")
    print("------------------------------END--------------------------------")


# 帮助手册
def menu_help():
    print("选择您想要使用的模块,按下回车即可......")


# 启动
def start():
    menu()
    while True:
        option = input(input_message)
        if option == 'exit':
            print("Good Bye!")
            sys.exit(0)
        if option == '1':
            Assets.Start.start()
        elif option == '2':
            Impact.Start.start()
        elif option == '3':
            Blasting.Start.start()
        elif option == 'help':
            menu()
            menu_help()
        else:
            print("无效的输入,请重新输入\n")
