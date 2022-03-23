import Blasting

name = "Blasting"
input_message = f"[{name} #]"


def menu():
    print("-------------------------------字典爆破子模块-------------------------------")
    print("1、SSH爆破")
    print("输入exit退出")
    print("-----------------------------------END-----------------------------------")


def start():
    menu()
    while True:
        option = input(input_message)
        if option == 'exit':
            break
        if option == '1':
            Blasting.SSH.ssh_blasting()
        else:
            print("无效的输入,请重新输入")
