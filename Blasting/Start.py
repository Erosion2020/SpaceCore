import Blasting

name = "Blasting"
input_message = f"[{name} #]"


def menu():
    print("-------------------------------弱口令爆破子模块-------------------------------")
    print("1、SSH弱口令爆破")
    print("2、MySQL弱口令爆破")
    print("输入exit退出")
    print("-----------------------------------END-----------------------------------")


def start():
    menu()
    while True:
        option = input(input_message)
        if option == 'exit':
            break
        elif option == '1':
            Blasting.SSH.ssh_blasting()
        elif option == '2':
            Blasting.MySQL.blasting_mysql()
        elif option == 'help':
            menu()
        else:
            print("无效的输入,请重新输入")
